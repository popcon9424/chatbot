# 1. python에게 naver.com 요청을 보내서
# 2. 응답받은 문서를 저장하고
# 3. BeautifulSoup 를 사용해서 정보를 찾기 좋게 만들고
# 4. 우리가 원하는 정보를 뽑아온다.
# 5. webbrowser를 통해 트렌드 1위 단어를 검색한 페이지를 열어주는 코드

import requests
import bs4
import webbrowser

url = "https://naver.com"
search_url = "https://search.naver.com/search.naver?query="

response = requests.get(url).text

doc = bs4.BeautifulSoup(response, 'html.parser')

result = []

# class를 이용한 스크래핑
result = doc.select('.ah_k')

for i in range(20):
    webbrowser.open(search_url+result[i].text)