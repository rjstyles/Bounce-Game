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
    btn = Button(root, text="입력", command=lambda: (insert(nameInput.get(), score), root.destroy(), showRank()))
    btn.pack()
    root.mainloop()

#랭크를 보여주는 함수.
def showRank():
    root = Tk()
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    root.title("순위표")
    root.geometry("300x230")
    try:
        sql = "SELECT * FROM rank order by score DESC"
        res = c.execute(sql)
    except:
        res = []
    treelist=[]
    for r in res:
        treelist.append(r)

    treeview = ttk.Treeview(root, columns=["이름", "점수"], displaycolumns=["이름", "점수"], yscrollcommand = scrollbar.set)
    treeview.pack()

    treeview.column("#0", width=50, anchor="center")
    treeview.heading("#0", text="순위", anchor="center")

    treeview.column("이름", width=100, anchor="center")
    treeview.heading("이름", text="이름", anchor="center")

    treeview.column("점수", width=100, anchor="center")
    treeview.heading("점수", text="점수", anchor="center")

    for i in range(len(treelist)):
        treeview.insert('', 'end', text=i+1, values=treelist[i])

    treeview.pack()

    #root.mainloop()