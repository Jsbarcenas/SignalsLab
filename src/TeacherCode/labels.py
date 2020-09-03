from tkinter import *
root = Tk()

root.geometry('700x400')
root.resizable(0,0)
frame = Frame(root, width = '680', height = '380' )
frame.pack()
frame.config(bd = '5', relief = 'sunken')
label = Label(frame, text = ' Hola, apenas he nacido')

label.place(x= 0, y=0)
label.grid(row = 1, column = 1)
root.mainloop()