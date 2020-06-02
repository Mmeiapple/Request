import requests
from bs4 import BeautifulSoup
import re


class GetUrlTitle:
    def __init__(self,url):
        self.response=requests.get(url)


    def get_urltitle(self):
        self.response.encoding='utf-8'
        htmltext=self.response.text
        soup = BeautifulSoup(htmltext,'lxml')
        content=str(soup.title)
        result = re.match('<title>(.+)</title>', content)
        return result.group(1)

if __name__=="__main__":
    title=GetUrlTitle('https://www.baidu.com/')
    a=title.get_urltitle()
    print(title.get_urltitle())

# response=requests.get('https://www.baidu.com/')
# response.encoding='utf-8'
# html=response.text
# suop=BeautifulSoup(html,'lxml')
# print(suop.prettify())
# print(suop.title)