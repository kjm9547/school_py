import random

user_num = int(input("복권번호를 입력하시오(0에서 99사이)"))
cpu_num = random.randint(0,99)
print("당첨번호는" ,cpu_num)
stack = 0

c_ten = cpu_num//10
c_one = cpu_num%10
u_ten =user_num//10
u_one = user_num%10
print(c_ten,c_one)

if c_ten == u_ten or c_ten==u_one:
    stack+=1

if c_one == u_ten or c_one==u_one:
    stack +=1

if stack>=2:
    print("당첨금은 100만원")
if stack ==1:
    print("당첨금은 50만원")
if stack == 0:
    print("당첨금은  0원")