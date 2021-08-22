import re

# 예시 차량번호 4자리 가정
# ca?e
# care, cafe, case, cave, ...

# .: 하나의 문자를 의미, 예) (ca.e) care, cafe, case 
# ^: 문자열의 시작, 예) (^de) desk, destination 
# $: 문자열의 끝, 예) (se$) case, base 
p = re.compile("ca.e")


def print_match(m):
    if m:
        print("m.group(): ", m.group()) # 일치하는 문자열 출력
        print("m.string: ", m.string) # 입력받은 문자열
        print("m.start(): ", m.start()) # 일치하는 문자열의 시작 index
        print("m.end(): ", m.end()) # 일치하는 문자열의 끝 index
        print("m.span(): ", m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음")


m = p.match("acareless") # 주어진 문자열의 처음부터 일치하는지 확인 따라서 매칭이 됨
print_match(m)

s = p.search("good care") # 주어진 문자열 중에 일치하는게 있는지 확인
print_match(s)

f = p.findall("careless, cafe") # findall: 일치하는 모든 것을 리스트 형태로 반환
print(f)

# print(m.group()) # 매치되지 않으면 에러가 발생


