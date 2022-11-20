from tkinter import *

root = Tk()
root.title('간단한 계산기')
# root.geometry('300x400+800+100')

entry = Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

def btn_click(number):
    current = entry.get()  # 입력값 얻기
    entry.delete(0, END)  # 입력값 지우기
    entry.insert(0, str(current) + str(number))  # 얻은 입력값에 새로운 값 붙이기
    return

def content_clear():
    entry.delete(0, END)

def content_add():
    first_number = entry.get()
    global f_num
    global math
    math = 'add'
    f_num = int(first_number)
    entry.delete(0, END)

def content_sub():
    first_number = entry.get()
    global f_num
    global math
    math = 'sub'    
    f_num = int(first_number)
    entry.delete(0, END)

def content_mul():
    first_number = entry.get()
    global f_num
    global math
    math = 'mul'    
    f_num = int(first_number)
    entry.delete(0, END)

def content_div():
    first_number = entry.get()
    global f_num
    global math
    math = 'div'    
    f_num = int(first_number)
    entry.delete(0, END)

def contetn_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if math == 'add':
        entry.insert(0, f_num + int(second_number))
    if math == 'sub':
        entry.insert(0, f_num - int(second_number))
    if math == 'mul':
        entry.insert(0, f_num * int(second_number))
    if math == 'div':
        entry.insert(0, f_num / int(second_number))                

button1 = Button(root, text='1', padx=30, pady=20, command=lambda: btn_click(1))
button2 = Button(root, text='2', padx=30, pady=20, command=lambda: btn_click(2))
button3 = Button(root, text='3', padx=30, pady=20, command=lambda: btn_click(3))
button4 = Button(root, text='4', padx=30, pady=20, command=lambda: btn_click(4))
button5 = Button(root, text='5', padx=30, pady=20, command=lambda: btn_click(5))
button6 = Button(root, text='6', padx=30, pady=20, command=lambda: btn_click(6))
button7 = Button(root, text='7', padx=30, pady=20, command=lambda: btn_click(7))
button8 = Button(root, text='8', padx=30, pady=20, command=lambda: btn_click(8))
button9 = Button(root, text='9', padx=30, pady=20, command=lambda: btn_click(9))
button0 = Button(root, text='0', padx=30, pady=20, command=lambda: btn_click(0))

btn_add = Button(root, text='+', padx=30, pady=20, command=content_add)
btn_sub = Button(root, text='-', padx=30, pady=20, command=content_sub)
btn_mul = Button(root, text='x', padx=30, pady=20, command=content_mul)
btn_div = Button(root, text='÷', padx=30, pady=20, command=content_div)
btn_equal = Button(root, text='=', padx=30, pady=20, command=contetn_equal)
btn_clear = Button(root, text='C', padx=30, pady=20, command=content_clear)

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
btn_add.grid(row=1, column=3)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
btn_sub.grid(row=2, column=3)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
btn_mul.grid(row=3, column=3)

button0.grid(row=4, column=0)
btn_clear.grid(row=4, column=1)
btn_equal.grid(row=4, column=2)
btn_div.grid(row=4, column=3)

mainloop()