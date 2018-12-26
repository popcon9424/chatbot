import random
import requests
import bs4
import json

my_lotto = sorted(random.sample(range(1,46),6))

# 0. random으로 로또번호를 생성한다.
# 1. 나눔로또 api를 통해 우승 번호를 가져온다.
# 2. random으로 생성된 번호와 우승 번호를 비교해서 나의 등수를 알려준다.
# - 1등 : 6개
# - 2등 : 5개 + 보너스 번호
# - 3등 : 5개
# - 4등 : 4개
# - 5등 : 3개

# json_phonenumber = "{\"john\":\"01012345678\",\"ashley\":\"01098765432\"}"
# dict_phonenumber = json.loads(json_phonenumber)

url = "http://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"

response = requests.get(url).text

dict_res = json.loads(response)

cor_num = []
for i in range(1,7):
    cor_num.append(dict_res["drwtNo"+str(i)])
cor_num = sorted(cor_num)
bonus = dict_res["bnusNo"]

count = 0
sec_con = 0
for i in my_lotto:
    for j in cor_num:
        if i == j:
            count += 1
        elif i == bonus:
            sec_con = 1

print(my_lotto)
print(cor_num)

if count == 6:
    print("1등")
elif count == 5 and sec_con == 1:
    print("2등")
elif count == 5:
    print("3등")
elif count == 4:
    print("4등")
elif count == 3:
    print("5등")
else:
    print("다음 기회에")



# set을 사용한 로또 확인
set_cha = set(my_lotto)
set_ans = set(cor_num)

def check():
    chk = len(set_cha & set_ans)
    if chk == 6:
        print("1등입니다")
    elif chk == 5:
        print("3등입니다")
    elif chk == 4:
        print("4등입니다")
    elif chk == 3:
        print("5등입니다")
    else:
        print("꽝입니다")