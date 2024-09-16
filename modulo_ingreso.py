from tkinter import *
from tkinter import messagebox
        
#----------Ventana Ingreso Usuarios--------------
def ingreso ():
    ventana_ingreso = Tk()                       
    ventana_ingreso.title("Ingreso de Usuario")    

    #----------imagenes-----------
    icono_panel="Casa\library.ico"                     
    imagen_fondo=PhotoImage(file="Casa\library_1767.png")

    #-----------icono ventana ingreso------------
    ventana_ingreso.iconbitmap(icono_panel)
#------------------------Variables para cerificar usuarios--------------------------
    usuario_cargado=StringVar()
    password_cargada=StringVar()
#-----------------------------fn control de usuario-----------------
    def control_de_usuario():
        if usuario_cargado.get() == "1":
            pass
        if password_cargada.get() == "1":
            pass
        else:
            messagebox.showwarning("Biblioteca","Usuario no Registrado")
            password_cargada.set("")
            usuario_cargado.set("")

#-------------fn salir------------
    def salir_aplicacion():
        salir=messagebox.askokcancel("Bilioteca","Desea salir de la aplicación?")
        if salir == True:
            ventana_ingreso.destroy()         

    #-------Frame imagen-------------
    frame_imagen=Frame(ventana_ingreso)
    frame_imagen.config(height=300,width=300)
    frame_imagen.pack()

    #--------Label imagen-------------
    label_imagen=Label(frame_imagen,image=imagen_fondo)
    label_imagen.pack()

    #----------------------------ingreso de usuarios-----------------
    #----------------------------frame - label - entry ---------------
    frame_ingreso=Frame(ventana_ingreso)
    frame_ingreso.pack()

    label_usuario= Label(frame_ingreso,text="usuario: ")
    label_usuario.grid(row=8,column=0,sticky=E)

    entry_usuario= Entry (frame_ingreso,textvariable=usuario_cargado)
    entry_usuario.grid(row=8,column=1,sticky=W)
    
    label_password= Label(frame_ingreso,text="contraseña: ")
    label_password.grid(row=9,column=0,sticky=E,pady=10)

    entry_password= Entry (frame_ingreso,textvariable=password_cargada)
    entry_password.grid(row=9,column=1,sticky=W)
    entry_password.config(show="*")
 
    #----------------------------Botones---------------------
    #--------------------------frame - boton-----------------
    frame_botones=Frame(ventana_ingreso)
    frame_botones.pack()  

    boton_aceptar=Button(frame_botones,text="Aceptar",command=control_de_usuario)
    boton_aceptar.grid(row=1,column=0,padx=10,pady=5)
    
    boton_registrarse=Button(frame_botones,text="Registrarse",command=ventana_registro_usuario)
    boton_registrarse.grid(row=1,column=1,padx=10,pady=5)
    
    boton_salir= Button(frame_botones,text="Salir",command=salir_aplicacion)
    boton_salir.grid(row=1,column=2,padx=10,pady=5)

#----fin de ventana ingreso-----------
    ventana_ingreso.mainloop()

ingreso()