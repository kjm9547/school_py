import random

options =["중앙","왼쪽 상단","왼쪽 하단", "오른쪽 상단", "오른쪽 하단"]
cpu = random.choice(options)
user = input("어디를 수비 하시겠어요?(중앙,왼쪽 상단,왼쪽 하단, 오른쪽 상단, 오른쪽 하단)")
print("컴퓨터는",cpu)
if cpu == user:
    print("패널티 킥이 실패하였습니다.")
else:
    print("패널티 킥이 성공하였습니다.")