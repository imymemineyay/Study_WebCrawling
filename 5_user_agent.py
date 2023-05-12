#### user agent ####
# user agent string 에 접속하면 내가 사용하고 있는 브라우저의 user agent 알 수 있음
# 접속하는 브라우저에 따라 user agent 가 다르게 뜸
# 특정 페이지는 접속 권한?을 막았었는데 user agent 를 주면 접근 권한이 부여됨
# user agent 라는 것
# : 브라우저가 웹사이트에 연결하면 http 헤더에 user agent 필드가 포함된다. 이 필드의 내용은 브라우저 마다 다르다.
# 각 브라우저는 고유한 user agent를 가지고 있어서 "안녕하세요. 저는 모질라 5.0블라블라예여!"라고 웹 서버에 말한다.
# 이 정보를 이용해서 웹 서버는 서로 다른 웹페이지를 보여주는 것이다. 즉, 최신 페이지는 최신 브라우저로 혹은 '브라우저를 업뎃하세요'등등



import requests 
url='http://nadocoding.tistory.com/'
headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers) # 원하는 url정보 넘겨주면 됨
res.raise_for_status()
with open('nadocoding.html','w',encoding='utf8') as f:
    f.write(res.text) # 정상적으로 받은 정보를 가지고 파일을 만듦


