from tkinter import*
import tkinter as tk
import pymysql
from tkinter import messagebox
from checkinfo import OsInfo, DiskInfo, RAMInfo, CPUInfo, VideoInfo
os = OsInfo()
disk = DiskInfo()
ram = RAMInfo()
cpu = CPUInfo()
graphic = VideoInfo()

root = tk.Tk()
root.title("CPP")
root.geometry("400x240")

#신규회원 PC사양 입력
def insertcode():
    input_codenum1 = ""
    #mysql과 연결하는 부분
    conn = pymysql.connect(host='cppdb1.cdoxiwetunqp.ap-northeast-2.rds.amazonaws.com', port=3306, user = 'cppadmin', password = '2021project', db = 'cppdb', charset = 'utf8mb4')

    curs = conn.cursor()

    input_codenum1 = edt1.get()

    try :           #입력받은 코드 값이 MySQL에 존재하는지 확인하는 코드
        curs.execute(
            "INSERT INTO user (codenum) VALUES (%s)", (input_codenum1)
        )
    except :        #입력받은 코드 값이 있을 경우 try에서의 insert문은 실행이 안 됨
        try :    
            curs.execute(
                "INSERT INTO user_pcinfo (codenum, cpu, graphic, os, ram, cdisk, ddisk, edisk, fdisk) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (input_codenum1, cpu, graphic, os, ram, disk[0], disk[1], disk[2], disk[3]))
        except :
            messagebox.showerror('오류', '이미 존재하는 코드입니다!')

        else :
            messagebox.showinfo('성공', '데이터 입력 성공')
        curs.connection.commit()

    else :          #입력받은 코드 값이 없을 경우
        messagebox.showerror('오류', '코드가 잘못 되었거나 아직 회원가입을 하지않은 상태입니다. 다시 한 번 확인 해주세요!')
       
#기존 회원 PC사양 업데이트 코드
def updatecode():
    #mysql과 연결하는 부분
    conn = pymysql.connect(host='cppdb1.cdoxiwetunqp.ap-northeast-2.rds.amazonaws.com', port=3306, user = 'cppadmin', password = '2021project', db = 'cppdb', charset = 'utf8mb4')

    curs = conn.cursor()

    input_codenum2 = edt1.get()

    try :           #입력받은 코드 값이 MySQL에 존재하는지 확인하는 코드
        curs.execute(
            "INSERT INTO user (codenum) VALUES (%s)", (input_codenum2)
        )
    except :        #입력받은 코드 값이 있을 경우 try에서의 insert문은 실행이 안 됨
        try :    
            curs.execute(
                "DELETE FROM user_pcinfo WHERE codenum = (%s)", (input_codenum2))
            curs.connection.commit()

            curs.execute(
                "INSERT INTO user_pcinfo (codenum, cpu, graphic, os, ram, cdisk, ddisk, edisk, fdisk) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (input_codenum2, cpu, graphic, os, ram, disk[0], disk[1], disk[2], disk[3]))
            curs.connection.commit()
                
        except :
            messagebox.showerror('오류', '이미 존재하는 코드입니다!')

        else :
            messagebox.showinfo('성공', '데이터 업데이트 성공')

    else :          #입력받은 코드 값이 없을 경우
        messagebox.showerror('오류', '코드가 잘못 되었거나 아직 회원가입을 하지않은 상태입니다. 다시 한 번 확인 해주세요!')


#PC사양 업데이트 확인 메세지창
def auth():
    str = messagebox.askyesno('확인', '이전의 PC 정보는 사라지게 됩니다. 정말 업데이트 하시겠습니까?', icon = 'error')
    if str == 1:
        updatecode()
    else: 
        messagebox.showinfo('정보','업데이트를 취소했습니다')

#랜덤코드 확인하기 눌렀을때 뜨는 창
def callback():
    messagebox.showinfo('정보', '웹사이트 마이페이지를 확인해주세요')


label = tk.Label(root, text = 'CPP 회원가입시 받은 랜덤코드를 입력해주세요', fg="Blue", font=("돋움체", 12, "bold"))
label.pack()
edtFrame = Frame(root);
edtFrame.pack()
edt1 = Entry(edtFrame, width = 50)
edt1.pack()
b2 = tk.Button(root, text = '랜덤코드 확인하기', command=callback, padx=5, pady=5)
b2.pack()
b1 = tk.Button(edtFrame, text = 'PC 정보 등록하기(신규회원)', command=insertcode, padx=5, pady=5)
b1.pack(side="left", fill='y')
b3 = tk.Button(edtFrame, text = 'PC 정보 업데이트 하기(기존회원)', command=auth, padx=5, pady=5)
b3.pack(side="right", fill='y')
tk.mainloop()