print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
number = 2 + 3 * 4 # 14
print(number)

number += 2 # number = number + 2
number *= 2 # number = number * 2
number /= 2 # number = number / 2
number -= 2 # number = number - 2
number %= 2 #number = number % 2

# 절댓값 abs
print(abs(-5)) # 5
# 제곱값 pow
print(pow(4, 2)) # 4^2 = 4*4 = 16
# 최댓값 max
print(max(5, 12)) # 12
# 최소값 min
print(min(5,12)) # 5
#반올림 round
print(round(3.14)) # 3
print(round(4.99)) # 5

from math import *
print(floor(4.99)) # 내림 . 4
print(ceil(3.14)) # 올림 . 4
print(sqrt(16)) # 제곱근 . 4