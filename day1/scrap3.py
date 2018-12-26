import requests
import bs4

url = 'https://finance.daum.net/domestic'

response = requests.get(url).text

doc = bs4.BeautifulSoup(response, 'html.parser')

result = doc.select_one('#boxDashboard > ul > li:nth-child(1) > a > span > strong')

print(result.text)