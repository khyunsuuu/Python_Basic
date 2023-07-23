# pass, super

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed): 
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit): # 상속받고 싶은 클래스 명 적기
    def __init__(self, name, hp, speed, damage): 
        Unit.__init__(self, name, hp, speed) # Unit 클래스를 통해 name 과 hp를 초기화 할 수 있다.
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage)) 
        # name, damage는 맴버 변수 안의 값을 사용하고 location은 전달 받은 인자를 사용한다.
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage)) 
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0,damage) # 지상 speeds는 0
        Flyable.__init__(self, flying_speed)
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # super를 사용할 때는 self를 사용하지 않는다. (문제는 다중 상속을 진행할 때 발생한다.)
        self.location = location

'''
건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # 완성된 것 처럼 넘어가서 사용할 수 있음.


# 서플라이 디폿: 건물, 1개 건물 = 8 유닛 생성 가능
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()
'''