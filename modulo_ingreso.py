from tkinter import *
import imagenes
from class_fns import Frames_de_Trabajo, Label_de_Trabajo


#----------Ventana Ingreso Usuarios--------------

ventana_ingreso = Tk()
ventana_ingreso.title("Ingreso de Usuario")
ventana_ingreso.iconbitmap(imagenes.icono_panel)

#-------Frame imagen-------------
frame_imagen=Frames_de_Trabajo(ventana_ingreso)

#--------Label imagen-------------
label_imagen=Label_de_Trabajo(label=frame_imagen)
label_imagen.imagen_label(imagenes.imagen_fondo)










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