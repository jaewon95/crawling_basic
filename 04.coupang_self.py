import requests
import random
from bs4 import BeautifulSoup

b_url = "https://www.coupang.com/np/search?component=&q="

# 임의로 생성한 랜덤값. 차단 막기위함.
random_numbers = random.sample(range(101, 131), 3)
random_data = ''.join(map(str, random_numbers))

headerNum = int(random_data) + 21


headers = {
    "User-Agent" : f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
cookie = {'asd125as' : str(headerNum) }

keyword = input("검색어를 입력하세요 : ")

search_url = b_url + keyword

#쿠팡은 cookie를 요구한다

 

# timeout : 지연시간 설정
req = requests.get(search_url,timeout=5, headers=headers, cookies=cookie)

site = req.text

soup = BeautifulSoup(site, "html.parser")

findNumber = soup.select('.search-product-link:not(.ad-badge)') # .ad-badge 가 있는건 빼고 가져오고 싶다. :not()
rankingProduct = []
number = 0
for i in findNumber :
    if i.find(class_='number') != None :
        print(' >>>> 순위상품 <<<<')
        print('순위 : ',i.find(class_='number').text)
        print('상품명 : ',i.find(class_='name').text.strip())
        print('가격 : ', i.find(class_='price-area').find(class_='price-value').text) # 자식요소 찾기
        
        rankingProduct.append({
            'code' : keyword,
            'number' : i.find(class_='number').text,
            'item' : {
                '순위' : i.find(class_='number').text,
                '상품명' : i.find(class_='name').text.strip(),
                '가격' : i.find(class_='price-area').find(class_='price-value').text
            }
        })    
    else :
        print('순위 : ',i.find(class_='number'))    
        print('상품명 : ',i.find(class_='name').text.strip())
        print('가격 : ', i.find(class_='price-area').find(class_='price-value').text) # 자식요소 찾기
        print('')
#
    
print(rankingProduct)