absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡했음
for student in range(1, 11): # 총 10명 가정
    if student in absent:
        continue
    elif student in no_book: 
        print("오늘 수업 여기까지. {0}는 교무실로 따라와.".format(student))
        break # 지금 상황에서 나머지 수행안하고 바로 탈출 후 끝
    print("{0}, 책을 읽어봐".format(student))