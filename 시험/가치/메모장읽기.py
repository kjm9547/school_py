from tkinter import *
alp = {}
infilename = input("입력파일이름:")
infile = open(infilename,"r")
rfile = infile.read()
infile.close()

for line in rfile:
    for ch in line:
        if ch in alp:
            alp[ch] += 1
        else:
            alp[ch] = 1
print(alp)