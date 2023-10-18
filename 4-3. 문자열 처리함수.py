python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # TRUE 출력
print(len(python)) # len : 길이값
print(python.replace("Python", "Java")) # .replace : 대체
print(python.count("n")) # .count : 해당값 몇 번 나오는지 센다

index = python.index("n") # 위치가 몇번째인지 알려줌
print(index)

index = python.index("n", index + 1) # 2번째 n 위치 찾기
print(index)

print(python.find("n")) # 위치 찾아줌
print(python.find("Java")) # 단, find는 원하는 값이 없으면 -1 출력
print("hi") # -1 출력 후에 다음 줄 문자열 출력 가능

print(python.index("Java")) # index는 원하는 값이 없으면 error 후 종료
print("hi") # 윗 줄에서 error 발생했기 때문에, print("hi")도 안 뜬다
