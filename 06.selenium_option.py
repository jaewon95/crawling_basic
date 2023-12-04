from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# 0.selenum_옵션지정할때 사용
options = Options()

# options.add_argument() : 각종 옵션 사용 가능.


# 1. 창이 자동으로 꺼지지않는 옵션
options.add_experimental_option("detach",True)

# 2. 화면 크기 지정 옵션
# options.add_argument("window-size=500,500")
# options.add_argument("--start-maximized") ... 등등

# 2-1. 헤드리스 모드 (화면없이 사용)
# options.add_argument("--headless")
# options.add_argument("--disable-gpu") # --headless 추가했는데 안될때 사용

# 2-2. 시크릿모드
options.add_argument("incognito")

# 2-3. 크롬 상단의 자동화메시지 없애기
options.add_experimental_option("excludeSwitches", ["enable-automation"])

# 2-4. html 만 보고 싶을때 .page_source 이거 사용중일때 같이 쓰면 좋다.
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 3. user_agent 유저에이전트 지정
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
options.add_argument(f"user-agent={user_agent}")

# 4. 유저 데이터 옵션을 추가하기 (방문기록 만들기)
user_data = r"C:\Users\admin\OneDrive\바탕 화면\myproject_tprtus1\test" # 경로\(저장할 파일명 작성 : test 라고 이름지음)
options.add_argument(f'user-data-dir={user_data}') # 사이트에 접속 후 닫기를 누르기 전까지 방문기록을 생성해준다.
#                                                     # 어디에? test 디렉토리에. 디렉토리는 미리 만들지 않아도 알아서 생성해줌

 
# 5. 크롬 드라이버
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options) # service , options 추가

url = 'https://naver.com'

driver.get(url)

print(driver.page_source[:1000]) # 페이지 소스 가져오기
# driver.quit() # 페이지 끄기



