# import sys
# print("Python", "Java", file=sys.stdout) # stdout: 표준출력으로 문장이 찍힘
# print("Python", "Java", file=sys.stderr) # stderr: 표준 에러로 처리
# 로그 처리를 따로 할 때, 표준출력에 대해서는 잘 출력되니 신경 쓸 필요 없으나
# error 경우, 확인해서 프로그램 코드 수정이 필요하기 떄문에
# stderr 필요하면 따로 에러처리 가능

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

print("Python", "Java", "JavaScript", sep=",", end="?") # end의 역할
print("무엇이 더 재미있을까요?")

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) #zfill : 채우는 용

answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")