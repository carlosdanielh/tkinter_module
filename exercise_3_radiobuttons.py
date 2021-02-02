import tkinter as tk

menu_radio = {key + 1: value for key, value in enumerate(range(10, 60, 10))}


# ------------------------------ Operation -----------------------------------#
def operation():
    number = int(integer_box.get())
    if option.get() < 6:
        value_to_multiply = menu_radio[option.get()]
        print(f'{number} * {value_to_multiply} = {number * value_to_multiply}')
    elif option.get() == 6:
        print(f'square{number} = {number ** 2}')
# --------------------------------- UI ---------------------------------------#


windows = tk.Tk()
windows.title('Radio buttons Tkinter')
windows.geometry('400x400+400+200')

number = tk.IntVar()
number.set('integer')
option = tk.IntVar()
# --------------------------------- Labels -----------------------------------#
label_integer = tk.Label(windows, text='write your number: ')
label_integer.grid(column=0, row=0)

integer_box = tk.Entry(windows, textvariable=number)
integer_box.grid(column=1, row=0)

label_option = tk.Label(windows, text='Write your option: ')
label_option.grid(column=0, row=1)

# --------------------------------- Radios -----------------------------------#
x10 = tk.Radiobutton(windows, text='x10', value=1, variable=option)
x10.grid(column=0, row=2)

x20 = tk.Radiobutton(windows, text='x20', value=2, variable=option)
x20.grid(column=1, row=2)

x30 = tk.Radiobutton(windows, text='x30', value=3, variable=option)
x30.grid(column=2, row=2)

x40 = tk.Radiobutton(windows, text='x40', value=4, variable=option)
x40.grid(column=0, row=3)

x50 = tk.Radiobutton(windows, text='x50', value=5, variable=option)
x50.grid(column=1, row=3)

square = tk.Radiobutton(windows, text='square', value=6, variable=option)
square.grid(column=2, row=3)

# --------------------------------- Button -----------------------------------#
operation_button = tk.Button(windows, text='Operation', fg='grey', bg='black',
                             command=operation)
operation_button.grid(column=0, row=4)


windows.mainloop()
