# 지역변수: 함수 내에서만 쓸 수 있음(함수 호출될 때만 사용)
# 전역변수 : 프로그램 내에 어디서든 불러서 쓸 수 있음

gun = 10 # 외부에서 gun 이라는 변수 설정

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun을 사용하겠다는 의미
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2) # checkpoint로 바로 불어들여옴 gun을
print("남은 총 : {0}".format(gun))