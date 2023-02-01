import tkinter
from tkinter import ttk
import pymysql
# db = pymysql.connect(host='localhost',
#                      user='root',
#                      password='1234',
#                      database='mars')

def change(*args):
    # cur = db.cursor()
    # cur.execute("SELECT * FROM typedata where typeid-%s and classe = 2")

    global list
    if mode.get() == "A":
        print("a")
        list2.config(values=["you choose A"])
        list2.current(0)
    else:
        print("b")
        list2['value'] = ["you choose B", "you choose B yes"]
        list2.current(0)
win = tkinter.Tk()
mode = tkinter.StringVar()
langlist = tkinter.StringVar()
list1 = ttk.Combobox(win, textvariable=mode, state='readonly',width=10)
list1.bind("<<ComboboxSelected>>", change)
list1["value"] = ["A", "B"]
list1.current(0)
list2=ttk.Combobox(win, textvariable=langlist, state='readonly')
list2.config(values=["you choose A"])
list2.current(0)
list1.pack()
list2.pack()

win.mainloop()
