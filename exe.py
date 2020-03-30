from selenium import webdriver
from bs4 import BeautifulSoup

path = "..\chromedriver\chromedriver.exe"


driver = webdriver.Chrome(path)
driver.get("https://www.naver.com/")
    

req = driver.page_source
soup = BeautifulSoup(req, "lxml")
find_title = soup.find("title").text

print(find_title)