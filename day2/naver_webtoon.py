import requests
import bs4


url = "https://m.comic.naver.com/webtoon/weekday.nhn?week=tue"
response = requests.get(url).text
doc = bs4.BeautifulSoup(response, 'html.parser')

names = []
imgs = []

names = doc.select_one(".toon_name")
# for i in doc.select(".toon_name"):
#     names.append(i.text)

for i in doc.select(".im_br"):
    imgs.append(doc.select_one("img")["src"])

print(names)

# f = open('./a.txt', 'a+')
# for i in range(len(names)):
#     print("제목 : " + names[i] + ", 이미지 : " + imgs[i])
#     f.write("제목 : " + names[i] + ", 이미지 : " + imgs[i] + "\n")

# f.close()