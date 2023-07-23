# 상속 , 다중 상속
# 두 클래스에서 사용하는 멤버변수가 같을 때 상속을 통해 처리한다.

# 일반 유닛
class Unit:
    def __init__(self, name, hp): 
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit): # 상속받고 싶은 클래스 명 적기
    def __init__(self, name, hp, damage): 
        Unit.__init__(self, name, hp) # Unit 클래스를 통해 name 과 hp를 초기화 할 수 있다.
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

# 메딕: 의무병

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정한다.
firebat1.damaged(25)
firebat1.damaged(25)