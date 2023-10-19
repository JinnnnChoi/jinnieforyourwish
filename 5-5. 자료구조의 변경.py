# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # 중괄호 사용했어서 세트로 들어감

menu = list(menu)
print(menu, type(menu)) # type 이 list로 바뀜

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))
