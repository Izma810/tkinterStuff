import tkinter as tk

root=tk.Tk()
root.geometry('250x170')

T=tk.Text(root, height=5,width=52)
L=tk.Label(root, text="Fact of the Day")
L.config(font=("Courier", 14))

Fact="A man ca be arrested in Italy for wearing a skirt in public"

b1=tk.Button(root, text="Next")
b2=tk.Button(root, text="Exit",command=root.destroy)

L.pack()
T.pack()
b1.pack()
b2.pack()

T.insert(tk.END, Fact)

tk.mainloop()

