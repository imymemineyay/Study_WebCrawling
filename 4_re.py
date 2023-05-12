##### 정규표현식 공부하기 #####

# 1. p = re.compile('원하는 형태')
# 2. m = p.match('비교할 문자열') : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search('비교할 문자열') : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall('비교할 문자열') : 일치하는 모든 것을 "리스트" 형태로 반환

# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case(o) | caffe(x) 
# ^ (^de) : 문자열의 시작 > desk, destination (o) | fade(x)
# $ (se$) : 문자열의 끝 > case, base (o) | face(x)


import re 

p = re.compile("ca.e")
# p = pattern, compile = 어떤 정규식을 컴파일할지 정해줌, . = 하나의 문자
# ^ = 문자열의 시작, $ = 문자열의 끝

m = p.match("case") # p랑 매칭되는지 확인 
print(m.group()) #매칭되면 내용 출력, 매칭안되면 에러발생


def print_match(m):
    if m:
        print(m.group()) # 일치하는 문자열 반환
        print(m.string) # 입력받은 문자 반환
        print(m.start()) # 일치하는 문자열의 시작 index
        print(m.end()) # 일치하는 문자열의 끝 index
        print(m.span()) # 일치하는 문자열의 시작 / 끝 index 
        
    else:
        print("it doesn't match the rule")

m = p.match("case")
print_match(m)

n = p.match("good care")
print_match(n)

k = p.match('careless') # match : 주어진 문자열의 처음부터 일치하는지 확인 
print_match(k) # 뒤에 다른 값이 나와도 상관 없음

m = p.search('good care') # search : 주어진 문자열 중에 일치하는게 있는지 확인
print_match(m)

n = p.search('careless')
print_match(n)

lst = p.findall('careless') # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)

lst = p.findall('careless care cafe good care') # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)



