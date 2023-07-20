python = "Python is Amazing"
print(python.lower()) # 모든 문자를 소문자로 출력
print(python.upper()) # 모든 문자를 대문자로 출력
print(python[0].isupper()) # 첫번째의 문자가 대문자인지 확인 하여 True, False 출력
print(len(python)) # 파이썬 전체 길이를 반환
print(python.replace("Python", "Java")) # 문장 안에 있는 문자를 다른 문자로 변경

index = python.index("n") # n이라는 글자가 몇 번째 위치에 있는지
print(index)
index = python.index("n", index + 1) # 첫번째 n을 찾은 위치부터 뒤에 있는 n을 찾는다.
print(index)

print(python.find("n"))
print(python.find("Java")) # 원하는 값이 포함되어 있지 않을 때 -1을 반환한다.
print(python.index("Java")) # 원하는 값이 포함되어 있지 않을 때 오류를 반환한다.

print(python.count("n")) # n이 몇 개 있는지 출력