# 예외 처리
# try 내부에 있는 문장이 실행이 되다가 except를 찾아서 관련 에러가 있으면 그 안의 내용을 출력한다.
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두번째 숫자를 입력하세요 : ")))
    #nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하셨습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err: # 설정한 오류가 아닌 모든 에러는 이 부분에서 처리 한다.
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)