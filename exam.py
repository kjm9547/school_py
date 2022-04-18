## 숫자 10개 뽑기
## 조건 처리 문자 입력 시 범위 오류 언제든지 q입력 시 종료

import random

r= random.Random()
ran_num = r.randint(1,100)
cnt  =0
while True:
    user_num = input("1~100사이의 수를 입력해주세요")    
    if user_num == 'q':
        break
    if user_num > 'a':
        print("문자를 입력하였습니다.")
    
    elif user_num < 'a':
        user_num = int(user_num)
        if user_num > 100 or user_num <0:
            print("숫자의 범위를 확인해주세요")
    
        if cnt == 10:
            break
        if user_num > ran_num:
            cnt+=1
            print("down")
        elif user_num < ran_num:
            cnt+=1
            print("up")
        elif user_num == ran_num:
            end = input("프로그램을 종료합니까?")
            if end == '\n':
                break
            