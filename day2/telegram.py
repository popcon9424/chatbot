import requests
from time import sleep
import bs4
import webbrowser

url = "https://naver.com"
search_url = "https://search.naver.com/search.naver?query="

response = requests.get(url).text

doc = bs4.BeautifulSoup(response, 'html.parser')

result = []

result = doc.select('.ah_k')

msg = ""

# url = f"https://api.telegram.org/bot{key}/getMe"

key = "환경변수"

# user_id = "환경변수"

# "sendMessage?chat_id=635406153&text=message_from_chatbot"


# 실시간 검색어 스크래핑을 통한 메세지 보내기
for i in range(600):
    sleep(1)
    msg = result[i%20].text
    url = f"https://api.telegram.org/{key}/sendMessage?chat_id=665624074&text={msg}"
    requests.get(url)