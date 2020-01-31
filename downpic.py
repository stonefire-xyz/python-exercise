#coding=utf-8
import re
import urllib.request
def getHtml(url):
    page=urllib.request.urlopen(url)
    html=page.read();
    return html
def getImage(html):
    reg=r'src="(.*?\.jpg)"'
    imgre=re.compile(reg)
    imgeList = imgre.findall(html)
    x=0
    for image in imgeList:
        urllib.request.urlretrieve(image,'%s_hhh.jpg' % x)
        x+=1
html=getHtml("https://tieba.baidu.com/p/5256641773")
getImage(html)
