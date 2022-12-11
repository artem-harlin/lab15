from tkinter import *
from tkinter import ttk

root = Tk()
root.title("АВТОСЕРВИС")
root.geometry("230x200")

btn1 = ttk.Button(text = "Скидки")
btn1.pack(anchor = NW, fill = X, ipadx = 10, ipady = 10)

btn2 = ttk.Button(text = "Автомобили")
btn2.pack(anchor = NW)

btn3 = ttk.Button(text = "Марка")
btn3.pack(anchor = NW, ipadx = 5, ipady = 5)

btn4 = ttk.Button(text = "Список сотрудников")
btn4.pack(anchor = NW, fill = BOTH, expand = True)

root.mainloop()


