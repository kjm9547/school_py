input_num = int(input("정수를 입력하시오"))

sum =0

last_num = input_num%10
second = input_num//10%10
third = input_num//100%10
fourth = input_num//1000
sum = last_num +second +third + fourth
print("자리수의 합 ", sum)
