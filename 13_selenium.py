from selenium.webdriver.common.by import By
from selenium import webdriver # 브라우저를 컨트롤하는 라이브러리
from selenium.webdriver.common.keys import Keys # 글자 입력 모듈
import time


driver = webdriver.Chrome('/Users/thisismine/Downloads/Install/chromedriver')
driver.get('http://naver.com')

elem = driver.find_element_by_class_name('link_login')
elem
elem.click()
driver.back() #이전 페이지 이동
driver.forward() # 앞 페이지 이동
driver.refresh() # 새로 고침
elem = driver.find_element_by_id('query')
elem.send_keys('나도 코딩')
elem.send_keys(Keys.ENTER) #keys 모듈 임포트한 이유
elem = driver.find_elements_by_tag_name('a') # a 태그에 해당하는 모든 값을 가져올 때 s 붙이기
elem

for e in elem:
    e.get_attribute('href')

driver.get('http://daum.net')
elem = driver.find_element_by_name('q')
elem.send_keys('나도 코딩')
elem.send_keys(Keys.ENTER)
driver.back()

# xpath 를 활용하여 버튼 누르기 
elem = driver.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[3]')
elem.click()
driver.quit() #모든 브라우저 닫기
driver.close() # 현재 열려있는 탭만 닫기 


# 1. go to naver
browser = webdriver.Chrome('/Users/thisismine/Downloads/Install/chromedriver')
browser.get('http://naver.com')

# 2. click the login button
elem = browser.find_element_by_class_name('link_login')
elem.click()

# 3. input the id
browser.find_element_by_id('id').send_keys('maninthemirror')
# 임의의 아이디 입력

# 4. input the pw
browser.find_element_by_id('pw').send_keys('password') # 임의의 비밀번호 입력


# 5. click the login button
browser.find_element_by_xpath('//*[@id="log.login"]').click()

time.sleep(3)

# retry
browser.find_element_by_id('id').clear() # 기존 입력 내용 지우기
browser.find_element_by_id('id').send_keys('heyyall') 

# 6.html 정보 출력
print(browser.page_source)

# 7. close the browser
browser.quit()