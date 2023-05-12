import requests
from bs4 import BeautifulSoup


url = 'https://play.google.com/store/movies'
headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
           'Accept-Language':'ko-KR,ko'} # 한글언어로된 페이지 요청
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,'lxml')

movies = soup.find_all('div',attrs={'class':'ULeU3b neq64b'})
print(len(movies))

with open('moovie.html','w',encoding='utf8') as f:
   # f.write(res.text)
    f.write(soup.prettify()) # 원하는 정보가 뜨지 않을 때 확인할 수 있는 방법
    # 추출 결과가 뜨지 않는 이유는 접속하는 header정보를 통해서 구글 무비에서는 서로 다른 페이지를 리턴해줌
    # 구글링을 통해서 접속했을 때는 kr로 뜨고 request를 통해서 접속했을 때는 아마도 미국에서 접속한 것을 default로 맞춰서 정보를 주는 것 같음
    # 한글 페이지로 잘받아와야 하기 때문에 user agent 사용할 것 

for movie in movies:
    title = movie.find('div',attrs={'class':'Epkrse'}).get_text()
    print(title)

