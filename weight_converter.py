from tkinter import *

w = Tk()
w.title("Weight Converter")
w.resizable(0, 0)

def kg():
    gram = float(c.get())*1000
    tonne = float(c.get())*0.001
    pound = float(c.get())*2.20462
    ounce = float(c.get())*35.274
    v1.delete("1.0", END)
    v1.insert(END, gram)
    v2.delete("1.0", END)
    v2.insert(END, tonne)
    v3.delete("1.0", END)
    v3.insert(END, pound)
    v4.delete("1.0", END)
    v4.insert(END, ounce)

def clear():
    c1.delete(0, END)
    v1.delete("1.0", END)
    v2.delete("1.0", END)
    v3.delete("1.0", END)
    v4.delete("1.0", END)

l = Label(w, text="Enter the weight in Kg")
c = StringVar()
c1 = Entry(w, textvariable=c)
c2 = Label(w, text="Gram")
c3 = Label(w, text="Tonne")
c4 = Label(w, text="Pound")
c5 = Label(w, text="Ounce")

v1 = Text(w, height=5, width=20)
v2 = Text(w, height=5, width=20)
v3 = Text(w, height=5, width=20)
v4 = Text(w, height=5, width=20)

b = Button(w, text="Convert", command=kg)
b1 = Button(w, text="Clear", command=clear)

l.grid(row=0, column=0)
c1.grid(row=0, column=1)
c2.grid(row=1, column=0)
c3.grid(row=1, column=1)
c4.grid(row=1, column=2)
c5.grid(row=1, column=3)
v1.grid(row=2, column=0)
v2.grid(row=2, column=1)
v3.grid(row=2, column=2)
v4.grid(row=2, column=3)

b.grid(row=0, column=2)
b1.grid(row=0, column=3)

w.mainloop()