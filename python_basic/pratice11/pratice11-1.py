# 모듈
'''
import theater_module
theater_module.price(3) # 3명이 영화보러 갔을 때 가격
theater_module.price_morning(4) # 4명이 조조 할인 영화 보러 갔을 때
theater_module.price_soldier(5) # 5명이 군인 할인 영화 보러 갔을 때

import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

# from random import *
from theater_module import *
price(3)
price_morning(4)
price_soldier(5)
'''

from theater_module import price, price_morning
price(5)
price_morning(6)
#price_soldier(7) - 불가능

from theater_module import price_soldier as price
price(5)