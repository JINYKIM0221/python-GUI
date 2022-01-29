from cgitb import text
from tkinter import *
from unittest import result
from tkinter import messagebox as msg
W=Tk()
W.geometry("300x100")
W.option_add("*Font","고딕 30")

E=Entry(W)
E.pack()

#로또번호 크롤링
def lotto():
    import requests #웹사이트 크롤링을 위해선 requests()설치가 필수
    from bs4 import BeautifulSoup#BeautifulSoup4도 필수
    n = E.get()#n에 E.get() : 우리가 입력창에 입력할 값 -> w
    if n >= 1: #n이 1보다 크면 밑의 함수 재생
        url="https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(n)#url에서 실수 n값을 괄호에 넣음
        result = requests.get(url)#requests로 url을 얻어오는 것을 result에 넣음
        soup=BeautifulSoup(result.text,"html.parser")#bs4에서 url에서 얻은 웹페이지 정보를 txt로 가져옴 html.parser형식으로 정리
        A = soup.find("div",{"class":"win_result"}).get_text()#<div class win_result를 text로 soup에서 가져옴
        lotto_list = A.split("\n")[7:13]#A 값을 줄바꿈 \n으로 나눠서 로또번호가 있는 어레이에서 7~12까지 가져옴
        lotto_bonus = A.split("\n")[-4]#A값에서 마지막 4번째만 가져옴
        print("당첨번호 : ",lotto_list )
        print("보너스번호 : ", lotto_bonus)
    else:
        msg.showinfo('경고창',"1이상의 값을 입력하시오")
    



btn=Button(W)
btn.config(text="로또")
btn.config(width=20)
btn.config(command = lotto)
btn.pack()












W.mainloop()
