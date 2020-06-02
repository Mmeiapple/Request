import requests
import json


class GetToken:
    def __init__(self,appid,secret):
        data={'grant_type':'client_credential','appid':appid,'secret':secret}
        self.response = requests.get('https://api.weixin.qq.com/cgi-bin/token?', params=data)
        self.response.encoding='utf-8'
    def get_token(self):
        content=self.response.json()
        return content['access_token']


class GetTag:
    def __init__(self,token,url='https://api.weixin.qq.com/cgi-bin/tags/get?'):
        self.url=url
        self.token=token

    def get_tag(self):
        data = {'access_token':self.token}
        response=requests.get(self.url,params=data)
        response.encoding='utf-8'
        return response.json()

if __name__=="__main__":
    token=GetToken('wx60536c088aee3040','f214d833f873d8cc1b38255eca0938d9').get_token()
    content=GetTag(token).get_tag()
    print(json.dumps(content,indent=1,ensure_ascii=False))
