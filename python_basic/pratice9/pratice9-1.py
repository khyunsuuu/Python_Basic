# 클래스

'''
# 마린 : 공격 유닛, 군인, 총을 쓸 수 있다.
name = "마린" # 유닛의 이름
hp = 40 # 유닛의 체력
damage = 5 # 유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크: 공격 유닛, 탱크, 포를 쏠 수 있다, 일반모드/ 시즈모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)
'''

# 클래스로 변경
# __init__ 파이썬에서 쓰이는 생성자이다. (객체가 만들어질 때 자동으로 호출되는 부분)
# 객체 - 마린이나 탱크 처럼 클래스로부터 만들어지는 부분을 객체라고 한다.
# 인스턴스 - 이때 마린과 탱크는 Uint 클래스의 인스턴스라고 부른다.
# self.name, self.hp, self.damage -> 맴버 변수 (클래스 내에서 정의된 변수이고, 그 변수를 가지고 우리가 출력하고 사용할 수 있는)
class Unit:
    def __init__(self, name, hp, damage): 
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
marine1 = Unit("탱크", 150, 35)
# marine3 = Unit("마린") (오류) -> 객체가 생성될 때 유닛 함수에 동일한 갯수 만큼 값을 전달해줘야 한다.

# 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않는다.)
wraith1 = Unit("레이스", 80, 5)
print("유닛이름: {0} 공격력: {1}".format(wraith1.name,wraith1.damage)) # 변수명.name 을 통해 맴버 변수에 접근할 수 있다.

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗기)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # 위의 클래스에 없지만 외부에서 변수를 추가로 할당해서 값을 저장했다. (확장을 한 객체에만 포함이 되고 다른 객체에서는 사용할 수 없음.)

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))