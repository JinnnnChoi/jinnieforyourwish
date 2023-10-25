# init : 파이썬에서 쓰이는 생성자임 (마린/탱크처럼 "객체" 만들어질 때 자동호출)
# 객체 : 마린/탱크처럼 클래스로부터 만들어지는 것
# 마린/탱크 : 유닛 클래스의 instance임.

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

marine3 = Unit("마린")
marine3 = Unit("마린", 40)
# init 안에 정의된 객체들이 필요함 