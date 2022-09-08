from tkinter import *

#from imagenes import *
#from class_fns import Frames_de_Trabajo, Label_de_Trabajo

icono_panel="library.ico"

imagen_fondo=PhotoImage(file="library_1767.png")
 
#----------Ventana Ingreso Usuarios--------------

ventana_ingreso = Tk()
ventana_ingreso.title("Ingreso de Usuario")
ventana_ingreso.iconbitmap(icono_panel)

#-------Frame imagen-------------
frame_imagen=Frame(ventana_ingreso)
frame_imagen.config(height=300,width=300)
frame_imagen.pack()
#--------Label imagen-------------
label_imagen=Label(frame_imagen,image=imagen_fondo)
label_imagen.pack()


ventana_ingreso.mainloop()



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