import random
x = random.randint(1,100)
y= random.randint(1,100)
print(x,'-',y,'=')
answer = int(input())

if x-y == answer:
    print("맞았습니다.")
else:
    print("틀렸습니다.")