#2019038027이동현
#탭이 2개인 프로그램

from tkinter import*
from tkinter import ttk

window = Tk() #윈도우창 생성
window.iconbitmap('python.ico') #실행창에 아이콘 삽입

baseTab = ttk.Notebook(window) #기본탭 설정

tabDog = ttk.Frame(baseTab) #강아지탭 설정
baseTab.add(tabDog, text = '강아지') #강아지탭 추가
tabCat = ttk.Frame(baseTab) #고양이탭 설정
baseTab.add(tabCat, text = '고양이') #고양이탭 추가

baseTab.pack(expand=1,fill="both") #탭 표시

photoDog = PhotoImage(file = "photo/dog1.gif") #강아지 사진
labelDog = Label(tabDog, image = photoDog) #강아지사진 레이블 생성
labelDog.pack() #강아지사진 탭에 부착

photoCat = PhotoImage(file = "photo/cat.gif") #고양이 사진
labelCat = Label(tabCat, image = photoCat) #고양이사진 레이블 생성
labelCat.pack() #고양이사진 탭에 부착

window.mainloop() #윈도우가 종료될떄까지 실행