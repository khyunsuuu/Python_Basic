'''
당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오/.

조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1 ~ 20 이라고 가정한다.
조건2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3: random 모듈의 shuffle 와 sample 을 활용한다.

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다. -- 

(활용 예제)
from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst) #list 안의 순서를 무작위로 변경한다.
print(lst)
print(sample(list, 1)) # 뒤의 숫자 만큼 무작위로 sample을 뽑는다.

'''

# 내가 쓴 답
from random import *
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(lst)
print("-- 당첨자 발표 -- ")
print("치킨 당첨자 : " + str(sample(lst,1)))
print("치킨 당첨자 : " + str(sample(lst,3)))
print("-- 축하합니다 -- ")


# 정답 (range는 방금 알려줌)
from random import *
users = range(1, 21) # 1부터 20까지 숫자를 생성
#print(type(users))
users = list(users)
#print(type(users))
shuffle(users)
winners = sample(users, 4) # 중복 불가이기 때문에 한번에 4명을 뽑았다.
print("-- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("치킨 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 -- ")
