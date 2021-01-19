import sqlite3
from tkinter import *
from tkinter import ttk

conn = sqlite3.connect("database.db", isolation_level=None)
c = conn.cursor()

def insert(name, score):
    c.execute("CREATE TABLE IF NOT EXISTS rank(name text, score int)")
    sql = "INSERT INTO rank (name, score) VALUES(?, ?)"
    c.execute(sql, (name, score))
    conn.commit()
    showRank()

def rank(score):
    root = Tk()
    userlist = []
    scorelist = []

    root.title("점수 입력창")
    root.geometry("300x100")
    label = Label(root, text="이름을 입력하세요.")
    nameInput = Entry(root, width = 30)
    nameInput.pack()
    btn = Button(root, text="입력", command=lambda: insert(nameInput.get(), score))
    btn.pack()
    root.mainloop()

def showRank():
    pass