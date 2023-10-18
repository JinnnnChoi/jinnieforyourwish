jumin = "990120-1234567"

print("성별 : " + jumin[7]) # []로 필요한 것에 대한 위치 지정
print("연 : " + jumin[0:2]) # 실제 자릿수 -1 로 범위 지정
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지 범위
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 (뒤부터 계산해보기): " + jumin[-7:]) # 맨 뒤에서부터
