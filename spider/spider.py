import urllib.request
import re
import time
import os
import sys
from PIL import Image

def getCurrentDate():
    return str(t.__getattribute__("tm_year"))+"-"+str(t.__getattribute__("tm_mon"))+"-"+str(t.__getattribute__("tm_mday"))

def filterImage(folderPath, width, height):
    pass


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
    print(title)
    return title

def downImg(html, foldername):
    reg = r'\s+src="(http.*?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    t = time.localtime(time.time())
    dicpath = 'D:\\ImageDownload\\%s' % (foldername)

    if not os.path.exists(dicpath):
        os.makedirs(dicpath)
    x = 0
    for imgurl in imglist:
        target = dicpath+'\\%s.jpg' % x  
        #print('Downloading image to location: ' + target + '\nurl=' + imgurl)
        try:
            image = urllib.request.urlretrieve(imgurl, target)
            print('%s%s%s' % (x, '/', len(imglist)))
        except:
            print(sys.exc_info()[0])
        else:
            x += 1
    return dicpath

def filterImage(dicpath, width, height):
    for filename in os.listdir(dicpath):
        picpath = os.path.join(dicpath, filename)
        image = Image.open(picpath)
        if image.size < (width, height):
            os.remove(picpath)

def writeUrl(targetPath, content):
    f = open(targetPath, "a")
    f.write(content)
    f.close()            

if __name__ == '__main__':
    targetDicPath = "D:\\ImageDownload"
    logUrlFileName = "readme.txt"
    isExit = True
    while isExit:
        url = input("Please enter the URL:")
        if url=='exit':
            isExit = False
        else:
            html = getHtml(url)
            foldername = getTitle(html)
            writeUrl(os.path.join(targetDicPath, logUrlFileName), "\n%s(%s)" % (url, foldername))
            dicpath = downImg(html, foldername)
            print("Download has finished.")
            #isFilterSize = input("Do you want to filter the size?(yes/no):")
            #iisFilterSize == "yes" or isFilterSize == "y"
            if(False):
                width = int(input("Please enter width:"))
                height = int(input("Please enter height:"))
                filterImage(dicpath, width, height)
                print("Filter has finished.")
            
        
           
