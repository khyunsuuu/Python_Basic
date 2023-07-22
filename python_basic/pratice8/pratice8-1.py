'''
print("Python", "Java")
print("Python" + "Java")
print("Python", "Java", sep = ", ")
print("Python", "Java", sep = "," , end="?")  # end = 문장의 끝 부분을 물음표로 바꿔주어라 , 원래는 줄바꿈이 기본 옵션이다.
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file=sys.stdout) # 표준 출력으로 처리.
print("Python", "Java", file=sys.stderr) # 표준 에러로 처리가 된다. 
'''

# 시험 성적
scores = {"수학":0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    # ljust(8) - 왼쪽으로 정렬을 하는데 총 8칸의 공간을 확보한 상태에서 진행.
    # rjuest(4) - 오른쪽으로 정렬을 하는데 총 4칸의 공간을 확보한 상태에서 진행.


# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) # 공간을 3개 확보하여 빈 공간에 0을 채워 넣는다.

# 표준 입력
answer = input("아무 값이나 입력하세요: ")
print("입력하신 값은 " + answer + "입니다.") # input 입력값은 모두 typoe = str