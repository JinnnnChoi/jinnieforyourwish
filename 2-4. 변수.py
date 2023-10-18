# 애완동물을 소개해 주세요
print("우리집 강아지의 이름은 연탄이에요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True") # true는 boolean 형태임

# 값을 저장하는 "변수" 사용하기
# 변수 선언
animal = "강아지" 
name = "연탄이"
age = 4 # 정수형이라 따옴표 없음
hobby = "공놀이"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 연탄이에요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요") # str 사용함으로써 문자형으로 바꿔줌
print(name + "는 어른일까요? " + str(is_adult)) 

#print(name, "는", age, "살이며, ", hobby, "을 아주 좋아해요")
# 콤마(,) 로도 대체가능 / 다만 콤마 들어가면 띄어쓰기가 무조건 포함되어 print

#주석은 ''' (작은 따옴표 3개 앞뒤로도 가능)
# 여러 문장 선택후 ctrl + / 