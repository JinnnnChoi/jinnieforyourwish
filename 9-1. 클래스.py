# 마린 : 공격 유닛, 군인. 총 쏠 수 있음
name = "마린" # 유닛 이름
hp = 40 # 유닛 체력
damage = 5 # 유닛 공격력

print("{} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

    #결과: 마린 유닛이 생성되었습니다.
    #결과: 체력 40, 공격력 5

# 탱크 : 공격 유닛, 탱크. 포 쏠 수 있고, 일반모드/시즈모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

    # 결과: 탱크 유닛이 생성되었습니다.
    # 결과: 체력 150, 공격력 35

def attack(name, location, damage) :
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format( \
        name, location, damage))
    
attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)

    # 결과: 마린 : 1시 방향으로 적군을 공격합니다. [공격력 5]
    # 결과: 탱크 : 1시 방향으로 적군을 공격합니다. [공격력 35]


###############################################################
# 클래스는 붕어빵 기계임.
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

    # 마린 유닛이 생성되었습니다.
    # 체력 40, 공격력 5
    # 마린 유닛이 생성되었습니다.
    # 체력 40, 공격력 5
    # 탱크 유닛이 생성되었습니다.
    # 체력 150, 공격력 35

    # 해설 : 하나의 클래스를 통해 서로 다른 마린과 탱크 유닛을 출력
    # self는 자기 자신을 의미, 클래스 안에서 메소드 앞에는 항상 self 적는다.
    # self. 을 통해서 접근 가능하기 때문