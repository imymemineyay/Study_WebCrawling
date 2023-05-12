import requests
from bs4 import BeautifulSoup

url = 'https://search.daum.net/search?w=tot&q=2022%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')
imgs = soup.find('img', attrs={'class':'thumb_img'}) # 동적 html 인듯 





for year in range(2015,2020):
    url = 'https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'.format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,'lxml')
    imgs = soup.find('img', attrs={'class':'thumb_img'}) # 동적 html 인듯 

    for idx,img in enumerate(imgs): 
        print(img['src'])
        img_url = img['src']
        if img_url.startswith('//'): # //로 시작한다면
            img_url = 'https:' + img_url
        print(soup)
        img_res = requests.get(img_url)
        img_res.raise_for_status()

        with open('movie_{}_{}.jpg'.format(year, idx+1),'wb') as f :# 텍스트 아니라 binary b 붙이기
            f.write(img_res.content)
        
        if idx >= 4:
            break