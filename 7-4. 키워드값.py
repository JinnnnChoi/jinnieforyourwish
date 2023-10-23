def profile(name, age, main_lang):
    print(name, age, main_lang)

# 키워드에 해당하는 값이, 순서가 뒤바뀌어도 정렬되어 출력
profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")
