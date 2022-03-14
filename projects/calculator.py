from tkinter import*

def sum1():
    x=int(e1.get())
    y=int(e2.get())
    z=x+y
    ans.set("ans is" + str(z))

def sub():
    x=int(e1.get())
    y=int(e2.get())
    z=x-y
    ans.set("ans is" + str(z))

def mult():
    x=int(e1.get())
    y=int(e2.get())
    z=x*y
    ans.set("ans is:"+str(z))

def div():
    x=int(e1.get())
    y=int(e2.get())
    z=x/y
    ans.set("ans is" +str(z))

top=Tk()
ans=StringVar()
top.title("Window")
top.config(background='orange')
top.geometry("500x600+10+10")
top.resizable(0,0)

Label(top, text="calculator", fg='red', bg='pink', font=('Arial',46)).pack()
Label(top, text='Enter first value', fg='white', bg='red', font=('Arial',16)).place(x=10, y=100)
Label(top, text='Enter secong value', fg='white', bg='red', font=('Arial', 16)).place(x=10,y=150)

e1=Entry(top)
e1.place(x=200, y=100)
e2=Entry(top)
e2.place(x=200,y=150)

Button(top, text='Sum', fg='red', command=sum1).place(x=50, y=250)
Button(top, text='Sub', fg='red', command=sub).place(x=100,y=250)
Button(top, text='Multiply', fg='red',command=mult).place(x=150,y=250)
Button(top, text='Divide', fg='red', command=div).place(x=225, y=250)

Label(top, textvariable=ans, fg='white', bg='blue', font=('Arial', 16)).place(x=80, y=300)
top.mainloop()