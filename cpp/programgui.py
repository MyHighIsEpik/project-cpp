from tkinter import*
import tkinter as tk

root = tk.Tk()
root.geometry("400x240")

def getText():
    result = textExample.get("1.0", "end")
    print(result)

def callback():
    b1["text"] = "버튼 클릭"

label = tk.Label(root, text = 'CPP 회원가입시 받은 랜덤코드를 입력해주세요')
label.pack()
textExample=tk.Text(root, height=10)
textExample.pack()
b2 = tk.Button(root, text = '랜덤코드 확인하기')
b2.pack()
b1 = tk.Button(root, text = '제출', command=getText)
b1.pack()
tk.mainloop()