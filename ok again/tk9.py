import tkinter as tk
from tkinter import ttk
from tkinter.tix import COLUMN

window=tk.Tk()
window.title('Combobox')
window.geometry('500x250')

ttk.Label(window, text="GFG Combobox Widget", background="green",foreground="white", font=("Times New Roman", 15)).grid(column=0,row=5,padx=10,pady=25)
ttk.Label(window, text="Select the month:", font=("Times New Roman", 10)).grid(column=0,row=5,padx=10,pady=25)

n=tk.StringVar()
month_chosen=ttk.Combobox(window, width=27, textvariable=n)

month_chosen['values']=('January','February','March','April','May','June','July','August','September','October','November','December')
month_chosen.grid(column=1,row=5)
month_chosen.current()

window.mainloop()