import requests

#------一、模拟get请求------#
# response=requests.get('https://www.baidu.com')
# print(response.content.decode('utf-8'))
# response.encoding='utf-8'
# print(response.text)

#------二、模拟带参数的get请求------#


# 写法一
# response=requests.get('https://api.weixin.qq.com/cgi-bin/token?'
#                       'grant_type=client_credential&appid=wx60536c088aee3040&secret=f214d833f873d8cc1b38255eca0938d9')
#
# response.encoding='utf-8'
# print(response.text)


# 写法二

# data={'grant_type':'client_credential','appid':'wx60536c088aee3040','secret':'f214d833f873d8cc1b38255eca0938d9'}
# response=requests.get('https://api.weixin.qq.com/cgi-bin/token?',params=data)
# print(response.content.decode('utf-8'))