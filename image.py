#2019038027 이동현
#사진감상프로그램

from tkinter import *
from tkinter.filedialog import *

def func_open() : #파일을 여는 함수
    global photo
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename) #photo에 이미지경로 설정
    pLabel.configure(image = photo) #사진 레이블 생성
    pLabel.image = photo #이미지 추가

def func_exit() : #프로그램을 종료하는 함수
    window.quit()
    window.destroy()

def Up(): #확대함수
    global photo
    photo = photo.zoom(6, 6)
    pLabel.image = photo

def Down(): #축소함수
    global photo
    photo = photo.subsample(6, 6)
    pLabel.image = photo

if __name__== "__main__":
    window = Tk() #윈도우창 생성
    window.geometry("500x500") #창크기 지정
    window.title("사진 감상하기") #타이틀명 지정

    photo = PhotoImage() #PhotoImage함수 실행
    pLabel = Label(window, image = photo) #pLabel생성
    pLabel.pack(expand=1, anchor = CENTER) #중앙에 위치

    mainMenu = Menu(window)
    window.config(menu = mainMenu)
    fileMenu = Menu(mainMenu) #메뉴 생성

    mainMenu.add_cascade(label = "파일", menu = fileMenu) #파일메뉴 생성
    fileMenu.add_command(label = "파일 열기", command = func_open) #파일열기 클릭 시 func_open함수 실행
    fileMenu.add_separator() #구분선 생성
    fileMenu.add_command(label = "프로그램 종료", command = func_exit) #프로그램 종료 클릭 시 func_exit함수 실행
    pLabel.bind("<Up>", Up()) #윗방향키 입력시 Up함수 실행
    pLabel.bind("<Down>", Down()) #아래방향키 입력시 Down함수 실행

    window.mainloop()