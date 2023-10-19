# 리스트 [] : 순서를 가진 객체의 집합
# 지하철 칸별로 10명, 20명, 30명
# 그동안은 하단과 같이 했음
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30] # 순서대로 이 값이 들어감. 상단의 서로 다른 변수 3개 정의와 다르게 표현
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 리스트 활용하기
# 조세호는 몇 번 째칸에 타고 있는가? : .index
print(subway.index("조세호"))

# 하하가 다음 정류장에서 다음 칸에 탐 : .append
subway.append("하하") #append : 더하는 것
print(subway)

# 정형돈을 유재석 / 조세호 사이에 태워봄 : .insert
subway.insert(1,"정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄 : .pop
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인 : .count
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능 : .sort
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능 : .reverse
num_list.reverse()
print(num_list)

# 모두 지우기 : .clear
num_list.clear
print(num_list)

# 다양한 자료형 함께 사용 가능
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장 : [5, 4, 3, 2, 1, '조세호', 20, True]
num_list.extend(mix_list)
print(num_list)