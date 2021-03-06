from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

print('-------------------------------------')
print('제작자 : https://blog.naver.com/cflab')
print('-------------------------------------')

def openDriver():
    url = 'https://www.melon.com/chart/index.htm'
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get(url)
    time.sleep(1)
    return driver

def searchMelon(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all(class_='wrap_song_info')

    mList = []
    rank = 1

    for i in tags:
        try:
            title = i.find(class_='ellipsis rank01').a.text
            singer = i.find(class_='ellipsis rank02').a.text
            print(f'순위 : {rank}\n가수 : {singer} \n제목 : {title}\n')
            mList.append([rank, singer, title])
            rank += 1
        except:
            pass
    return mList

def saveToFile(filename, mList):
    with open(filename, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(mList)

driver = openDriver()
mList = searchMelon(driver)
saveToFile('melon.csv', mList)