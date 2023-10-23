# score_file = open("score.txt", "w", encoding="utf8") # w : write
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()


# score_file = open("score.txt", "a", encoding="utf8") # a : 덮어쓰기
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# 파일 읽어오기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

# 한줄씩 가져오기
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

# list에 값을 넣어서 처리하기
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")

score_file.close

