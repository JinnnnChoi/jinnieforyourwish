from random import * # random 라이브러리의 모든 것 사용

print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)

print(int(random() * 10)) # 0 ~ 10 미만의 정수 임의의 값 생성

print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성

# 로또 값 출력해보기
print(int(random() * 45) + 1) # int(random()) : 1 ~ 45 이하의 임의값
print(randrange(1,46))        # randrange: 1 ~ 45 이하의 임의값 생성, 더 편하게 생성
print(randint(1,45))          # randint:  1 ~ 45 이하의 임의값 생성