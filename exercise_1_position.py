from tkinter import *


def sayhi():
    print('hiiiii')


windows = Tk()
windows.geometry('400x200')
windows.title('my first exercise')

label1 = Label(windows, text='from here we say Hi')
button1 = Button(windows, text='click on me to say HI',command=sayhi)

label2 = Label(windows, text='from here we mimisize')
button2 = Button(windows, text='click on me to say HI',command=windows.iconify)


label1.place(x=30, y=66)
button1.place(x=200, y=66)
label2.place(x=30, y=132)
button2.place(x=200, y=132)
# label1.pack(side=LEFT)
# button1.pack(side=RIGHT)
# label2.pack(side=LEFT)
# button2.pack(side=RIGHT)

# label1.grid(row=1,column=0)
# button1.grid(row=1,column=1)
# label2.grid(row=4,column=0)
# button2.grid(row=4,column=1)

windows.mainloop()