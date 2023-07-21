# 함수 개념 (전달값, 반환값)
def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money # return을 통해 값을 전달

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금하려는 돈 보다 많을 때
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))

def withdraw_night(balance, money): # 저녁에 출금
    commision = 100 # 수수료 100원
    return commision, balance - money - commision # 튜플 형식으로 보내준다.
balance = 0
balance = deposit(balance, 1000) # 안의 전달값이 함수의 인자로 들어감.
#balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이고, 잔액은 {1}원 입니다.".format(commission, balance))