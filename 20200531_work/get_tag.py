import requests
import re


class GetToken:
    def __init__(self,appid,secret):
        data={'grant_type':'client_credential','appid':appid,'secret':secret}
        self.response = requests.get('https://api.weixin.qq.com/cgi-bin/token?', params=data)
        self.response.content.decode('utf-8')


# data={'grant_type':'client_credential','appid':'wx60536c088aee3040','secret':'f214d833f873d8cc1b38255eca0938d9'}
# response=requests.get('https://api.weixin.qq.com/cgi-bin/token?',params=data)
# print(response.content.decode('utf-8'))