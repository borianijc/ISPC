from tkinter import *
from tkinter import messagebox


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

#---------------------Label------------------
class Label_de_Trabajo(Label):
    def __init__ (self,master=None):
        super().__init__(master)
        self.master=master    
        self.nuevo_label= Label(self)
        
        self.nuevo_label.pack()

#-----------------------Botones-----------------    
class Botones_de_Trabajo (Button):
    def __init__ (self,master=None):
        texto=None
        fn=None
        self.master=master
        self.nuevo_boton= Button(self,height=10,width=10,padx=10,pady=5)
        self.nuevo_boton ["text"] = texto
        self.nuevo_boton ["command"]=fn
        self.nuevo_boton.pack()

#------------------------class  Funciones ----------------
#--------------fn salir---------
class Salir:
    def __init__(self,master):
        master=master
    def salir_aplicacion(master):
        salir=messagebox.askokcancel("Metalplast","Desea salir de la aplicación?")
        if salir == True:
            master.o 
            
#-----------------ingreso de usuario------------------------

#class Ingreso:
#    def ingreso_de_usuario(usuario_ingresado,password_ingresado):
#        usuario_ingresado.get()
#        password_ingresado.get()
#        print(usuario_ingresado)
#        print(password_ingresado)

