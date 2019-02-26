import requests
import os
from urllib.parse import urlencode
from hashlib import md5
from multiprocessing.pool import Pool


def get_page(offset, keyword):
    params = {
        'aid': 24,
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'en_qc': 1,
        'cur_tab': 3,
        'from': 'search_tab',
        'pd': 'synthesis'
    }


url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)

try:
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
except requests.ConnectionError:
    return None


def get_image(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                yield {
                    'image': image.get('url'),
                    'title': title
                }


def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'),
                                             md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Download', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')


def main(offset):
    keyword = input('please input the key:')
    json = get_page(offset, keyword)
    for item in get_images(json):
        print(item)
        save_image(item)


GROUP_START = 1
GROUP_END = 20

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.json()
