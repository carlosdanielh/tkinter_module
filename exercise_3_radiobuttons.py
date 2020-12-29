from tkinter import *

windows = Tk()
windows.title('Radio buttons Tkinter')
windows.geometry('400x400+400+200')

number = IntVar()
number.set('integer')
option = IntVar()

label_integer = Label(windows,text='write your number: ')
integer_box = Entry(windows,textvariable=number)

label_option = Label(windows,text='Write your option: ')
x10 = Radiobutton(windows,text='x10', value=1, variable=option)
x20 = Radiobutton(windows,text='x20', value=2, variable=option)
x30 = Radiobutton(windows,text='x30', value=3, variable=option)
x40 = Radiobutton(windows,text='x40', value=4, variable=option)
x50 = Radiobutton(windows,text='x50', value=5, variable=option)
square = Radiobutton(windows,text='square', value=6, variable=option)
operation_button = Button(windows, text='Operation', fg='grey', bg='black')

# #############################################################################

label_integer.place(x=10, y=10)
integer_box.place(x=120, y=10 )

label_option.place(x=10 , y=40)
x10.place(x=10 , y=70)
x20.place(x=50 , y=70)
x30.place(x=90 , y=70)
x40.place(x=10 , y=100)
x50.place(x=50 , y=100)
square.place(x=90 , y=100)
operation_button.place(x=10 , y=130)

# #############################################################################
windows.mainloop()
