problems = {'파이썬': '최근에 가장 떠오르는 프로그래밍 언어', 
            '변수': '데이터를 저장하는 메모리 공간', 
            '함수': '작업을 수행하는 문장들의 집합에 이름을 붙인것',
            '리스트': '서로 관련이 없는 항목들의 모임'
            }
for word in problems.keys():
    while(1):
        print("다음은 어떤 단어에 대한 설명일까요?")
        print(problems[word])
        print("(1)파이썬 (2)변수 (3)함수 (4)리스트")
        a = input()
        if a=='q':
            break
        elif word==a:
            print("정답입니다.")
            break
        elif a=="파이썬"or a=="변수"or a=="함수" or a=="리스트":
            print("정답이 아닙니다.")
            break
        else:
            print(a," 는 보기 중 하나가 아님니다. 문제 Skip(q)")
    

text = input("종료하려면 엔터키")
if text == ' ':
    exit()
        