from tkinter import *


def sayhi():    
    print(f'hi {name.get()} {middle_name.get()} {last_name.get()}')


windows = Tk()
windows.geometry('400x400')
windows.title('inputs Tkinter')
name = StringVar()
middle_name = StringVar()
last_name = StringVar()
name.set('write your name')


label1 = Label(windows, text='write your name')
name_box = Entry(windows, textvariable=name)

label2 = Label(windows, text='write your middle name')
middle_name_box = Entry(windows, textvariable=middle_name)

label3 = Label(windows, text='write your last name')
last_name_box = Entry(windows, textvariable=last_name)

button1 = Button(windows, text='custom hi', command=sayhi)

############################################
label1.place(x=10, y=10)
name_box.place(x=170, y=10)

label2.place(x=10, y=40)
middle_name_box.place(x=170, y=40)

label3.place(x=10, y=70)
last_name_box.place(x=170, y=70)

button1.place(x=10, y=100)
############################################
windows.mainloop()