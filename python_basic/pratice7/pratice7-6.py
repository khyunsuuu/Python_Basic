# 지역변수와 전역변수
'''
gun = 10

def checkpoint(soldiers): # 경계근무
    gun = gun - soldiers #안에 있는 gun은 밖에 있는 gun 변수가 아니고 checkpoint 함수 내에서 만들어진 gun이다. (초기화가 되지 않아서 사용할 수 없다. = 지역변수)
    print("[함수 내] 남은 총: {0}".format(gun))

print("전체 총: {0}".format(gun))
checkpoint(2) # 2명이 경계 근무에 나갔다.
print("남은 총: {0}".format(gun))

-----------------------------------------------------------------------

gun = 10 # 여기의 gun 변수가 변하지 않았다.
def checkpoint(soldiers):
    gun = 20
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun)) # 18자루

print("전체 총: {0}".format(gun)) # 10자루 
checkpoint(2)
print("남은 총: {0}".format(gun)) # 10자루

-----------------------------------------------------------------------

# 전역 변수 사용 (일반적으로 전역 변수를 많이 쓰게 되면 코드 관리가 힘들어져서 권장되지 않는 방법이다.)
gun = 10
def checkpoint(soldiers):
    global gun # 전역 공간에 있는 gun을 사용하겠다.
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))
print("전체 총: {0}".format(gun)) 
checkpoint(2)
print("남은 총: {0}".format(gun))
'''

# 자주 사용하는 방법
gun = 10
def checkpoint_ret(gun, soldiers):
    gun = gun-soldiers # 지역 변수이다.
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun # 하지만 return을 해줌으로써 밖으로 값을 전달할 수 있다.

print("전체 총: {0}".format(gun)) 
gun = checkpoint_ret(gun, 2)
print("남은 총: {0}".format(gun))