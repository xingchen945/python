import requests
import os
from pyquery import PyQuery as pq

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
}


def get_page(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def parse_page(html):
    doc = pq(html)
    return doc


if __name__ == "__main__":
    url = input("请输入url：")
    html = get_page(url)
    doc = parse_page(html)
