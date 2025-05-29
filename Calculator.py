import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

win = tk.Tk()
win.title('Calculator')

frame = tk.Frame(win, bg="black", padx=70)
frame.pack()

entry = tk.Entry(frame, relief=SUNKEN, borderwidth=10, width=100)
entry.grid(row=0, column=0, columnspan=50, ipady=30, pady=10)

def click(num):
    entry.insert(tk.END, num)

def equal():
    try:
        res = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, res)
    except:
        tk.messagebox.showinfo("Error", "Syntax Error")

def clear():
    entry.delete(0, tk.END)

buttons = [
    ('1', 1, 2), ('2', 1, 3), ('3', 1, 4),
    ('4', 2, 2), ('5', 2, 3), ('6', 2, 4),
    ('7', 3, 2), ('8', 3, 3), ('9', 3, 4),
    ('0', 4, 3), ('+', 5, 1), ('-', 5, 2),
    ('*', 5, 3), ('/', 5, 4), ('%', 5, 5),
]

for txt, r, c in buttons:
    tk.Button(frame, text=txt, padx=30, pady=20, width=10, command=lambda t=txt: click(t)).grid(row=r, column=c, pady=7)

tk.Button(frame, text="Clear", padx=20, pady=10, width=17, command=clear).grid(row=7, column=2, columnspan=2, pady=3)
tk.Button(frame, text="=", padx=20, pady=10, width=15, command=equal).grid(row=7, column=4, columnspan=2, pady=3)

win.mainloop()
