import tkinter

class ventana_Tk:
    def __init__(self,titulo,icono):
        self.ventana= tkinter.Tk()
        self.ventana.config(height=1500,width=1500)
        self.titulo= self.ventana.title(titulo)
        self.icono= self.ventana.iconbitmap(icono)
        self.ventana.mainloop()

    def labels(self,dentro_de,titulo):
        self.label=tkinter.Label(dentro_de)
        self.label.config(height=300,width=300)
        self.label.grid(row=1,column=1)
        self.titulo= self.label(text=titulo)
            
    

ventana_inicio=ventana_Tk
ventana_inicio("Inicio","library.ico")
ventana_inicio.label(ventana_inicio,"Prueba")







        

