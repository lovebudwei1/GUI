import tkinter
from tkinter import ttk
import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='1234',
                     database='baoding')


def change_area(*args):
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


def change_op(*args):
    global list
    opname_data = langlist.get()
    opname_data = opname_data.split(',')
    cur.execute("SELECT typeid,typename FROM typetable where opid = %s", opname_data[0])
    cur_typename = cur.fetchall()
    list_typename = []
    for j in cur_typename:
        print(j)
        list_typename.append(('%s' + ',' + '%s') % (j[0], j[1]))
    list3['value'] = list_typename
    list3.current(0)


win = tkinter.Tk() # 创建窗口
mode = tkinter.StringVar()  # 创建变量
langlist = tkinter.StringVar() # 创建变量
langlist2 = tkinter.StringVar() # 创建变量
list1 = ttk.Combobox(win, textvariable=mode, state='readonly', width=10) # 创建下拉列表
list1.bind("<<ComboboxSelected>>", change_area) # 绑定事件,(下拉列表框被选中时，绑定change_area()函数)
cur = db.cursor() # 创建游标
cur.execute("SELECT areaid,areaname FROM area")
cur_area = cur.fetchall()
list_area = []
for i in cur_area:
    list_area.append(('%s' + ',' + '%s') % (i[0], i[1]))
list1["value"] = list_area  # 设置下拉列表的值
list1.current(0) # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
list2 = ttk.Combobox(win, textvariable=langlist, state='readonly') # 创建下拉列表
list2.bind("<<ComboboxSelected>>", change_op) # 绑定事件,(下拉列表框被选中时，绑定change_op()函数)
list2.config(values=[" "]) # 设置下拉列表的值
list2.current(0) # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
list3 = ttk.Combobox(win, textvariable=langlist2, state='readonly') # 创建下拉列表
list3.config(values=[" "]) # 设置下拉列表的值

list1.pack()
list2.pack()
list3.pack()

win.mainloop()
