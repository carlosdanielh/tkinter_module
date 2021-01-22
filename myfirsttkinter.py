from tkinter import *
from time import sleep


def parpadear():
    windows.iconify()
    sleep(3)
    windows.deiconify()


def imprimir():
    windows.quit()
    windows2 = Tk()
    label_imprimir = Label(windows2,text='imprimir')
    button_exit2 = Button(windows2, text='salir', command=windows2.quit)
    label_imprimir.pack()
    button_exit2.pack()
    windows2.mainloop()


windows = Tk()
windows.geometry('400x200')
windows.title('my first tkinter')
label_one = Label(windows,text='esta es una etiqueta')
label_two = Label(windows,text='esta es otra etiqueta')
button_one = Button(windows, text='minimizar', command=windows.iconify)
button_two = Button(windows, text='parpadear', command=parpadear)
button_exit = Button(windows, text='salirrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr',fg='red', command=windows.quit)
button_imprimir = Button(windows, text='imprimir',fg='darkblue', command=imprimir)

button_imprimir.grid(row=0, column=1)
button_two.grid(row=1, column=1)
button_one.grid(row=2, column=1)
label_one.grid(row=3, column=2)
label_two.grid(row=4, column=2)
button_exit.grid(row=5, column=3)

print('this is a sample')
# button_two.pack(side=RIGHT)
# button_one.pack(side=LEFT)
# label_one.pack(side=RIGHT)
# label_two.pack(side=LEFT)
# button_exit.pack(side=RIGHT)



















windows.mainloop()