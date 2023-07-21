# 자료 구조의 변경
# 커피숍

# set
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

# set -> list
menu = list(menu)
print(menu, type(menu))

# list -> tuple
menu = tuple(menu)
print(menu, type(menu))

#tuple -> set
menu = set(menu)
print(menu, type(menu))