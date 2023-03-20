from tkinter import *
from tkinter import messagebox
def button_1():
    messagebox.showinfo('Результат', int(a.get())+int(b.get()))
def button_2():
    messagebox.showinfo('Результат', int(a.get())*int(b.get()))
def button_3():
    messagebox.showinfo('Результат', int(a.get())//int(b.get()))
def button_4():
    messagebox.showinfo('Результат', int(a.get())-int(b.get()))
def button_5():
    messagebox.showinfo('Результат', int(a.get())%int(b.get()))

root=Tk()
root.title('Калькулятор')
root.geometry('700x600')
a=Entry(root, width=20,  bg='#D3D3D3', fg='#696969', font=('Purisa',30,'bold italic'))
a.pack()
b=Entry(root, width=20,  bg='#D3D3D3', fg='#696969', font=('Purisa',30,'bold italic'))
b.pack()

Button(root, text='+', width=20, height=3, bg="#FFDAB9", 
	 command=button_1).pack()
Button(root, text='*', width=20, height=3, bg="#FFDAB9", 
	 command=button_2).pack()
Button(root, text='//', width=20, height=3, bg="#FFDAB9", 
	 command=button_3).pack()
Button(root, text='-', width=20, height=3, bg="#FFDAB9", 
	 command=button_4).pack()
Button(root, text='%', width=20, height=3, bg="#FFDAB9", 
	 command=button_5).pack()
root.mainloop()

