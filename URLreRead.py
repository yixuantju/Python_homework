import requests
from urlextract import URLExtract
import time


def getInput():
  
    url = input('''
    请输入你想爬虫的网址：
(如：http://www.baidu.com
    https://www.bilibili.com)
                 ''')
    depth = eval(input("请输入想要爬虫的深度："))

    return depth, url

start = time.process_time()
def getHTMLText(depth, url):
    global end, n
    try:
        n = 0
        n = n + 1
        if n >= depth:                     #限制递归的深度
            return ""        
        end = time.process_time()
        if int(end-start) >= 20:     #限制程序占用的系统时间
           return "'Warning: Timeout!!'*2"
        r = requests.get(url, timeout=30)
        r.raise_for_status() #如果状态不是200，引发异常 自带异常检查
        r.encoding = 'utf-8' #无论原来用什么编码，都改成utf-8
        extractor = URLExtract()
        urls = extractor.find_urls(r.text) #列表类型
        if urls:                           #去掉空列表
            print(urls)          
    
        #递归检查url网址的对应内容
        for i in range(len(urls)):
            getHTMLText(urls[i])    
    except:
        return ""

def OutputHTML():
    depth, url = getInput()
    getHTMLText(depth, url)




#url = "http://www.baidu.com"
#url = "https://www.bilibili.com"
