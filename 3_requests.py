## request 를 통해 스크핑하기
### 1. 정상적으로 동작하는 지 확인, 정상 동작할 경우 파일을 만들어보기 

import requests 
res = requests.get('http://naver.com') # 원하는 url정보 넘겨주면 됨
print("응답코드 : ", res.status_code)  # 200 : 접근 가능, 403 : 접근 권한 없음 (정보 잘 받아왔는지 확인용)

if res.status_code == requests.codes.ok:
    print('정상')
else:
    print('비정상 [에러코드, {0}]'.format(res.status_code))


res = requests.get('http://naver.com') 
res.raise_for_status() # 올바로 url정보를 가져오면 정상, 아니면 에러 발생 후 끝
print('웹 스크래핑을 진행합니다.')

print(len(res.text)) # 가지고 온 html 글자 개수

res = requests.get('http://google.com')
print(len(res.text))

with open('mygoogle.html','w',encoding='utf8') as f:
    f.write(res.text) # 정상적으로 받은 정보를 가지고 파일을 만듦
