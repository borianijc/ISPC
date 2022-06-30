from cProfile import label
from tkinter import *

ventana_inicio = Tk()

ventana_inicio.title("INICIO")
ventana_inicio.iconbitmap("Casa\library.ico")
ventana_inicio.config(height=1500,width=1500)

fondo_inicio=PhotoImage("Casa\library_1767.png")
label_inicio= Label(ventana_inicio, image=fondo_inicio)
label_inicio.grid(sticky=W)

ventana_inicio.mainloop()
 