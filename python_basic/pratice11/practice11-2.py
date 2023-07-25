# 패키지
# import travel.thailand.ThailandPackage -> 사용 불가능
'''
import travel.thailand # 모듈, 패키지만 import 가능
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

from travel import *
trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()
'''
# 파일 위치 확인하기.
from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))