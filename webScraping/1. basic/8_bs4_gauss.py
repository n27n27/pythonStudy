import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

def printLn(str):    
    print("="*60)
    print(str)   

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# printLn(title)
# printLn("https://comic.naver.com" + link)

# 웹툰 제목 + 링크가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     printLn(title)
#     print(link)

# 평점 구하기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})

for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    printLn(rate)
    total_rates += float(rate)
print("전체 점수: ", total_rates)
print("전체 점수: %.1f"%total_rates)
print("평균 점수: ", total_rates / len(cartoons))