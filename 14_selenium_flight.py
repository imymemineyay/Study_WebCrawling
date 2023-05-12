import time
import datetime as dt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 글자 입력 모듈
from selenium.webdriver.common.by import By # 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome('/Users/thisismine/Downloads/Install/chromedriver')
driver.maximize_window() # 창 최대화

url = 'https://m-flight.naver.com/'
driver.get(url) # move to url

# close the pop up page 
driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div/div[2]/button[1]').click()

# click the day to go button
driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()

# wait 
time.sleep(5)

# select the 27th  and 30th of the current month 
dates = driver.find_elements_by_css_selector('.sc-evZas.dDVwEk.num')
dates[26].click()
dates = driver.find_elements_by_css_selector('.sc-evZas.dDVwEk.num')
dates[29].click()

## select the 27th and 30th of the next month

# Find the parent element containing the month and year information
month_year_element = driver.find_elements_by_css_selector('.sc-kDDrLX.ctbFvd.month')[1]

# Find the day elements within the parent element
day_elements = month_year_element.find_elements_by_css_selector('.sc-evZas.dDVwEk.num')

# Click on the element corresponding to the 27th day
day_elements[26].click()

# Find the day elements within the parent element
day_elements = month_year_element.find_elements_by_css_selector('.sc-evZas.dDVwEk.num')

# Click on the element corresponding to the 27th day
day_elements[29].click()


## 이번달과 다음달 27일 30일 선택하기
# 이번달 27일 선택
dates = driver.find_elements_by_css_selector('.sc-evZas.dDVwEk.num')
dates[26].click()

# Find the parent element containing the month and year information
month_year_element = driver.find_elements_by_css_selector('.sc-kDDrLX.ctbFvd.month')[1]

# Find the day elements within the parent element
day_elements = month_year_element.find_elements_by_css_selector('.sc-evZas.dDVwEk.num')

# Click on the element corresponding to the 27th day
day_elements[29].click()

# click the arrival location "도쿄"
driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]').click()
driver.find_element_by_class_name('autocomplete_input__1vVkF').send_keys('도쿄')
a = driver.find_elements_by_css_selector('.autocomplete_search_item__2WRSw')[0].click()

# click the search button
driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/button').click()

try:
    # 로딩할 때 시간이 걸릴 시 해당 코드 작성
    elem = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located)
    # print the first result
    elem = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[6]/div/div[3]/div[1]')
    print(elem.text)
finally:
    driver.quit()

