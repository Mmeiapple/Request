import requests

#------一、模拟get请求------#
# response=requests.get('https://www.baidu.com')
# print(response.content.decode('utf-8'))
# response.encoding='utf-8'
# print(response.text)

#------二、模拟带参数的get请求------#


# 写法一
response=requests.get('https://api.weixin.qq.com/cgi-bin/token?'
                      'grant_type=client_credential&appid=wx60536c088aee3040&secret=f214d833f873d8cc1b38255eca0938d9')

response.encoding='utf-8'
print(response.text)


# 写法二

# data={'grant_type':'client_credential','appid':'wx60536c088aee3040','secret':'f214d833f873d8cc1b38255eca0938d9'}
# response=requests.get('https://api.weixin.qq.com/cgi-bin/token?',params=data)
# print(response.content.decode('utf-8'))

#------三、自定义请求头------#

# headinfo={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#           'Accept-Encoding':'gzip, deflate, br',
#           'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
#           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
# }
# data={'wd':'上海创蓝文化传播有限公司'}
#
# response=requests.get('https://www.baidu.com/s',params=data,headers=headinfo)
# print(response.content.decode('utf-8'))
