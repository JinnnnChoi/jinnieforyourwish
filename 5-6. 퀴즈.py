# 추첨 통해 1명은 치킨, 3명은 커피 쿠폰
# 추첨 프로그램 작성

# 조건1 : 댓글은 20명이 작성, 아이디는 1~20 가정
# 조건2 : 무작위 추첨, 중복 불가
# 조건3 : random 모듈의 shuffle과 sample 활요

# (출력예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# (활용 예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

from random import *
users = range(1,21) # 1부터 20까지 숫자를 생성
# print(type(users))
users = list(users)
# print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명 커피

print(" -- 당첨자 발표 -- ")
print(" 치킨 당첨자 : {0}".format(winners[0]))
print(" 커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 -- ") 