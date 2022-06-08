word = input("기호를 입력하세요")
text = input("삽입할 문자열을 입력하시오")

s = word[:1] + text + word[1:]

print(s)