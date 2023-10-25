## LINE 62 부터 PASS
## 부모 클래스에서 2개 이상 상속 받을 떄, (부모 둘 이상)
## 일반 유닛 (공격력 없음)
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
              .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit):
   def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

   def attack(self, location):
       print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
             .format(self.name, location, self.damage))
       
   def damaged(self, damage):
       print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
       self.hp -= damage
       print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
       if self.hp <= 0:
           print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 x

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))
        
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
        
# 벌처 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력과 공격력 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")

########################################PASS
# 건물
class BuildingUnit(Unit) :
    def __init__(self, name, hp, location):
        pass # 해당 함수를 일단 넘어간다

# 서플라이 디폿 : 건물, 1개 건물 = 8유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()

########### 최종결과
# [지상 유닛 이동]
# 벌쳐 : 11시 방향으로 이동합니다. [속도 10]
# [공중 유닛 이동]
# 배틀크루저 : 9시 방향으로 날아갑니다. [속도 3]
# [알림] 새로운 게임을 시작합니다.