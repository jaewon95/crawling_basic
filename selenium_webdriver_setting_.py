# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service #webdriver-manager set
# from webdriver_manager.chrome import ChromeDriverManager #webdriver-manager set
# import time

# service = Service(ChromeDriverManager().install())

# driver = webdriver.Chrome(service=service)

# driver.get("https://naver.com")
# time.sleep(3)



# 4.6 이후부터는 간단하게 웹 드라이버 자동화 가능
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://naver.com")
time.sleep(3)
