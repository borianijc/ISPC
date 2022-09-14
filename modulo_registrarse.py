from tkinter import *
from tkinter import messagebox

#---------------------------raiz------------------
#---------------------Ventana registrarse------------------
def ventana_registro_usuario():
       
    ventana_registro = Tk()
    ventana_registro.title("Registro de usuario")

    #----------imagenes-----------
    icono_panel="library.ico"                     
    imagen_fondo=PhotoImage(file="library_1767.png")

    #----------icono------------
    ventana_registro.iconbitmap(icono_panel)
    
    #ventana_registro.config(height=1000,width=1000)

    #-----------------------------frame y label imagen fondo---------------------
    #frame_imagen_registro=Frame(ventana_registro)
    #frame_imagen_registro.pack()
    
    #label_imagen_registro= Label(frame_imagen_registro, image=imagen_fondo)
    #label_imagen_registro.pack()

    #----------------------------frame - label y entry Registro de usuarios-----------------

    frame_registro=Frame(ventana_registro)
    frame_registro.pack()

    label_nombre= Label(frame_registro,text="Nombre:")
    label_nombre.grid(row=1,column=0,sticky=E,pady=10)

    entry_nombre= Entry (frame_registro)
    entry_nombre.grid(row=1,column=1,sticky=W)

    label_apellido= Label(frame_registro,text="Apellido:")
    label_apellido.grid(row=2,column=0,sticky=E,pady=10)

    entry_apellido= Entry (frame_registro)
    entry_apellido.grid(row=2,column=1,sticky=W)

    label_direccion= Label(frame_registro,text="Dirección:")
    label_direccion.grid(row=3,column=0,sticky=E,pady=10)

    entry_direccion= Entry (frame_registro)
    entry_direccion.grid(row=3,column=1,sticky=W)

    label_localidad= Label(frame_registro,text="Localidad:")
    label_localidad.grid(row=4,column=0,sticky=E,pady=10)

    entry_localidad= Entry (frame_registro)
    entry_localidad.grid(row=4,column=1,sticky=W)

    label_provincia= Label(frame_registro,text="Provincia:")
    label_provincia.grid(row=5,column=0,sticky=E,pady=10)

    entry_provincia= Entry (frame_registro)
    entry_provincia.grid(row=5,column=1,sticky=W)


    label_telefono= Label(frame_registro,text="Telefono:")
    label_telefono.grid(row=6,column=0,sticky=E,pady=10)

    entry_telefono= Entry (frame_registro)
    entry_telefono.grid(row=6,column=1,sticky=W)

    label_email= Label(frame_registro,text="E-mail:")
    label_email.grid(row=7,column=0,sticky=E,pady=10)

    entry_email= Entry (frame_registro)
    entry_email.grid(row=7,column=1,sticky=W)

    label_nombre_usuario= Label(frame_registro,text="Nombre de usuario: ")
    label_nombre_usuario.grid(row=9,column=0,sticky=E,pady=10)

    entry_nombre_usuario= Entry (frame_registro)
    entry_nombre_usuario.grid(row=9,column=1,sticky=W)

    label_password= Label(frame_registro,text="contraseña:")
    label_password.grid(row=18,column=0,sticky=E,pady=10)

    entry_password= Entry (frame_registro)
    entry_password.grid(row=18,column=1,sticky=W)
    entry_password.config(show="*")

    label_confirm_password= Label(frame_registro,text="Confirmar contraseña:")
    label_confirm_password.grid(row=19,column=0,sticky=E,pady=10)

    entry_confirm_password= Entry (frame_registro)
    entry_confirm_password.grid(row=19,column=1,sticky=W)
    entry_confirm_password.config(show="*")

    #---------------frame y botones registrarse/salir-----------
    frame_botones_regristro=Frame(ventana_registro)
    frame_botones_regristro.pack()
    
    boton_registrarse= Button(frame_registro,text="Aceptar",height=1,width=10)
    boton_registrarse.grid(row=20,column=0,padx=10,pady=10)

    boton_salir= Button(frame_registro,text="Salir",height=1,width=10, command= ventana_registro.destroy)
    boton_salir.grid(row=20,column=2,padx=10,pady=10)

    ventana_registro.mainloop()
