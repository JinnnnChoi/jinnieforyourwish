cabinet = {3:"유재석", 100:"김태호"} # key 는 3이고 value는 유재석
print(cabinet[3]) # 유재석
print(cabinet[100])

# 다른 방법 : .get
print(cabinet.get(3))

print(cabinet.get(5)) # 오류 없이 none 출력 후 다음 출력 가능
print("hi")
print(cabinet.get(5, "사용 가능")) # default 값 출력(사용 가능)

#print(cabinet[5]) # 오류 나면서 다음 hi 값 적히지 않는다. # cabinet.5에 값이 없어서 오류 후 프로그램 종료
print("hi")

print(3 in cabinet) # True : in 사용 key 값 있는지 확인
print(5 in cabinet) # False 

cabinet = {"A-3":"유재석", "B-100":"김태호"} # 문자열로도 KEY 가능
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님 : del
del cabinet["A-3"]
print(cabinet)

# key 들만 출력 : .keys
print(cabinet.keys())

# value 들만 출력 : .values
print(cabinet.values())

# key, value 쌍으로 출력 : .items
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear() # {} 만 남음
print(cabinet)