import tkinter as tk

root=tk.Tk()
root.geometry('600x400')

name_var=tk.StringVar()
password_var=tk.StringVar()

def submit():
    name=name_var.get()
    password=password_var.get()
    print("The name is:" +name)
    print("The password is:" +password)
    name_var.set("")
    password_var.set("")

name_label=tk.Label(root, text="Username", font=("Calibre",10,"bold"))
password_label=tk.Label(root, text="Password", font=("Calibre",10,"bold"))

name_entry=tk.Entry(root, textvariable=name_var, font=("Calibre",10,"bold"))
password_entry=tk.Entry(root, textvariable=password_var, font=("Calibre",10,"bold"), show='*')
sub_btn=tk.Button(root, text="Submit", command="submit")

name_label.grid(column=0, row=0)
name_entry.grid(column=0, row=0)
password_label.grid(column=0, row=1)
password_entry.grid(column=1, row=1)
sub_btn.grid(row=2, column=1)

root.mainloop()