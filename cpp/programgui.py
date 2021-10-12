from tkinter import*
import tkinter as tk
import pymysql
from tkinter import messagebox
from checkinfo import OsInfo, DiskInfo, RAMInfo, CPUInfo, VideoInfo
os = OsInfo()
disk = DiskInfo()
ram = RAMInfo()
cpu = CPUInfo()
grapic = VideoInfo()


root = tk.Tk()
root.geometry("400x240")

def insertcode():
    input_codenum1 = ""
    #mysql과 연결하는 부분
    conn = pymysql.connect(host='cppdb1.cdoxiwetunqp.ap-northeast-2.rds.amazonaws.com', port=3306, user = 'cppadmin', password = '2021project', db = 'cppdb', charset = 'utf8mb4')

    curs = conn.cursor(pymysql.cursors.DictCursor)

    input_codenum1 = edt1.get()

    try :    
        curs.execute(
            "INSERT INTO test (cpu, grapic, os, ram, cdisk, ddisk, edisk, fdisk, codenum) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (cpu, grapic, os, ram, disk[0], disk[1], disk[2], disk[3], input_codenum1))
    except :
        messagebox.showerror('오류', '데이터 입력 오류')
    else :
        messagebox.showinfo('성공', '데이터 입력 성공')
    curs.connection.commit()



def callback():
    messagebox.showinfo('정보', '웹사이트 마이페이지를 확인해주세요')


label = tk.Label(root, text = 'CPP 회원가입시 받은 랜덤코드를 입력해주세요')
label.pack()
edtFrame = Frame(root);
edtFrame.pack()
edt1 = Entry(edtFrame, width = 50)
edt1.pack()
b2 = tk.Button(root, text = '랜덤코드 확인하기', command=callback)
b2.pack()
b1 = tk.Button(edtFrame, text = '제출', command=insertcode)
b1.pack()
tk.mainloop()