# 튜플 (조회만 가능 하지만 리스트보다 속도가 빠르다.)
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까쓰") - 값을 변경 불가능

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

name,age,hobby = ("김종국", 20, "코딩")
print(name, age, hobby)