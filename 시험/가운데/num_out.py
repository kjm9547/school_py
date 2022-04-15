num = int(input("4자리 수 입력하세요"))

sum=0
sum+=num//1000
print(sum)
sum+=num//100%10
print(sum)
sum+=num//10%100%10

sum+=num%1000%100%10
print(sum)
