# super를 사용할 때 문제점.

class Unit:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flayable 생성자")

class FlyableUnit(Unit, Flyable): # 순서에 따라서 앞에 순서인 클래스만 호출이 된다. (다중 상속을 사용할 때는 super를 사용하지 않는다.)
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()

