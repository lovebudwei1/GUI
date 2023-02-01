import tkinter
from tkinter import ttk
import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='1234',
                     database='baoding')


def change(*args):
    global list
    area_data = mode.get()
    area_data = area_data.split(',')
    cur.execute("SELECT opid,opname FROM optable where areaid = %s", area_data[0])
    cur_opname = cur.fetchall()
    list_opname = []
    for j in cur_opname:
        list_opname.append(('%s' + ',' + '%s') % (j[0], j[1]))
    list2['value'] = list_opname
    list2.current(0)
win = tkinter.Tk()
mode = tkinter.StringVar()
langlist = tkinter.StringVar()
list1 = ttk.Combobox(win, textvariable=mode, state='readonly', width=10)
list1.bind("<<ComboboxSelected>>", change)
cur = db.cursor()
cur.execute("SELECT areaid,areaname FROM area")
cur_area = cur.fetchall()
list_area = []
for i in cur_area:
    print(i)
    list_area.append(('%s' + ',' + '%s') % (i[0], i[1]))
list1["value"] = list_area
list1.current(0)
list2 = ttk.Combobox(win, textvariable=langlist, state='readonly')
list2.config(values=["you choose A"])
list2.current(0)
list1.pack()
list2.pack()

win.mainloop()
