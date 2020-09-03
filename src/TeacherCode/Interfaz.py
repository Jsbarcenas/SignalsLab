from  tkinter import *
ventana = Tk()

ventana.title("ventana de pureba")
##ventana.resizable(True,False)
ventana.configure(bg= 'white',padx=4)
#ventana.geometry("700x400")
miFrame = Frame()
miFrame.pack()
miFrame.config(bd = '35')
miFrame.config(bg='red',width="700",height = "400", relief = 'sunken')
miFrame.config(cursor = 'hand2')
ventana.mainloop()