# bithumb 에서 코인 이름과 가격 가져오기

import bs4
import requests

url = "https://www.bithumb.com/"

response = requests.get(url).text
doc = bs4.BeautifulSoup(response, "html.parser")
result = doc.select(".sort_real")
result2 = doc.select(".coin_list tr td p a strong")

for i in range(len(result)):
    print(result2[i].text + " : " + result[i].text)