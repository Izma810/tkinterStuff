from tkinter import*

root=Tk()
root.geometry('150x200')

w=Label(root, text='GeeksForGeeks', font='50')
w.pack()

scroll_bar=Scrollbar(root)
scroll_bar.pack(side=RIGHT, fill=Y)

my_list=Listbox(root, yscrollcommand=scroll_bar.set)
for line in range(1, 26):
    my_list.insert(END, 'Geeks'+str(line))
    my_list.pack(side=LEFT, fill=BOTH)
    scroll_bar.config(command=my_list.yview)

root.mainloop()