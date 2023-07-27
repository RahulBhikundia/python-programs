from tkinter import *

root = Tk()

# gui logic

# Width x Height

root.title("Welcome to PyCharm Community Edition") 

root.geometry("624x234")

# width, height
root.minsize(300,100)

# width, height
root.maxsize(1200, 988)

pycharm_photo = PhotoImage(file="1.png")
label0 = Label(image=pycharm_photo,width=100,height=100)
label0.pack()

label1 = Label(text="PyCharm Community Edition",font=('Arial',20))
label1.pack()

label2 = Label(text="Version 2017.2",fg='#83838B')
label2.pack()

root.mainloop()