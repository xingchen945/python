import requests
from bs4 import BeautifulSoup
import platform
#import win32api

url = 'http://www.dytt8.net/'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
}
default_xunlei_path = 'D:\Program Files (x86)\Thunder Network\Thunder\Program\Thunder.exe'

# 获取最近电影


def getNewFilms():
    dict_films = {}
    res = requests.get(url, headers = headers)
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser',
                             from_encoding="GB18030")
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
        soup = BeautifulSoup(res.content, 'html.parser',
                             from_encoding="GB18030")
        return soup.find_all("table")[1].find("a").attrs["href"]


def download(exe_path, download_url):
    sysstr = platform.system()
    if sysstr == "Windows":
        pass
        #win32api.ShellExecute(0, "open", exe_path, download_url, '', 1)
    else:
        print(download_url)


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
