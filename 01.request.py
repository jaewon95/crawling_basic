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

# * 빈공간은 . 으로 바꿔줘야한다.

# titleItem = soup.select(".title_link") 1개만 가져올때는 이렇게.
titleItem = soup.select(".title_link") # 2개 이상 가져올때는 이렇게

newArr = {}
for index,item in enumerate(titleItem) :
    # print(item) # 전체요소
    
    # item.get('요소') key error 감지하려면 이렇게 하면 된다. 
    # 만약 요소가 없다면 None을 반환함
    
    print(item['href']) # 요소 선택하기
    print(f"{index}. {item.text}")
#

# 만약에 요소를 선택해서 가지고 왔는데 '공백'이 존재하면 . 으로 연결해줘야한다.
# 스크롤해서의 내용을 가져오려면 BeautifulSoup 이 아니라 selenium 사용해야함



# 3개는 모두 같은 코드이다.
print(soup.h1)
h1 = soup.find('h1')
h1 = soup.select_one('h1')

# find
h2 = soup.find(class_='클래스명') # class는 _ 를 사용함
h2 = soup.find(id='클래스명') # id는 그대로 진행

nav = soup.find(class_="nav", string='증권') # 클래스가 nav , string 증권
nav = soup.find('h1', string='증권') # 클래스가 nav , string 증권


