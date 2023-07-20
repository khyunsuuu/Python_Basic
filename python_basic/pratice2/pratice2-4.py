# 애완동물을 소개해 주세요~ 
animal = "고양이"
name = " 해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3

# + 로 문자열을 합칠 때 정수형 변수나 boolean 변수는 str을 통해 형 변환을 해줘야 한다.
print("우리집" + animal + "의 이름은" + name + "예요")
# 중간에 변수값을 변경할 수 있다.
hobby = "공놀이"
#  , 로 문자열을 합치면 정수형 변수나 boolean 변수는 str을 통해 형 변환을 해주지 않아도 되지만 , 위치에 띄어쓰기 하나가 포함된다.
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))

