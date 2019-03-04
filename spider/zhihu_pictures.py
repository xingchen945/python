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
    #print(doc('figure img'))
    # return doc('figure img')
    return doc


def get_title(doc):
    title = doc('.QuestionHeader-title').text()
    # print(title)
    return title


def get_images_url(doc):
    return doc('figure img')


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def download_img(path, imgUrl):
    print('正在获取：' + imgUrl)
    response = requests.get(imgUrl, headers=headers)
    if response.status_code == 200:
        fileName = os.path.join(path, imgUrl.split('/')[-1])
        with open(fileName, 'wb') as f:
            f.write(response.content)


if __name__ == "__main__":
    url = input("请输入url：")
    html = get_page(url)
    doc = parse_page(html)
    # 获取标题
    title = get_title(doc)
    # 当前路径创建文件夹
    create_folder(title)
    currentPath = os.path.join(os.getcwd(), title)
    # 获取图片地址
    imgs = get_images_url(doc)
    for item in imgs.items():
        # print(item.attr('src'))
        src = item.attr('src')
        if src.endswith('.jpg'):
            download_img(currentPath, src)
