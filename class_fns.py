from cgitb import text
from tkinter import *

#---------------------Frame---------------

class Frames_de_Trabajo(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master      #donde va a estar ubicado el frame
        #self.crear_label()        #fn para crear label
        #self.crear_botones()      #fn para crear botones 
        #self.crear_entry()        #fn para crear entry
        self.pack()               #empaquetado
        #self.frame.pack(expand=True,fill="both")      #para que se expanda con la pantalla  

class Label_de_Trabajo(Label):
    def __init__ (self,master=None):
        super().__init__(master)
        self.master=master    
        self.nuevo_label= Label(self)
        
        self.nuevo_label.pack()
    
class Botones_de_Trabajo (Button):
    def __init__(self):
        self.nuevo_boton= Button(self)
        self.nuevo_boton ["text"] = "Hola"
        self.nuevo_boton.pack(side="top")
   

#-----------------ingreso de usuario------------------------

#class Ingreso:
#    def ingreso_de_usuario(usuario_ingresado,password_ingresado):
#        usuario_ingresado.get()
#        password_ingresado.get()
#        print(usuario_ingresado)
#        print(password_ingresado)

