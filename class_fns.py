from tkinter import *
from tkinter import messagebox

#---------------------Frame---------------

class Frames_de_Trabajo:
    def __init__(self, ubicacion):
        self.frame = ubicación = Frame()
        self.frame.config(height=300,width=300)
        self.frame.pack(expand=True,fill="both")

class Label_de_Trabajo (Frames_de_Trabajo):
    def __init__(self, ubicacion):
        super().__init__(Label)
    def __init__(self,label):
        self.label= Label()
        self.label.pack(expand=True,fill="both")
        self.imagen_label=Label(image=None)

#-----------------ingreso de usuario------------------------

class Ingreso:
    def ingreso_de_usuario(usuario_ingresado,password_ingresado):
        usuario_ingresado.get()
        password_ingresado.get()
        print(usuario_ingresado)
        print(password_ingresado)
