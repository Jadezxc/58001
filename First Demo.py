from tkinter import *
window = Tk()
window.geometry("500x400+10+10")
window.title("my First GUI")

btn1 = Button(window, text = "Click me!", fg = "Red", bg="Yellow")
btn1.place(x=200, y=200)
txtfld = Entry(window, border=2.50)
txtfld.place(x=180,y=150)

lbl = Label(window, text= "My First Demo")
lbl.place(x=1800,y=50)


window.mainloop()