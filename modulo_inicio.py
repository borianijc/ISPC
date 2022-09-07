from tkinter import *
import class_fns
import imagenes

#---------------------------raiz------------------
ventana_inicio = Tk()

ventana_inicio.title("INICIO")

ventana_inicio.iconbitmap(imagenes.icono_panel)

w, h = ventana_inicio.winfo_screenwidth(), ventana_inicio.winfo_screenheight()
ventana_inicio.geometry("%dx%d+0+0" % (w, h))


#-----------------------------label fondo---------------------
#fondo_inicio=PhotoImage(file=imagenes.imagen_fondo)
#label_inicio= Label(ventana_inicio,image=fondo_inicio)
#label_inicio.grid(columnspan=3)

#----------------------------ingreso de usuarios-----------------
#label_usuario= Label(ventana_inicio,text="usuario: ")
#label_usuario.grid(row=8,column=0,sticky=E)

#entry_usuario= Entry (ventana_inicio)
#entry_usuario.grid(row=8,column=1,sticky=W)

#label_password= Label(ventana_inicio,text="contraseña: ")
#label_password.grid(row=9,column=0,sticky=E,pady=10)

#entry_password= Entry (ventana_inicio)
#entry_password.grid(row=9,column=1,sticky=W)
#entry_password.config(show="*")

#---------------Botones ingresar/registrarse/salir-----------
#boton_ingresar= Button(ventana_inicio,text="Ingresar",height=1,width=10,command=ingreso.ingreso_de_usuario(usuario_ingresado=entry_usuario,password_ingresado=entry_password))
#boton_ingresar.grid(row=10,column=0,padx=10,pady=10)

#boton_registrarse= Button(ventana_inicio,text="Registrarse",height=1,width=10)
#boton_registrarse.grid(row=10,column=1,padx=10,pady=10)

#boton_salir= Button(ventana_inicio,text="Salir",height=1,width=10)
#boton_salir.grid(row=10,column=2,padx=10,pady=10)


ventana_inicio.mainloop()
 