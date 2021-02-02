import tkinter as tk
from tkinter import messagebox as msg
from time import sleep


FONT_RESULT = ('Arial', 15, 'bold')
menu_radio = {key + 1: value for key, value in enumerate(range(10, 60, 10))}


# ------------------------------ Operation -----------------------------------#
def operation():
    check()
    if integer_box.get().isdigit():
        label_result.grid()
        
        number = int(integer_box.get())
        if option.get() < 6:
            value_to_multiply = menu_radio[option.get()]
            label_result.configure(text=f'{number * value_to_multiply}')
        elif option.get() == 6:
            label_result.configure(text=f'{number ** 2}')
    else:
        msg.showinfo('info', 'is no numerical')


# ------------------------------ check windows -------------------------------#
def check():
    id = windows.after(100, check)
    if len(integer_box.get()) == 0:
        label_result.grid_forget()
        windows.after_cancel(id)


# --------------------------------- UI ---------------------------------------#
windows = tk.Tk()
windows.title('Radio buttons Tkinter')
windows.geometry('259x300+400+200')
windows.configure(bg='gray')


# --------------------------------- Frames -----------------------------------#
frame_top = tk.Frame(windows)
frame_top.pack(pady=10)

label_frame = tk.LabelFrame(text='Option', width=200, height=100)
label_frame.grid_propagate(0)
label_frame.pack()

frame_bottom = tk.Frame()
frame_bottom.pack(pady=10)
# --------------------------------- Widget's variables -----------------------#
number = tk.IntVar()
# number.set('integer')
option = tk.IntVar()
# --------------------------------- Labels -----------------------------------#
label_integer = tk.Label(frame_top, text='Number: ')
label_integer.grid(column=0, row=0)

label_result = tk.Label(frame_bottom, width=25, bg='red', font=FONT_RESULT)
label_result.grid(column=0, row=1, pady=15)
label_result.grid_forget()
# --------------------------------- Entry ------------------------------------#
integer_box = tk.Entry(frame_top, textvariable=number, width=23)
integer_box.grid(column=1, row=0)
integer_box.focus_set()

# --------------------------------- Radios -----------------------------------#
x10 = tk.Radiobutton(label_frame, text='x10', value=1, variable=option)
x10.grid(column=0, row=2)

x20 = tk.Radiobutton(label_frame, text='x20', value=2, variable=option)
x20.grid(column=1, row=2)

x30 = tk.Radiobutton(label_frame, text='x30', value=3, variable=option)
x30.grid(column=2, row=2)

x40 = tk.Radiobutton(label_frame, text='x40', value=4, variable=option)
x40.grid(column=0, row=3)

x50 = tk.Radiobutton(label_frame, text='x50', value=5, variable=option)
x50.grid(column=1, row=3)

square = tk.Radiobutton(label_frame, text='square', value=6, variable=option)
square.grid(column=0, row=4, columnspan=3, sticky=tk.W)

# --------------------------------- Button -----------------------------------#
operation_button = tk.Button(frame_bottom, text='Operation', fg='grey',
                             bg='black',
                             command=operation)
operation_button.grid(column=0, row=0, sticky=tk.W)

windows.resizable(False, False)
windows.mainloop()
