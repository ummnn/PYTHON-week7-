#2019038027 이동현
#그림판 프로그램

from tkinter import*
from tkinter.colorchooser import*
from tkinter.simpledialog import*

def mouseClick(event): #마우스를 클릭할때
    global x1, y1, x2, y2
    x1 = event.x    #x의 좌표를 찍는다
    y1 = event.y    #y의 좌표를 찍는다

def mouseDrop(event): #마우스를 뗄 때
    global x1, y1, x2, y2, penWidth, penColor
    x2 = event.x    #x의 좌표를 찍는다
    y2 = event.y    #y의 좌표를 찍는다
    canvas.create_line(x1,y1,x2,y2, width = penWidth, fill = penColor) #선을 긋는다

def getColor(): #색상을 선택
    global penColor
    color = askcolor() #askpencolor함수 실행
    penColor = color[1] #color 배열에서 불러온다

def getWidth(): #두께를 선택
    global penWidth
    penWidth = askinteger("선 두께", "선 두께(1~10)을 입력하세요", minvalue=1, maxvalue=10)

    window = None
    canvas = None
    x1, y1, x2, y2 = None, None, None, None
    penColor = 'black' #펜 색깔 설정
    penWidth = 5 #펜 두께 설정

window = Tk() #윈도우창 생성
window.title("그림판 프로그램") #타이틀명 설정
canvas = Canvas(window, height = 300, width = 300) #캔버스 크기 설정
canvas.bind("<Button-1>", mouseClick) #마우스왼쪽버튼이 눌릴 때 mouseClick 실행
canvas.bind("<ButtonRelease-1>", mouseDrop) #마우스왼쪽버튼을 뗄 떄 mouseDrop 실행
canvas.pack() #canvas배치

mainMenu = Menu(window) #메인메뉴 생성
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu) #메뉴 지정
mainMenu.add_cascade(label = "설정",menu = fileMenu) #하위메뉴 지정
fileMenu.add_command(label = "선 색상 선택", command = getColor) #메뉴 작동 지정
fileMenu.add_separator()
fileMenu.add_command(label="선 두께 설정", command = getWidth) #메뉴 작동 지정

window.mainloop() #윈도우가 종료될떄까지 실행