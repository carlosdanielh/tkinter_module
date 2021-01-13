import tkinter as tk


windows = tk.Tk()
frame = tk.Frame(windows, bg='black', width=400,height=400)
frame1 = tk.Frame(frame,width=100,height=100,bg='blue')
frame2 = tk.Frame(windows,bg='red')
windows.geometry('440x400')
# button1 = tk.Button(frame, text='button1', width=20)
# button2 = tk.Button(frame, text='button2', width=20)

button1 = tk.Button(windows, text='button1', width=30)
button2 = tk.Button(windows, text='button2', width=30)
# button3 = tk.Button(frame, text='button3', width=20)
# labelblue = tk.Label(windows, text='1111', font=('Arial', 20, 'bold'),bg='blue')
# label2 = tk.Label(windows, text='2222', font=('Arial', 16, 'bold'),bg='lightblue')
# # 
# button1.grid(column=0, row=0)
# button2.grid(column=1, row=0)

frame.grid(column=0, row=1, columnspan=2, pady=20) #grid(column=0, row=0)
frame1.grid(column=0, row=0)
# frame2.grid(column=1, row=0,sticky=tk.W+tk.E)
button1.grid(column=0, row=0)
button2.grid(column=1, row=0,padx=60)
# button3.grid(column=3, row=0,padx=80)
# labelblue.grid(column=1, row=1, columnspan=2, pady=10)
# label2.grid(column=1, row=1, sticky=tk.N)
windows.mainloop()


