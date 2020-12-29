from tkinter import *
import os


def sayhi():
    print(f'hi {name.get()} {middle_name.get()} {last_name.get()}')


os.system('cls')
windows = Tk()
windows.geometry('400x400+400+150')
windows.title('inputs Tkinter')
name = StringVar()
middle_name = StringVar()
last_name = StringVar()
age = IntVar()
sex = StringVar()
name.set('write your name')
sex.set('M/F')


label1 = Label(windows, text='write your name')
name_box = Entry(windows, textvariable=name)

label2 = Label(windows, text='write your middle name')
middle_name_box = Entry(windows, textvariable=middle_name)

label3 = Label(windows, text='write your last name')
last_name_box = Entry(windows, textvariable=last_name)

label_age = Label(windows, text='Age: ')
age_box = Entry(windows, textvariable=age)

label_sex = Label(windows, text='Sex: ')
sex_box = Entry(windows, textvariable=sex)

button1 = Button(windows, text='custom hi', command=sayhi)

############################################
label1.place(x=10, y=10)
name_box.place(x=170, y=10)

label2.place(x=10, y=40)
middle_name_box.place(x=170, y=40)

label3.place(x=10, y=70)
last_name_box.place(x=170, y=70)

label_age.place(x=10, y=100)
age_box.place(x=45, y=100)

label_sex.place(x=10, y=130)
sex_box.place(x=45, y=130)

button1.place(x=10, y=160)
############################################
windows.mainloop()