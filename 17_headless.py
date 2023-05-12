## 동적 웹페이지 작동시키는 법 (현재 구글 영화에 해당되지 않음 주의)
from selenium import webdriver
options = webdriver.ChromeOptions() # 백그라운드에서 스크래핑 시작되는 것 
options.headless = True
options.add_argument('window-size=1920X1080')


driver = webdriver.Chrome('/Users/thisismine/Downloads/Install/chromedriver',options=options)
driver.maximize_window()

url = 'https://play.google.com/store/movies'
driver.get(url)

#모니터 높이인 1080 위치로 스크롤 내리기
driver.execute_script('window.scrollTo(0,1080)') #1920*1080

#화면 가장 아래로 스크롤 내리기
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

import time
interval=2

#현재 문서 높이를 가져와서 저장
prev_height = driver.execute_script('return document.body.scrollHeight')

#반복 수행
while True:
    #스크롤을 가장 아래로 내림
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    #페이지 로딩 대기
    time.sleep(interval)
    # 현재 문서 높이를 가져와서 저장
    curr_height = driver.execute_script('return document.body.scrollHeight')
    if curr_height == prev_height :
        break
    prev_height = curr_height
print('스크롤 완료')
driver.get_screenshot_as_file('google_movie.png') # 백그라운드에서 동작을 하는지 확인하는 것

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(driver.page_source,'lxml')

movies = soup.find_all('div',attrs={'class':['ULeU3b neq64b','Vpfmgd']}) # 두개 이상일 시 사용
print(len(movies))

for movie in movies:
    title = movie.find('div',attrs={'class':'Epkrse'}).get_text()
    
    # 할인 전 가격
    original_price = movie.find('span',attrs = {'class':'SUZt4c djCuy'})
    if original_price:
        original_price = original_price.get_text()
    else:
        print(title, " <할인되지 않은 영화 제외")
        continue

    # 할인된 가격
    price = movie.find('span',attrs = {'class':'VFPpfd ZdBevf i5DZme'}).get_text()
    
    # link
    link = movie.find('a',attrs = {'class':'JC71ub'})['href']
    
    print(f'제목 : {title}')
    print(f'할인 전 금액 : {original_price}')
    print(f'할인 후 금액 : {price}')
    print('링크 : ', 'https://play.google.com' + link)
    print('-'*200)

driver.quit()
          



