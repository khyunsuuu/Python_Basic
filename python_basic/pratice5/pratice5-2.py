# 딕셔너리 {키:값}
cabinet = {3:"유재석", 100:"김태호"}

# 방법 1
print(cabinet[3])
print(cabinet[100])

# 방법 2
print(cabinet.get(3))

#print(cabinet[5]) # 5라는 키가 없기 때문에 에러를 반환
print(cabinet.get(5)) # 5라는 키가 없으면 None을 반환
print(cabinet.get(5, "사용가능")) # 5라는 키가 없으면 "사용 가능"을 반환

print(3 in cabinet) # 키가 있으면 True
print(5 in cabinet) # 키가 없으면 False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새로운 손님
cabinet["A-3"] = "김종국" # 키 값이 이미 사용중이면 덮어 씌워진다.
cabinet["C-20"] = "조세호" # 추가
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key. value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)

