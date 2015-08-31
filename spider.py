import urllib.request
import re
import time
import os
import sys

#显示下载进度  
def schedule(a,b,c):  
    '''
    a:已经下载的数据块 
    b:数据块的大小 
    c:远程文件的大小 
   '''  
    per = 100.0 * a * b / c  
    if per > 100 :  
        per = 100  
    print('%.2f%%' % per)

def getCurrentDate():
    return str(t.__getattribute__("tm_year"))+"-"+str(t.__getattribute__("tm_mon"))+"-"+str(t.__getattribute__("tm_mday"))

def getHtml(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    return html.decode()

def getTitle(html):
    reg = r'<title>\s*(.*?)\s*</title>'
    m = re.findall(reg, html)
    title = ''
    if(len(m) > 0):
        title = m[0]
    else:
        title = getCurrentDate()
    return title

def downImg(html):
    reg = r'\s+src="(http.*?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    t = time.localtime(time.time())
    foldername = getTitle(html)
    picpath = 'D:\\ImageDownload\\%s' % (foldername)

    if not os.path.exists(picpath):
        os.makedirs(picpath)
    x = 0
    for imgurl in imglist:
        target = picpath+'\\%s.jpg' % x  
        #print('Downloading image to location: ' + target + '\nurl=' + imgurl)
        try:
            image = urllib.request.urlretrieve(imgurl, target)
            print('%s%s%s',len(imglist),'/',x)
        except:
            print(sys.exc_info()[0])
        else:
            x += 1

def getMenu():
    pass
        

if __name__ == '__main__':
    isExit = True
    while isExit:
        url = input("Please enter the URL:")
        if url=='exit':
            isExit = False
        else:
            html = getHtml(url)
            print("Read html finished.")
            downImg(html)
            print("Download has finished.")
        
           
