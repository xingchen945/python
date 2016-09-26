#coding:utf-8
import urllib.request
url = "http://tieba.baidu.com/p/1000000000"
for i in range(10):
    url = url[0:-1] + str(i)
    dStr = urllib.request.urlopen(url).read()
    title = url.split('/')[-1] + ".html"
    f = open(title,'wb')
    f.write(dStr)
    f.close()
print("End")
