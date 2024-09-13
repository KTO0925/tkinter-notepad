from tkinter import *
from tkinter.filedialog import *

def new_file(): #새로 만들기 함수
    text_area.delete(1.0,END)

def save_file(): #저장 함수
    f = asksaveasfile(mode="w",defaultextension=".txt",filetypes=[('Text files','.txt')])
    text_save = str(text_area.get(1.0,END))
    f.write(text_save)
    f.close()

def maker(): #만든이 함수
    help_view = Toplevel(window)
    help_view.geometry("300x50")
    help_view.title("만든이")
    lb = Label(help_view, text ="KTO가 만든 메모장입니다.")
    lb.pack()

#window tkinter GUI 틀 제작
window = Tk()
window.title("Notepad")
window.geometry("400x400")
window.resizable(False,False)

menu = Menu(window)
menu_1 = Menu(menu, tearoff= 0)
menu_1.add_command(label="새파일",command=new_file)
menu_1.add_command(label="저장",command=save_file)
menu_1.add_separator()
menu_1.add_command(label="종료", command=window.destroy)

menu.add_cascade(label="파일",menu=menu_1) #상단바 파일 메뉴 생성

menu_2 = Menu(menu,tearoff=0)
menu_2.add_command(label="만든이",command=maker) #하위 만든이(상위 만든이 X)

menu.add_cascade(label="만든이",menu=menu_2) #상단바 만든이 메뉴 생성

text_area = Text(window)
window.grid_rowconfigure(0,weight=1) # 행 방향 공백을 채우는 메소드
window.grid_columnconfigure(0,weight=1) #열 방향 공백을 채우는 메소드
text_area.grid(sticky= N + E + S + W) #영역을 격자 단위로 나누어 텍스트 창의 위치를 지정

window.config(menu=menu)

window.mainloop() #창 계속 띄우기