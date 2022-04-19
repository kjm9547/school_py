

while True:
    num = input("숫자를 입력하세요")
    if num == 'a':
        print("프로그램을 종료합니다.")
    elif num  >'a':
        print("문자를 입력하였습니다.")
    else:
        num = float(num)
        if num <2 or num >1000:
            print("2~1000사이의 값을 입력해주세요.")
        elif num%1 > 0:
            print("정수형을 입력해주세요")
        else:
            num = int(num)
            cnt = 0
            text =""
            for i in range(2,num+1,1):
                stack = 0
                for y in range(1,i+1,1):
                    if i%y==0:
                        stack+=1
                if stack == 2:
                    text +=str(i)
                    text += " "
                    cnt+=1
                    stack =0
                if i%100 == 0:
                    text += '\n'
                    cnt =0
        print(text)
        break
    