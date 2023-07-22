# pickle - 프로그램 상에서 우리가 사용하고 있는 데이터를 파일 형태로 저장하는 방법.
import pickle

'''
profile_file = open("profile.pickle", "wb") # wb - w = write , b = 바이너리(pickle을 이용하기 위해서는 필수이다.)
profile = {"이름":"박명수", "나이:":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장한다.
profile_file.close()
'''

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()