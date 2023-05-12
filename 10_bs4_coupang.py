import requests
import re
from bs4 import BeautifulSoup

headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

for i in range(1,6):
    print('페이지 {}'.format(i))
    url = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=9&backgroundColor='.format(i)
    res=requests.get(url,headers=headers)
    res.raise_for_status() # 여기서부터 동작 안함
    soup = BeautifulSoup(res.text,'lxml')

    items = soup.find_all('li',attrs={'class':re.compile('^search-product')}) # search-product로 시작하는 뭐든 li element 추출
    print(items[0].find('div',attrs={'class':'name'}).get_text())

    for item in items :
        # 광고 제품 제거
        ad_badge = item.find('span',attrs={'calss':'ad-badge-text'})
        if ad_badge:
            continue

        name = item.find('div',attrs={'class':'name'}).get_text()
        #apple 제품 제외
        if 'Apple' in name:
            continue

        price = item.find('strong',attrs={'class':'price-value'}).get_text()
        
        # 리뷰 100개 이상, 평점 4.5이상 되는 것만 조회
        rate = item.find('em',attrs={'class':'rating'})
        if rate :
            rate = rate.get_text()
        else:
            rate='평점 없음'
            continue

        rate_cnt = item.find('span', attrs={'class':'rating-total-count'})
        if rate_cnt :
            rate_cnt = rate_cnt.get_text()
            rate_cnt = rate_cnt[1:-1]
        else:
            rate_cnt='평점 수 없음'
            continue

        link = item.find('a',attrs={'class':'search-product-link'})['href']
        
        if float(rate) >= 4.5 and int(rate_cnt) >= 100:
            print(f'제품명:{name}')
            print(f'가격 : {price}')
            print(f'평점:{rate}점 ({rate_cnt}개)')
            print('바로가기 : {}'.format('https://www.coupang.com'+link))
            print('-'*100)



            



