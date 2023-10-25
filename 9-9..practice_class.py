class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__()
        # 결과는 제일 뒤의 클래스만 불러옴. 즉,
        # Unit 생성자 (결과값)
        # 둘다 부를거면 밑에 처럼 불러온다.
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()

############# 최종결과
# Unit 생성자
# Flyable 생성자
