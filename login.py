from tkinter import *
from tkinter import messagebox as msg
from tkinter import Label

from cgitb import text
from unittest import result

from selenium import webdriver
W=Tk()
W.geometry("500x300")
W.title("Log-in")
W.option_add("*Font","고딕 30")

#네이버 로고
lab3=Label(W)#라벨을 창에 붙임
img = PhotoImage(file = "C:/Users/김진영/Downloads/네이버.png",master=W)#파일이 있는 주소와 창이 master라는 것을 알려줌
#photoimage는 변수안에 넣어줘야함
img = img.subsample(4)#이미지의 크기조정
lab3.config(image = img)#image와 가져온 파일과 같음
lab3.pack()#라벨 조정

#ID라벨
lab1 = Label(W)#라벨 생성
lab1.config(text="ID")#라벨 내용
lab1.pack()

#ID 입력창
E1 = Entry(W)#창에 입력 공간을 넣음
E1.insert(0,"wlsdudqkqh7@naver.com")#왼쪽부터 빠짐없이 id를 적음
def clear(event):
    if E1.get() == "wlsdudqkqh7@naver.com":
        E1.delete(0,len(E1.get()))#만약 E1(ID)창에 입력한 것이 id와 같다면 처음부터 끝까지 E1객체를 지움


E1.bind("<Button-1>",clear)#버튼의 왼쪽(-1)을 클릭하면 def clear작동
E1.pack()

#PW라벨
lab2 = Label(W)#라벨 생성
lab2.config(text="PW")#라벨 내용
lab2.pack()

#PW입력창
E2 = Entry(W)
E2.config(show="*")#*로 보이게함
E2.pack()

#로그인 버튼
btn = Button(W)
btn.config(text="로그인")#버튼에 "로그인"이라 넣음
def AUTO_login():
    WEB = webdriver.Chrome("C:/Users/김진영/Desktop/파이썬 가계부/chromedriver_win32 (4)/chromedriver")
    #크롬드라이버와 selenium을 깐다음에 Webdriver를 통해 chromedriver을 가져오고
    url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
    #네이버 id입력 페이지를 받아옴
    WEB.get(url)#크롬드라이버에서 네이버id입력페이지를 받고 가져옴
    WEB.implicitly_wait(5)#implicitly_wait 5초까지만 기다리는 함수
    xpath1 = "//input[@name='id']"#xpath로 경로 표시 input안에 있는 name=id태그를 가져옴
    WEB.find_element_by_xpath(xpath1).send_keys(E1.get())#xpath1에서 가져온 경로에 E1에 입력한 값을 보냄

    xpath2 = "//input[@name='pw']"#xpath로 경로 표시 input안에 있는 name=pw태그를 가져옴
    WEB.find_element_by_xpath(xpath2).send_keys(E2.get())#xpath2에서 가져온 경로에 E1에 입력한 값을 보냄

    xpath3 = "//button[@class='btn_login']"#xpath로 경로 표시 input안에 있는 class=btn_login 태그를 가져옴
    WEB.find_element_by_xpath(xpath3).click()#xpath3에서 가져온 경로를 클릭 (로그인 버튼 클릭)
btn.config(command=AUTO_login)
btn.pack()

# 메시지 라벨
lab4 = Label(W)
lab4.pack()

# def AUTO_login():
#     WEB = webdriver.Chrome("C:/Users/김진영/Desktop/파이썬 가계부/chromedriver_win32 (4)/chromedriver")
#     url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
#     WEB.get(url)
#     WEB.implicitly_wait(5)
#     xpath1 = "//input[@name='id']"
#     WEB.find_element_by_xpath(xpath1).send_keys(E1.get())

#     xpath2 = "//input[@name='pw']"
#     WEB.find_element_by_xpath(xpath2).send_keys(E2.get())

#     xpath3 = "//button[@class='btn_login']"
#     WEB.find_element_by_xpath(xpath3).click()

# lab.config(image = img)#라벨 이미지
# img=Photoimage(file = "temp.png".master=W)
# img = img.subsample(3)
# lab.pack()#라벨 배치

# ent.config(show="*")#입력문자숨기기
# ent.insert(0."temp@temp.com")#입력창 문자열 삽입
# ent.delete(0,3)# 0~2번째 문자열 삭제
# ent.bind("<Button-1>".clear)#입력창 클릭시 명령
W.mainloop()