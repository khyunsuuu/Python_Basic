# 패키지
# import travel.thailand.ThailandPackage -> 사용 불가능
'''
import travel.thailand # 모듈, 패키지만 import 가능
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
'''

from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()
