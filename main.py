from selenium import webdriver
from bs4 import BeautifulSoup

path = "..\chromedriver\chromedriver.exe"


driver = webdriver.Chrome(path)
driver.get("https://l0o02.github.io/2018/06/12/python-crawling-selenium-1/")
    
    
req = driver.page_source
soup = BeautifulSoup(req, "lxml")
find_div = soup.find("div")
find_span = find_div.find("span").text

print(find_span)