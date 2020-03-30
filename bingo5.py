from selenium import webdriver
from bs4 import BeautifulSoup
import time

path = "..\chromedriver\chromedriver.exe"
URL = "https://www.mizuhobank.co.jp/retail/takarakuji/bingo/backnumber/index.html"

driver = webdriver.Chrome(path)

def get_html():
    driver.get(URL)
    request = driver.page_source
    soup = BeautifulSoup(request, "lxml")
    return soup

def max_page():
    soup = get_html()
    find_title = soup.find("table", class_="js-backnumber-b")
    find_rounds = find_title.find_all("a")
    page_num = []
    for number in find_rounds:
        page_num.append(number.text)
    if "" in page_num:
        for erase_blank in page_num:
            if "" in page_num:
                del page_num[page_num.index("")]
    last_page = page_num[-1]
    last_page = last_page.replace("第","").replace("回","").split("〜")[-1]
    return last_page

def extract_raffle_data(raffle_rounds):
    date = raffle_rounds.find("td", class_="js-lottery-date").text
    nth_round = raffle_rounds.find("th", class_="bgf7f7f7").text
    num = raffle_rounds.find_all("td")
    num_text = [] 
    for n in num:
        num_text.append(n.text)
    num_text = num_text[1:]

    return {"date":date, "round":nth_round, "num01":num_text[0], "num02":num_text[1], "num03":num_text[2], "num04":num_text[3], "num05":num_text[4], "num06":num_text[5], "num07":num_text[6], "num08":num_text[7]}

def get_raffle_page():
    URL = f"https://www.mizuhobank.co.jp/retail/takarakuji/bingo/backnumber/detail.html?fromto=1_{max_page()}&type=bingo5"
    driver.get(URL)
    time.sleep(5)
    request = driver.page_source
    soup = BeautifulSoup(request, "lxml")
    find_raffle_num = soup.find("div", class_="spTableScroll js-lottery-backnumber-list sp-none")
    find_raffle_rounds = find_raffle_num.find_all("tr", class_="js-lottery-backnumber-temp-pc")

    results = []
    for rounds in find_raffle_rounds:
        result = extract_raffle_data(rounds)
        results.append(result)
    driver.close()
    return results