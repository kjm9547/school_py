from tkinter import *
import os
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from turtle import width

def open_file():
    file = askopenfilename(title="파일선택", filetypes=(("텍스트 파일", "*.txt"), 
    ("all files", "*.*")))
    window.title(os.path.basename(file) + " - 메모장")
    text.delete(1.0, END)
    f=open(file, "r")
    text.insert(1.0, f.read())
    f.close()

def save():
    file = filedialog.asksaveasfile(parent=window, mode='w')
    if file != None: # text.get() 은 입력된 내용을 얻을 때 사용
        lines = text.get('1.0', END+'-1c') # 1.0 은 1번째 행, 0번째 글자
        file.write(lines) # -1c 는 맨끝에서 한 문자만 제거
        file.close()
 
def exit():
    if messagebox.askokcancel("Quit", "종료하시겠습니까?"):
        window.destroy()
def about():
    label = messagebox.showinfo("About", "메모장 프로그램")

def create_new_file():
    text.delete(1.0,END)
def delete():
    text.delete(SEL_FIRST,SEL_LAST)
def copy():
    global es    
    es = text.get(SEL_FIRST,SEL_LAST)
def paste():
    global es
    text.insert(INSERT,es)
def cut():
    global es
    es = text.get(SEL_FIRST,SEL_LAST)
    text.delete(SEL_FIRST,SEL_LAST)
window = Tk()
text = Text(window, height=30, width=80)
text.grid(sticky= N + E + S + W)

ScrollBr = Scrollbar(text)
text = Text(text, yscrollcommand = ScrollBr.set)
text.pack(side="left", fill="both", expand=True)
ScrollBr.pack(side=RIGHT,fill=Y)


menu = Menu(window) # 윈도우에 메뉴 객체 생성
filemenu = Menu(menu) # 메뉴 탭 항목 추가
menu.add_cascade(label="파일", menu=filemenu) # 상위 메뉴 탭 설정
filemenu.add_command(label="열기", command=open_file) # 항목 추가
filemenu.add_command(label="저장하기", command=save) # 항목 추가
filemenu.add_command(label="종료", command=exit) # 항목 추가
filemenu.add_command(label="새로만들기",command=create_new_file)
helpmenu = Menu(menu)
menu.add_cascade(label="도움말", menu=helpmenu)
helpmenu.add_command(label="프로그램 정보", command=about)
window.config(menu=menu) # 생성된 객체를 해당 윈도우 창에 메뉴 등록

editmenu = Menu(menu)
menu.add_cascade(label="edit",menu=editmenu)
editmenu.add_command(label="cut",command=cut)
editmenu.add_command(label="delete",command=delete)
editmenu.add_command(label="copy",command=copy)
editmenu.add_command(label="paste",command=paste)


window.mainloop()