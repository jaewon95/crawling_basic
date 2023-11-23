import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

keyword = input("검색어를 입력하세요 : ")
base_url = f'https://search.naver.com/search.naver?query={keyword}&nso=&where=blog&sm=tab_opt'
url = base_url
print(url)

req = requests.get(url, headers=headers) # 1. get 요청을 하겠당

soup = BeautifulSoup(req.text, "html.parser") # (html 코드, 번역기~)

titleItem = soup.select(".title_link")

newArr = {}
for index,item in enumerate(titleItem) :
    print(f"{index}. {item.text}")
    
    




