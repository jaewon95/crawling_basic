# 크롤링 연습을 할 때 처음에 해당 페이지가 request와 BeautifulSoup 만으로 가능한가?
# 페이지 소스 보기 -> js로 동적으로 뿌려주는건 위 2개로만 하는건 불가능.
# 동적이다? 셀레니움 사용

import requests
from bs4 import BeautifulSoup
 
# header 준비
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

url = 'https://www.melon.com/chart/index.htm'

req = requests.get(url, headers=headers)
html = req.text

soup = BeautifulSoup(html, "html.parser")


# 1단계 방법 ->
# lst50 = soup.select(".lst50") # .select -> 전부가져옴
# lst100 = soup.select(".lst100") # .select -> 전부가져옴
# lstPlus = lst50+lst100

# 2단계 방법 ->
# lstPlus = soup.select('.lst50, .lst100')

# 3단계 방법 ->
lstPlus = soup.find_all(class_=['lst50', 'lst100'])






# .isdigit() -> 문자는 False, 숫자는 True 
# ''.join -> ['a', 'b', 'c'] 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환

def getSongNum(link):
    songData = []
    for i in link :
        if i.isdigit():
            songData.append(i)
    resSongData = ''.join(songData)
    return resSongData
#


for k,v in enumerate(lstPlus) :
    # ellipsis rank01 빈간은 . 으로 이어주기
    title = v.select_one('.ellipsis.rank01 a') # 하단 요소 전체에서 찾음
    singer = v.select_one('.ellipsis.rank02 > a') # css 처럼 이렇게도 가능함. 바로 자식 요소 찾음. 정확한 태그 구조를 넣으면 됨
    singerLink = getSongNum(singer['href'])
    
    print(f' {k+1} >>>')
    # print(title) # 태그 통째로 가져오기
    
    print('제목:',title.text.strip(),' 가수:', singer.text.strip()) # text 가져오기 
    print('가수링크 :', 'https://www.melon.com/artist/timeline.htm?artistId='+singerLink)
    print()





