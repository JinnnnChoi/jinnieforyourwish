# 튜플은 리스트와 다르게, 내용 변경/추가 불가능
# 단, 속도가 리스트보다 빨라 변경되지 않는 목록 사용 떄 활용

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") : error

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)