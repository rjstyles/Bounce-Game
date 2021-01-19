import sqlite3
from tkinter import *
from tkinter import ttk

conn = sqlite3.connect("database.db", isolation_level=None)
c = conn.cursor()

#db에 데이터(입력한 이름, 점수)를 추가하는 함수.
def insert(name, score):
    c.execute("CREATE TABLE IF NOT EXISTS rank(name text, score int)")
    sql = "INSERT INTO rank (name, score) VALUES(?, ?)"
    c.execute(sql, (name, score))
    conn.commit()
    showRank()

#데이터추가를 위한 이름 입력창을 띄우는 함수.
def rank(score):
    root = Tk()
    userlist = []
    scorelist = []

    root.title("이름 입력창")
    root.geometry("300x100")
    label = Label(root, text="이름을 입력하세요.")
    nameInput = Entry(root, width = 30)
    nameInput.pack()
    btn = Button(root, text="입력", command=lambda: insert(nameInput.get(), score))
    btn.pack()
    root.mainloop()

#랭크를 보여주는 함수.
def showRank():
    pass