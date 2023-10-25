# 멤버변수 : 클래스 내에서 정의된 변수. (name, hp, damage)

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
# . 으로 멤버 변수에 접근 가능

################################확장 변수
# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (뺴앗음)
wraith2 = Unit("뺴앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
    # 클로킹 변수는 유닛 클래스에 없는데 추가 할당함.
    # 클래스 외부에서 원하는 변수에 대한 확장 가능. 
    # 확장 변수는 확장 개체에 대해서만 적용됨! 
    # 즉 wraith2 에만 적요
