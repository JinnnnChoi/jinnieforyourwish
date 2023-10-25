# 오버로딩
# 자식 클래스에서 정의한 메소드를 쓰고 싶을 때, 메소드를 새로 정의해서 사용 
# 지상 유닛 만들어보기


## 부모 클래스에서 2개 이상 상속 받을 떄, (부모 둘 이상)
## 일반 유닛 (공격력 없음)
class Unit:
    def __init__(self, name, hp, speed): # speed for 지상유닛
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
              .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit):
   def __init__(self, name, hp, speed, damage): # speed 추가
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

    def move(self, location): # move 함수 재정의!!!!!!!
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
        
############### 지상유닛 만들기
# 벌처 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)
# 배틀크루저 : 공중 유닛, 체력과 공격력 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

############### 함수 사용
vulture.move("11시") # 지상유닛이기에 .move 사용
# battlecruiser.fly(battlecruiser.name, "9시") 
# # 어떤 유닛인지에 따라 사용함수 확인 필요한 번거로움
battlecruiser.move("9시") # 공중유닛인데 오버라이딩 사용하여 .move 사용가능

############### 최종 출력
# [지상 유닛 이동]
# 벌쳐 : 11시 방향으로 이동합니다. [속도 10]
# [공중 유닛 이동]
# 배틀크루저 : 9시 방향으로 날아갑니다. [속도 3]