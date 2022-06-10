problem = {"파이썬":"가장떠오르는 언어","변수":"메모리공간","함수":"문장의 집합","리스트":"서로 관련이 있는항목"}

for i in problem.keys():
    print(i)
    print(problem[i])
    answer =input("답은?")
    if answer == int(answer):
        print("숫자입니다")
    elif answer == i:
        print("정답")
    else:
        print("오류")