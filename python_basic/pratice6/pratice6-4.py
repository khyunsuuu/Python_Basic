# break, continue
absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡했다.
for student in range(1, 11): # 1, 2, 3, 4, 5, 6, 7, 8, 9 ,10
    if student in absent:
        continue # continue를 만나게 되면 밑에 문장으로 넘어가지 않고 다음 반복으로 넘어간다.
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break # 뒤의 반복값이 남아도 반복문을 탈출해버린다.
    print("{0}야, 책을 읽어봐".format(student))

