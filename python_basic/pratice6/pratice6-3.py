# while
'''
customer = "토르"
index = 5
while index >= 1:
    print("{0}님, 커피가 준비 되었습니다. {1}번 남았습니다. ".format(customer, index))
    index -= 1
    if index == 0:
        print("커피가 폐기처분되었습니다.")


customer = "아이언맨"
index = 1
while True:
    print("{0}님, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
    index += 1
'''

customer = "토르"
person = "Unknown"

# 안의 조건이 만족할 때까지 계속 반복한다.
while person != customer:
    print("{0}님, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")