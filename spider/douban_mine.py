import requests
import os
from pyquery import PyQuery as pq

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
}

def get_page(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_page(html):
    doc = pq(html)
    return doc


if __name__ == "__main__":
    base_url = "https://book.douban.com/people/xingchen945/"
    base_status = ["wish", "collect", "do"]
    url = ""
    for item in base_status:
        for index in range(0, 20):
            if index == 0:
                url = base_url + item + '?start=' + str(index + 1)
            else:
                url = base_url + item + '?start=' + str(index * 15)
            print(url)    
            doc = pq(url)
            nodes = doc('.subject-item a[title]')
            if len(nodes) != 0:
                for node in nodes:
                    pq_node = pq(node)
                    print(pq_node.attr('title') + "------------------" + item)

