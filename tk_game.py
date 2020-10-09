import random
import tkinter as tk
from tkinter import messagebox
set_num = random.randint(1,100)
def check_and_compare():
    try:
        guess_num = int(text.get())
        if guess_num < set_num:
            print(messagebox.askokcancel('提示','太小了'))
        elif guess_num > set_num:
            print(messagebox.askokcancel('提示','太大了'))
        else:
            print(messagebox.askokcancel('提示','对了'))
    except:
        print(messagebox.askokcancel('提示','输入错误'))

def click():
    set_num=random.randint(1,100)
window = tk.Tk(className= '猜数字1-100')
width = 330
height = 300
screen_width = window.winfo_screenmmwidth()
screen_height = window.winfo_screenheight() #获取屏幕的宽度和长度
alignstr = '%dx%d+%d+%d' % (width, height, (screen_width - width) / 2, (screen_height - height) / 2)
window.geometry(alignstr)
window.resizable(width=False,height=True) #窗口是否可调True可变，False不可变
label = tk.Label(window,text='输入一个数1-100',bg='yellow').grid(row=0,column=1,ipadx=5,ipady=5)
#ipadx：设置控件里面水平方向空白区域大小,padx：设置控件周围水平方向空白区域保留大小
#label.pack() #可以简单理解为把label显示出来,pack和控件的布局排版有关
#grid()利用类似表格的组件排列方式
text = tk.StringVar()  #设置和接受输入框内容
text.set('')
entry = tk.Entry(window)
entry['textvariable']=text
entry.grid(row=0,column=5,ipadx=5,ipady=5) #textvariable可变文字
button1 = tk.Button(window,text='确定',command=check_and_compare).grid(row=1,column=5,ipadx=3,ipady=3,padx=5,pady=5)#padx,pady为x轴或者y轴所留白部分
button2 = tk.Button(window,text= '重新开始',command=click()).grid(row=1,column=1,ipadx=3,ipady=3,padx=5,pady=5)
window.mainloop()