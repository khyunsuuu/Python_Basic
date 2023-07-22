# with - 조금 더 편하게 데이터를 저장할 수 있음.
import pickle
# profile.pickle을 열어서 profile_file이라는 변수로 저장하고 load를 통해 불러왔다.
# close도 필요 없다.
with open("profile.pickle", "rb") as profile_file: 
    print(pickle.load(profile_file))

# 2줄로 파일에 데이터를 작성할 수 있음.
with open("study.txt", "w", encoding="utf8") as study_file: 
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file: 
    print(study_file.read())