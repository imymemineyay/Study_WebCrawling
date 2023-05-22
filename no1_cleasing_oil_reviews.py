#### 올리브영의 넘버즈인 제품 리뷰 웹크롤링


#### 라이브러리 불러오기 ####
import time
from selenium.webdriver.common.by import By
from selenium import webdriver # 브라우저를 컨트롤하는 라이브러리
from selenium.webdriver.common.keys import Keys # 글자 입력 모듈
from selenium.webdriver.common.by import By # 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
driver = webdriver.Chrome('/Users/thisismine/Downloads/Install/chromedriver')

#해당 url로 이동
url = "https://www.oliveyoung.co.kr/store/planshop/getPlanShopDetail.do?dispCatNo=500000103040001&utm_source=google&utm_medium=powerlink&utm_campaign=onpro_emnet_app-first-deal_0103_1231&utm_content=pc_main&gclid=CjwKCAjw36GjBhAkEiwAKwIWySpG0OFM29dy9gMrJHtXArvSS-zQw6J5Dvx1qyDFRGoApUL3VsdqxxoCqqsQAvD_BwE" 
driver.get(url)
time.sleep(4)

# 넘버즈인 검색 
driver.find_element_by_xpath('//*[@id="w_search_box"]').click()
driver.find_element_by_class_name('inp_placeholder').send_keys('넘버즈인')
driver.find_element_by_xpath('//*[@id="searchSubmit"]').click()
time.sleep(3)

# 제품 클릭
driver.find_element_by_xpath('//*[@id="w_cate_prd_list"]/li[1]/div').click()
time.sleep(4)

# 리뷰 클릭
driver.find_element_by_xpath('//*[@id="reviewInfo"]').click()
time.sleep(4)

# 광고 리뷰 제거
driver.find_element_by_xpath('//*[@id="searchType_3"]').click()
time.sleep(4)

# '>>' 대 페이지 개수 구하기
cnt = 1

while True:
    try : 
        driver.find_element_by_css_selector("#gdasContentsArea > div > div.pageing > a.next").send_keys(Keys.ENTER)
        time.sleep(2) # time.sleep 안하면 안넘어가는 경우 있음 그래서 대기시간 부여해주는 게 좋음
        cnt += 1
    except:
        break

# 첫 페이지로 이동
while True:
    try : 
        driver.find_element_by_css_selector("#gdasContentsArea > div > div.pageing > a.prev").send_keys(Keys.ENTER)
        time.sleep(2)
    except:
        break



# 한 페이지 내에 필요한 내용 담기(인덱스, 별점, 날짜, 리뷰) 수집에 필요한 함수 생성
def collector():
    for k in range(1,11):
        global review_cnt # local variable 'review_cnt' referenced before assignment 에러 해결
        idx.append(review_cnt) # 인덱스 수 입력

        s = '#gdasList > li:nth-child({}) > div.review_cont > div.score_area > span.review_point > span'.format(k) # 별점 css
        d = '#gdasList > li:nth-child({}) > div.review_cont > div.score_area > span.date'.format(k) # 날짜 css
        r = '#gdasList > li:nth-child({}) > div.review_cont > div.txt_inner'.format(k) # 리뷰 css
        
        star = driver.find_element_by_css_selector(s).text # 별점 문자 추출
        stars.append(star)
        time.sleep(2)
        
        day = driver.find_element_by_css_selector(d).text # 날짜 문자 추출
        date.append(day)
        time.sleep(2)

        review = driver.find_element_by_css_selector(r).text # 리뷰 문자 추출
        reviews.append(review)
        time.sleep(2)

        review_cnt += 1


# 10 페이지 컬렉터 
def ten_pages_collector():
    for j in range(1,11): # 한 페이지 수만큼 반복
        if j == 1:
            driver.find_element_by_css_selector('#gdasContentsArea > div > div.pageing > strong').click() # 첫 페이지
            time.sleep(2)
            collector()
        else:
            a ='#gdasContentsArea > div > div.pageing > a:nth-child({})'.format(j) # 다음 페이지
            driver.find_element_by_css_selector(a).click()
            time.sleep(2)
            collector()

# 11페이지 이상부터의 컬렉터
def num2_ten_pages_collector():
    for j in range(2,12): # 한 페이지 수만큼 반복
        if j == 2:
            driver.find_element_by_css_selector('#gdasContentsArea > div > div.pageing > strong').click() # 첫 페이지
            time.sleep(2)
            collector()
        else:
            a ='#gdasContentsArea > div > div.pageing > a:nth-child({})'.format(j) # 다음 페이지
            driver.find_element_by_css_selector(a).click()
            time.sleep(2)
            collector()

# 페이지 별 수집 
idx = [] # 인덱스 리스트
stars = [] # 별점 리스트
date = [] # 날짜 리스트
reviews = [] # 후기 리스트
review_cnt = 1 # 인덱스

for l in range(cnt): # 큰 페이지 수 만큼 반복
    if l == 0 :
        ten_pages_collector()
    else:
        driver.find_element_by_css_selector("#gdasContentsArea > div > div.pageing > a.next").click()
        time.sleep(4) 
        num2_ten_pages_collector()
 



    


#gdasContentsArea > div > div.pageing > strong
#gdasContentsArea > div > div.pageing > a:nth-child(10)
#gdasContentsArea > div > div.pageing > a:nth-child(11)

data = {'IDX' : idx,
        'STARS' : stars,
        'DATE' : date,
        'REVIEW' : reviews
        }
no1_cleasing_oil_reviews = pd.DataFrame(data, columns =['IDX','STARS','DATE','REVIEW'])

no1_cleasing_oil_reviews.to_csv('/Users/thisismine/Downloads/My_Area_For_Programming/Benow/no1_cleasing_oil_reviews.csv', encoding='utf-8-sig')
