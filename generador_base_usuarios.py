import sqlite3
from tkinter import messagebox 

def crear_base_usuario():
    
    conexion=sqlite3.connect("Base_usuarios")
    
# cursor para conexion

    cursor_base_usuarios=conexion.cursor()
#------------------ejecuta el create para crear la tabla USUARIOS_BIBLIOTECA-----------
    try:
        cursor_base_usuarios.execute('''CREATE TABLE USUARIOS_BIBLIOTECA (
            ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            NOMBRES VARCHAR (20), 
            APELLIDO VARCHAR (20),
            DIRECCION VARCHAR (20),
            LOCALIDAD VARCHAR (20),
            TELEFONO INTEGER (10),
            EMAIL VARCHAR (30),  
            USUARIO VARCHAR (10) UNIQUE,
            CONTRASEÑA VARCHAR (10),
            TIPO_USUARIO (15)
            ) ''')
        messagebox.showinfo("BIBLIOTECA", "La base de datos fue creada con exito")
    except:
        messagebox.showwarning("Atención", "La base de datos ya fue creada")

#------------------Hasta aca fue editado 06/07/2022


#def limpiar_campos():
#    my_ID.set("")
#    my_name.set("")
#    my_surname.set("")
#    my_usuarname.set("")
#    my_password.set("")


# ------------------------------------funcion para cargar los datos de nuevo usuario a la BBDD---------------
def nuevo_usuario():
    cargar_usuario= (my_name.get(),my_surname.get(),my_usuarname.get(),my_password.get(),text_comentarios.get("1.0",END)) 
    
    conexion=sqlite3.connect("Base_usuarios_MP")

    my_cursor=conexion.cursor()
    
    my_cursor.execute ("INSERT INTO USUARIOS_MP VALUES (NULL,?,?,?,?,?)", cargar_usuario)

    conexion.commit()

    limpiar_campos()

    messagebox.showinfo("Metalpalst","Usuario Registrado con exito!")

# -------------------------------------funcion para leer datos de la BBDD---------------------------------------

def datos_usuarios():
    
    conexion=sqlite3.connect("Base_usuarios_MP")

    my_cursor=conexion.cursor()

    my_cursor.execute("SELECT * FROM USUARIOS_MP WHERE ID=" + my_ID.get())

    usuario_buscado=my_cursor.fetchall()

    if usuario_buscado == []:
        messagebox.showwarning("Metalplast","Usuario no registrado")
        limpiar_campos()
    else:
# bucle for para que busque el ID y carge los datos en los entry
# for usuario in usuario_buscado:
        for usuario in usuario_buscado:
            my_ID.set(usuario[0])
            my_name.set(usuario[1])
            my_surname.set(usuario[2])
            my_usuarname.set(usuario[3])
            my_password.set(usuario[4])
            text_comentarios.insert("1.0",usuario[5])

    conexion.commit()

# --------------------------------------------funcion actualizar datos de usuario---------------------
def actualizar_datos_usuario():

    conexion=sqlite3.connect("Base_usuarios_MP")

    my_cursor=conexion.cursor()

# instruccion para actualizar info en la BBDD
#    my_cursor.execute("UPDATE USUARIOS_MP SET NOMBRE='"+ my_name.get() +
#        "', APELLIDO= '" + my_surname.get() +
#        "', USUARIO= '" + my_usuarname.get() +
#        "', CONTRASEÑA= '" + my_password.get() +
#        "', COMENTARIO= '" + text_comentarios.get("1.0",END) +
#        "' WHERE ID=" + my_ID.get())

# otra forma puede ser 

    datos_actualizados=(my_name.get(),my_surname.get(),my_usuarname.get(),my_password.get(),text_comentarios.get("1.0",END))
    
    my_cursor.execute("UPDATE USUARIOS_MP SET NOMBRE=?,APELLIDO=?,USUARIO=?,CONTRASEÑA=?,COMENTARIO=?" + "WHERE ID=" + my_ID.get(),datos_actualizados)
    
    conexion.commit()

    limpiar_campos()

    messagebox.showinfo("Metalplast","Datos del usuario actualizado")

def borrar_registro ():
    
    conexion=sqlite3.connect("Base_usuarios_MP")

    my_cursor=conexion.cursor()

    my_cursor.execute("DELETE FROM USUARIOS_MP WHERE ID=" + my_ID.get())

    conexion.commit()

    limpiar_campos()

    messagebox.showinfo("Metalplast","Usuario eliminado")