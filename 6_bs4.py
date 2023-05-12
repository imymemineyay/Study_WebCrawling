# beautifulsoup : 스크랩핑하기 위해서 사용하는 패키지
# lxml : 구문을 분석하는 파서

import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/index'
res = requests.get(url)
res.raise_for_status() # 문제있는지 확인 

soup = BeautifulSoup(res.text,"lxml") # 가져온 html 문서를 lxml 파서를 통해서 bs객체로 만든 것
                                      # bs이 정보를 다 가지고 있음

print(soup.title) # soup 객체를 통해서 다른 html 정보를 가져올 수 있는 것
print(soup.title.get_text()) # 글자만 추출 가능

print(soup.a) # soup 객체에서 처음 발견되는 값 추출
print(soup.a.attrs) # a element의 속성 정보 추출
print(soup.a['href']) # a element의 속성의 특정 정보 추출

print(soup.find('span',attrs={'class':'blind'})) # 해당하는 첫 번째 element 를 추출, 조건 부여 가능 attrs = {"class":"Nbtn--"} 예시 

#### soup 으로 했을 때 title 빼곤 결과값이 None으로 출력됨 
# 이것은 동적콘텐츠 로딩이나 태그가 중첩되어서 그럴 가능성이 있음 이럴 땐 selenium을 이용해야함

##### 결과값이 안나와도 그냥 따라서 쳐보겠움...

rank1 = soup.find('li',attrs={'class':'rank01'})
print(rank1.a.get_text())
rank2 = rank1.next_sibling.next_sibling # 형제 element 추출
rank3 = rank2.next_sibling.next_sibling # 두번 사용하는 것은 형제 요소들 사이에 다른 요소가 추가되어서임
print(rank3.a.get_text())
rank2 = rank3.previous_sibling.previous_sibling # 이전 형제 element 추출

print(rank1.parent) # 부모 요소 추출

rank2 = rank1.find_next_sibling('li') # li인 다음 형제 요소 추출
print(rank2.a.get_text()) 
rank2 = rank3.find_previous_sibling('li') 

rank1.find_next_siblings('li') # rank1 기준으로 형제 모두 추출

webtoon = soup.find('a', text='독립일기-11화 밥공기 딜레마') # text에 해당하는 a 태그 추출


