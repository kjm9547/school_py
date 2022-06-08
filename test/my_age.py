import time
t=time.time()

age = int(input("현재 나이를 입력해주세요"))
later_year = int(input("몇 년도의 나이를 구하십니까?"))
#만약 2150년

#올해 구하는 식
thisyear = int(1970+t//(365*24*3600))

old = later_year-thisyear
age = age +old
print(age)
