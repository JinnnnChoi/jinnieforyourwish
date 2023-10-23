# pickle : 프로그램 상에서 사용하고 있는 데이터를 파일형태로 저장. 파일을 누군가에게 준다면 이를 사용가능

import pickle
# profile_file = open("profile.pickle", "wb") #b : binary 타입 정의 / 인코딩 따로 필요 없음
# profile = {"이름" : "박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()


# load 통해 불러옴.
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close
