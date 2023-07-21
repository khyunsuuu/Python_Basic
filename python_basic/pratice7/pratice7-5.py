# 가변인자
'''
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름: {0}\t나이: {1}\t".format(name,age), end=" ") # 프린트 문이 끝날 때 줄바꿈을 하지 않고 end= 에 있는 부분으로 이어진다.
    print(lang1, lang2, lang3, lang4, lang5)
'''

# 만약 유재석씨가 할 줄 아는 언어가 늘어났을 때 가변 인자를 사용할 수 있다.
def profile(name, age, *language):
    print("이름: {0}\t나이: {1}\t".format(name,age), end=" ") # 프린트 문이 끝날 때 줄바꿈을 하지 않고 end= 에 있는 부분으로 이어진다.
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "c#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")
