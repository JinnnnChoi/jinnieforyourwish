# 회사에서 매주 1회 작성해야 하는 보고서의 형태는 다음과 같다

# - X 주차 주간보고 - 
# 부서 : 
# 이름 : 
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성해라.

# 조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만든다.

for i in range(1,3):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write(" - {0} 주차 주간보고 - ".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 :")
