'''
사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com
규칙1: http:// 부분은 제외 => naver.com
규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성한다.

예) 생성된 비밀번호: nav51!
'''

# 내가 쓴 답
url = "http://naver.com"
rule1 = url[7:]
find = rule1.index(".")
rule1 = rule1[0:find]
password = rule1[0:3] + str(len(rule1)) + str(rule1.count("e")) + "!"
print("생성된 비밀번호= {}".format(password))

# 정답
url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙1
my_str = my_str[:my_str.index(".")] # 규칙2  => my_str[0:5] -> 0 ~ 5 직전까지
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!" # 규칙 3
print("{0}의 비밀번호는 {1} 입니다.".format(url, password))
