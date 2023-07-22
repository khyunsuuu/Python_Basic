# 파일 입출력
'''
score_file = open("score.txt", "w", encoding="utf8")
# open -> 파일 열기 (1. 파일 이름 , 2. write(w), 3. 한글 정보를 제대로 확인하기 위함.)
print("수학: 0", file=score_file)
print("영어: 50", file=score_file)
score_file.close() # 열었으면 꼭 닫아줘야 한다.

score_file = open("score.txt", "a", encoding="utf8") # append를 나타내는 a를 이용하여 추가 작성
score_file.write("과학: 80")
score_file.write("\n코딩: 100")
score_file.close()


score_file = open("score.txt", "r", encoding="utf8") # read를 나타내는 r을 이용하여 읽기
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동한다.
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()
'''

# 가져오고 싶은 파일이 몇 줄인지 모를 때 처리 방법
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

# list에 파일 값을 넣어서 처리 하는 방법
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()