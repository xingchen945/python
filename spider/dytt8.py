import requests
from bs4 import BeautifulSoup
import win32api

url = 'http://www.dytt8.net/'
default_xunlei_path = 'D:\Program Files (x86)\Thunder Network\Thunder9\Program\Thunder.exe'

# 获取最近电影
def getNewFilms():
    dict_films = {}    
    res = requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser', from_encoding="GB18030")
        new_films = soup.select('div[class="co_content8"]')[0].select("tr")
        for item in new_films[1:]:
            tag = item.select("a")[1]
            film_title = tag.getText()
            film_url = url + tag.attrs['href']
            dict_films[film_title] = film_url
    return dict_films

# 输出最近电影
def outputFilms(dict_films):
    output_films = {}
    index = 0
    for item in dict_films:
        index += 1
        output_films[index] = item
        print("%s 、 %s" % (index, item))
    return output_films

def getDownloadUrl(film_url):
    res = requests.get(film_url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser', from_encoding="GB18030")
        return soup.find_all("table")[1].find("a").attrs["href"]

def download(exe_path, download_url):
    win32api.ShellExecute(0, "open", exe_path, download_url, '', 1)



if __name__ == '__main__':
    input_xunlei_path = input("请输入迅雷路径或者直接修改源码的默认路径：")
    if input_xunlei_path.strip() == "":
        input_xunlei_path = default_xunlei_path
    dict_films = getNewFilms()
    output_films = outputFilms(dict_films)
    num = int(input("请输入要下载电影编号或者0结束："))
    while num != 0:
        film_url = dict_films[output_films[num]]
        download_url = getDownloadUrl(film_url)
        download(input_xunlei_path, download_url)
        num = int(input("请输入要下载电影编号或者0结束："))
    print("再见")
        

