# 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오
#     Follow link(ctrl + click)

# 예) http://naver.com
# 규칙 1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#                           (nav)         (5)             (1)     (!)
# 예) 생성된 비밀번호 : nav51!

url = "http://google.com"
my_str = url.replace("http://", "") # 규칙 1 의거
print(my_str)

my_str = my_str[:my_str.index(".")] # my_str 변수 중에서 자를 건데 my_str에서 처음 점이 나오는 위치 직전까지
#my_str[0:5]
print(my_str) # 규칙 2 의거

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다".format(url, password))