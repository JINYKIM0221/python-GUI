from tkinter import *
from datetime import datetime
W = Tk()
W.geometry("1250x500")
W.title("가계부")
W.option_add("*Font","고딕 20")

def what_time():
    dnow = datetime.now()
    btn.config(text=dnow)


btn = Button(W)
btn.pack()
btn.config(width=30)
btn.config(text="버튼")
btn.config(command = what_time)



W.mainloop()

print(datetime.now())
