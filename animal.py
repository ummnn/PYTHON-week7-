#2019038027이동현
#애완동물선택 프로그램

from tkinter import*

def myFunc():
    if var.get() == 1: #1번을 선택한 경우
        labelImage.configure(image=photo1) #1번이미지 출력
    elif var.get() == 2: #2번을 선택한 경우
        labelImage.configure(image=photo2) #2번이미지 출력
    else: #나머지
        labelImage.configure(image=photo3) #3번이미지 출력

var,labelImage=0,None
photo1,photo2,photo3=[None]*3

window = Tk() #윈도우창 생성
window.geometry("400x400") #창크기 설정
window.title("애완동물 선택하기") #타이틀명 설정
labelText = Label(window, text="좋아하는 동물 투표", fg="black", font=("궁서체",20)) #텍스트 설정

var = IntVar() #정수형타입 변수 생성
rb1 = Radiobutton(window, text = "강아지", variable = var, value = 1) #1번 버튼
rb2 = Radiobutton(window, text = "고양이", variable = var, value = 2) #2번 버튼
rb3 = Radiobutton(window, text = "호랑이", variable = var, value = 3) #3번 버튼
buttonOK = Button(window, text = "사진 보기", command = myFunc) #사진보기 버튼

photo1 = PhotoImage(file = "photo/dog1.gif") #강아지사진
photo2 = PhotoImage(file = "photo/cat.gif") #고양이사진
photo3 = PhotoImage(file = "photo/tiger1.gif") #호랑이사진

labelImage = Label(window, width = 200, height = 200, bg = "yellow", image = None) #이미지 크기 배경 설정

labelText.pack(padx = 5, pady = 5) #여백설정
rb1.pack(padx = 5, pady = 5)
rb2.pack(padx = 5, pady = 5)
rb3.pack(padx = 5, pady = 5)
buttonOK.pack(padx = 5, pady = 5)
labelImage.pack(padx = 5, pady = 5)

window.mainloop() #윈도우가 종료될떄까지 실행