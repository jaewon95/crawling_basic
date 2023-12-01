from selenium import webdriver
from selenium.webdriver.chrome.service import Service #webdriver-manager set
from webdriver_manager.chrome import ChromeDriverManager #webdriver-manager set
import time

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

driver.get("https://naver.com")
time.sleep(3)