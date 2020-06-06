import requests
import re
import random
name=random.randint(1,1000)
print(name)
proxies={"http":"http://127.0.0.1:8888"}
sessions=requests.session()
response1=sessions.get('http://47.107.178.45/phpwind/',proxies=proxies)
body=response1.content.decode('utf-8')
value=re.findall('csrf_token" value="(.+?)"/><',body)[0]
print(value)


# 注册
data={'m':'u','c':'register'}
headifons={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
response2=sessions.get('http://47.107.178.45/phpwind/index.php',params=data,headers=headifons)
# print(response2.content.decode('utf-8'))


data={'m':'u','c':'register','a':'dorun'}
headifons={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
name1=str(name)+'hem'
emai=str(name)+'@qq.com'
print(name1)
form={'username':name1,'password':'123456','repassword':'123456','email':emai,'csrf_token':value}
response3=sessions.post(url='http://47.107.178.45/phpwind/index.php',params=data,headers=headifons,data=form)
print(response3.content.decode('utf-8'))

