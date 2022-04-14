print("구구단 출력")
i=1

while True:
    y=1
    if i>9:
        break
    while True:
        print(i," * ",y," = ",i*y)
        y +=1
        if y>9:
            break
    i +=1     
    print("\n")