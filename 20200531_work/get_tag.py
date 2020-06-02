import requests
import re


class GetToken:
    def __init__(self,appid,secret):
        data={'grant_type':'client_credential','appid':appid,'secret':secret}
        self.response = requests.get('https://api.weixin.qq.com/cgi-bin/token?', params=data)
        self.response.encoding='utf-8'
    def get_token(self):
        content=str(self.response.text)
        result=re.match('"access_token":"(.+)"',content)
        return result.group(1)

if __name__=="__main__":
    a=GetToken('wx60536c088aee3040','f214d833f873d8cc1b38255eca0938d9')
    print(a.get_token())
# data={'grant_type':'client_credential','appid':'wx60536c088aee3040','secret':'f214d833f873d8cc1b38255eca0938d9'}
# response=requests.get('https://api.weixin.qq.com/cgi-bin/token?',params=data)
# print(response.content.decode('utf-8'))