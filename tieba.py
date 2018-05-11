#coding:utf-8
import requests
from bs4 import BeautifulSoup
import os

# 测试地址：https://tieba.baidu.com/p/5634733664?see_lz=1

def main():
    url = raw_input('please enter the url:')  #贴吧楼主地址
    path = raw_input('please enter the save path:') #保存路径
    total = input('please enter the max pages:') #总页数

    #url = 'https://tieba.baidu.com/p/5634733664?see_lz=1'
    #path = 'D:\Download\TieBa'
    #total = 3

    if not path:
        path = 'D:\Download\TieBa'

    pn = 0 # 初始第一页

    while pn < total:
        pn = pn + 1
        tempUrl = url + '&pn=' + str(pn)

        response = downloadUrl(tempUrl)

        if response:
            soup = BeautifulSoup(response.content, 'html.parser')    
            if pn == 1:                
                title = getTitle(soup)
                output(title)
                path = createFolder(os.path.join(path,title))
            imgs = getImgUrl(soup)
            for img in imgs:
                downloadImg(path, img['src'])
            output('第' + str(pn) + '页完成')
        else:
            output('错误')    
    
def downloadUrl(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response
    else:
        return None

def getTitle(soup):
    return soup.title.get_text()

def getImgUrl(soup):
    return soup.find_all('img', attrs={'class': 'BDE_Image'})

def downloadImg(path, imgUrl):
    response = requests.get(imgUrl)
    if response.status_code == 200:
        output(imgUrl)
        fileName = os.path.join(path, imgUrl.split('/')[-1]).encode('gb18030')
        #fileName = imgUrl.split('/')[-1] 
        with open(fileName, 'wb') as f:
            f.write(response.content)

def createFolder(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def output(content):
    try:
        print(content.decode('utf8').encode('gb18030'))
    except:

        print(content.encode('gb18030'))


if __name__ == '__main__':
    main()
