import requests
import re

proxies={"http":"http://127.0.0.1:8888"}
sessions=requests.session()
response1=sessions.get('http://47.107.178.45/phpwind/',proxies=proxies)
body=response1.content.decode('utf-8')
value=re.findall('csrf_token" value="(.+?)"/><',body)[0]
print(value)


headinfos={'Accept':'application/json, text/javascript, */*; q=0.01',
           'X-Requested-With':'XMLHttpRequest',
           'Accept-Encoding':'gzip, deflate',
           'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}

data={'m':'u','c':'login','a':'dologin'}
form_data={'username':'xiaoliusir001',
           'password':'123456',
           'csrf_token':value,
           'csrf_token':value}
response2=sessions.post(url='http://47.107.178.45/phpwind//index.php',params=data,data=form_data,headers=headinfos)
print(response2.content.decode('utf-8'))

