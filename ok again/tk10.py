import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.geometry('350x250')

ttk.Label(window, text="Select the month:", font=("Times New Roman",10)).grid(column=0,row=15,padx=10,pady=25)
n=tk.StringVar()

month_chosen=ttk.Combobox(window, width=27, textvariable=n)
month_chosen['values']=('January','February','March','April','May','June','July','August','September','October','November','December')
month_chosen.grid(column=1,row=15)

window.mainloop()

