#coding:utf-8
import requests
from bs4 import BeautifulSoup
import os
import json

# 测试地址：https://tieba.baidu.com/p/4440135874?see_lz=1&pn=1
# 总页数：<span class="red">xx</span>

config_path = './config/tieba.json'
save_path = ''
see_lz = 1 

def loadConfig():
    pass



def main():
    url = input('please enter the url:')  #贴吧楼主地址

    if len(save_path) == 0:
        save_path = input('please enter the save path:') #保存路径

    total = int(input('please enter the max pages:')) #总页数


    if not save_path:
        save_path = './'

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
        fileName = os.path.join(path, imgUrl.split('/')[-1])
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
