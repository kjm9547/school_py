import random

tries =0
guess =0
answer = random.randint(1,100)

print("1부터 100 사이의 숫자를 맞추시오")

while guess != answer:
    if tries == 10:
        print("10번 이상 시도 불가합니다. 프로그램을 종료합니다.")
        break
    guess = int(input("숫자를 입력하시오: "))
    tries = tries +1
    if guess < answer:
        print("낮음")
    elif guess > answer:
        print("높음")

if guess == answer:
    print("축하합니다. 시도횟수=", tries)
else:
    print("정답은", answer)