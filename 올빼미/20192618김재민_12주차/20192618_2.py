from tkinter import *
alp = {}
infilename = input("입력 파일 이름 : ")
infile = open(infilename, "r")
rfile = infile.read()
infile.close()

for line in rfile:
    for ch in line:
        if ch in alp:
            alp[ch] += 1
        else:
            alp[ch] = 1
print(alp)
