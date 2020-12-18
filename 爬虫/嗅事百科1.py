import re
import urllib.request
def getUserName(url,page):
    #模拟浏览器登陆
    headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36")
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode("utf-8")
    userpat='<h2>(.*?)</h2>'#相应的正则表达式
    contentpat='<span>(.*?)</span>'
    conpat='<br/>'#替代的正则表达式
    data=re.sub(conpat,"",data)#替换函数
    usernamelist=re.compile(userpat,re.S).findall(data)#得到一个列表（关于发帖人的）
    contentlist=re.compile(contentpat,re.S).findall(data)#得到一个列表（关于段子的）
    x=1
    for username in usernamelist:
        print("用户"+str(page)+'-'+str(x)+"是:"+str(username))
        print(str(contentlist[x]))
        x+=1
for i in range(1,4):
    url="https://www.qiushibaike.com/text/"+str(i)#获取它的网页（从第一页到第三页）
    getUserName(url,i)
    print(str(i))