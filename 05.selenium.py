from selenium import webdriver
import time

url ="https://naver.com"

driver = webdriver.Chrome()

driver.get(url)
time.sleep(3)