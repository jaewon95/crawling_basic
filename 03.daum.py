import requests
from bs4 import BeautifulSoup

# header 준비
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

url = 'https://news.daum.net/'


req = requests.get(url, headers=headers)
print(req.text)
siteText = req.text

soup = BeautifulSoup(siteText, "html.parser")


soupIssue = soup.select('.link_txt')
soupC = soup.select('.logo_cp > img')

for idx,(sis, soc) in enumerate(zip(soupIssue,soupC)) :
    print()
    print('>>>' ,idx)
    print('제목 : ',sis.text.strip())
    print('회사 : ',soc['alt'])
    

    
