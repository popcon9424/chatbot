import os
import requests
from pprint import pprint as pp

# ?chat_id={chat_id}&text={name}
# string 수술 (interpolation)
# 1. f-string
# print(f"Hello, {name}")

# # 2. format()
# print("Hello, {}".format(name))

token = os.getenv('TELEGRAM_TOKEN')

msg = input()

# AGENDA : 텔레그램 메세지를 보낼거임 (sendMsg)
## I. chat_id 받아오는 기능(function)
# 1. 환경변수를 불러와서
# 2. url을 만들고
# 3. getUpdates
# 4. chat_id
#--------------------------------------
## II. 메세지를 보내는 기능(function)
# 5. url 다시 만들고
# 6. 메세지를 보냄

def getID(token):    # => chat_id
    # url (base_url + token + methods)
    url = f"https://api.telegram.org/bot{token}/getUpdates"

    res = requests.get(url)
    doc = res.json()
    # json.loads(json) => python dictionary
    chat_id = doc['result'][0]['message']['chat']['id']

    return chat_id


def sendMessage(token, chat_id, msg):   # => 텔레그램 메세지를 보냄( requests.get(url) )
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)
    print(f"{msg} 를 성공적으로 보냈습니다")


sendMessage(token, getID(token), msg)

# def sendURL():
#     method = "sendMessage"
#     url = f"https://api.telegram.org/bot{token}/{method}"
#     return url

# url = sendURL()

# requests.get(f'{url}?chat_id={chat_id}&text={name}')


# def sendMsg(msg):   # => 텔레그램 메세지를 보냄( requests.get(url) )
#     token = os.getenv('TELEGRAM_TOKEN')
#     method = "getUpdates"
#     url = f"https://api.telegram.org/bot{token}/{method}"
#     chat_id = requests.get(url).json()['result'][0]['message']['chat']['id']

#     method = "sendMessage"
#     requests.get(f"https://api.telegram.org/bot{token}/{method}?chat_id={chat_id}&text={msg}")