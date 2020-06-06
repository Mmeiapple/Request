import requests
import re
import random
name=random.randint(1,1000)
proxies={"http":"http://127.0.0.1:8888"}
sessions=requests.session()

#打开网页
response1=sessions.get('http://47.107.178.45/phpwind/',proxies=proxies)
body=response1.content.decode('utf-8')
value=re.findall('csrf_token" value="(.+?)"/><',body)[0]
print(value)

#登录
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


#发帖

data={'c':'post','a':'doadd','_json':'1','fid':'81'}
headifons={'Accept': 'application/json, text/javascript, */*; q=0.01',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
           'X-Requested-With': 'XMLHttpRequest',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
tag=str(name)+'发帖标题'
content=str(name)+'发帖内容'

form={'special':'default','reply_notice':'1','atc_title':tag,'atc_content':content,'csrf_token':value,'pid':'','tid':''}
response3=sessions.post(url='http://47.107.178.45/phpwind/index.php',params=data,headers=headifons,data=form)
print(response3.content.decode('utf-8'))