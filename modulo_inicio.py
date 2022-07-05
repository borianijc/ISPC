from tkinter import *

#-------------------------Funciones---------------

#---------------------fn salir------------

def fn_salir ():
    ventana_inicio.destroy()




#---------------------------raiz------------------
ventana_inicio = Tk()

ventana_inicio.title("INICIO")

ventana_inicio.iconbitmap("library.ico")

ventana_inicio.config(height=1500,width=1500)

#-----------------------------label fondo---------------------
fondo_inicio=PhotoImage(file="library_1767.png"),#height=1200,width=1200)
label_inicio= Label(ventana_inicio, image=fondo_inicio)
label_inicio.grid(sticky=N and W,columnspan=2)

#----------------------------ingreso de usuarios-----------------
label_usuario= Label(ventana_inicio,text="usuario: ")
label_usuario.grid(row=8,column=0,sticky=E)

entry_usuario= Entry (ventana_inicio)
entry_usuario.grid(row=8,column=1,sticky=W)

label_password= Label(ventana_inicio,text="contraseña: ")
label_password.grid(row=9,column=0,sticky=E)

entry_password= Entry (ventana_inicio)
entry_password.grid(row=9,column=1,sticky=W)

#---------------Botones ingresar/registrarse/salir-----------
boton_ingresar= Button(ventana_inicio,text="Ingresar")
boton_ingresar.grid(row=10,column=0,padx=10,pady=20,sticky=E)

boton_registrarse= Button(ventana_inicio,text="Registrarse")
boton_registrarse.grid(row=10,column=1,padx=10,pady=20)

boton_salir= Button(ventana_inicio,text="Salir",command=fn_salir)
boton_salir.grid(row=10,column=2,padx=10,pady=20,sticky=W)





ventana_inicio.mainloop()
 