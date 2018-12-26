# kospi 정보를 스크랩한다.

import requests
import bs4

url = "http://finance.daum.net"

response = requests.get(url).text

doc = bs4.BeautifulSoup(response, 'html.parser')

result = doc.select_one('#boxIndexTabs > span > h4')

print(result.text)