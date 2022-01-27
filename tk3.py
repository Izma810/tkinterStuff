from tkinter import*
from tkinter.ttk import*

root=Tk()
root.geometry('100x100')
btn=Button(root,text="Click me!",command=root.destroy)
btn.pack(side='top')

root.mainloop()


