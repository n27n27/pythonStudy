import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

def printLn(str):
    print("\n")
    print("="*60)
    print(str.a.get_text())

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
print(soup.a) # soup 객체에서 처음 발견되는 a element
print(soup.a.attrs) # a element의 속성 정보
print(soup.a["href"]) # a element의 href속성 정보

# class="Nbtn_upload" 인 a element를 찾아줘
print(soup.find("a", attrs={"class":"Nbtn_upload"})) 

# class="Nbtn_upload" 를 찾아줘
print(soup.find(attrs={"class":"Nbtn_upload"})) 

print(soup.find("li", attrs={"class":"rank01"}))
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.next_sibling.next_sibling)
print("="*30)
rank2 = rank1.next_sibling.next_sibling
print(rank2) 
print("="*30)
rank3 = rank2.next_sibling.next_sibling
print(rank3)
print("="*30)
print(rank3.a.get_text())

rank2 = rank3.previous_sibling.previous_sibling
printLn(rank2)
rank2 = rank1.find_next_sibling("li")
printLn(rank2)

