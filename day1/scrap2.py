import requests
import bs4

url = 'https://finance.naver.com/sise'

response = requests.get(url).text

doc = bs4.BeautifulSoup(response, 'html.parser')

result = doc.select_one('#KOSPI_now')

print(result.text)