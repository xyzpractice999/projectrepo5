from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
 
path="C:/Users/suman/Downloads/chromedriver-win64_L/chromedriver-win64/chromedriver.exe"
obj=Service(path)
driver=webdriver.Chrome(service=obj)
time.sleep(10)
