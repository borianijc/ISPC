from tkinter import *
from tkinter import messagebox #para ventanas emergentes



#-------------------------Funciones---------------

#---------------------fn salir------------

def fn_salir_aplicacion():
    salir=messagebox.askokcancel("Biblioteca","Desea salir de la aplicación?")
    #ask ok cancel es para carteles con opciones, se debe definir que accion toma el boton aceptar
    # aceptar devuelve True o False lo cual el resultado se guarda en una variable
    if salir == True:
        ventana_registro.destroy() 

#---------------------------raiz------------------
ventana_registro = Tk()

ventana_registro.title("REGISTRO DE USUARIOS")

ventana_registro.iconbitmap("library.ico")

ventana_registro.config(height=1500,width=1500)

#-----------------------------label fondo---------------------
#fondo_inicio=PhotoImage(file="Casa\library_1767.png"),#height=1200,width=1200"
#label_inicio= Label(ventana_inicio, image=fondo_inicio)
#label_inicio.grid(columnspan=3)

#----------------------------ingreso de usuarios-----------------
label_nombre= Label(ventana_registro,text="Nombre:")
label_nombre.grid(row=1,column=0,sticky=E,pady=10)

entry_nombre= Entry (ventana_registro)
entry_nombre.grid(row=1,column=1,sticky=W)

label_apellido= Label(ventana_registro,text="Apellido:")
label_apellido.grid(row=2,column=0,sticky=E,pady=10)

entry_apellido= Entry (ventana_registro)
entry_apellido.grid(row=2,column=1,sticky=W)

label_direccion= Label(ventana_registro,text="Dirección:")
label_direccion.grid(row=3,column=0,sticky=E,pady=10)

entry_direccion= Entry (ventana_registro)
entry_direccion.grid(row=3,column=1,sticky=W)

label_localidad= Label(ventana_registro,text="Localidad:")
label_localidad.grid(row=4,column=0,sticky=E,pady=10)

entry_localidad= Entry (ventana_registro)
entry_localidad.grid(row=4,column=1,sticky=W)

label_telefono= Label(ventana_registro,text="Telefono:")
label_telefono.grid(row=5,column=0,sticky=E,pady=10)

entry_telefono= Entry (ventana_registro)
entry_telefono.grid(row=5,column=1,sticky=W)

label_email= Label(ventana_registro,text="E-mail:")
label_email.grid(row=6,column=0,sticky=E,pady=10)

entry_email= Entry (ventana_registro)
entry_email.grid(row=6,column=1,sticky=W)

label_nombre_usuario= Label(ventana_registro,text="Nombre de usuario: ")
label_nombre_usuario.grid(row=8,column=0,sticky=E,pady=10)

entry_nombre_usuario= Entry (ventana_registro)
entry_nombre_usuario.grid(row=8,column=1,sticky=W)

label_password= Label(ventana_registro,text="contraseña:")
label_password.grid(row=18,column=0,sticky=E,pady=10)

entry_password= Entry (ventana_registro)
entry_password.grid(row=18,column=1,sticky=W)
entry_password.config(show="*")

#---------------Botones ingresar/registrarse/salir-----------
boton_ingresar= Button(ventana_registro,text="Ingresar",height=1,width=10)
boton_ingresar.grid(row=20,column=0,padx=10,pady=10)

boton_registrarse= Button(ventana_registro,text="Registrarse",height=1,width=10)
boton_registrarse.grid(row=20,column=1,padx=10,pady=10)

boton_salir= Button(ventana_registro,text="Salir",height=1,width=10, command=fn_salir_aplicacion)
boton_salir.grid(row=20,column=2,padx=10,pady=10)



ventana_registro.mainloop()
 