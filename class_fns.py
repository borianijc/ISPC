from typing_extensions import Self


class funciones:
    def limpiar_campos_inicio(self):
        self.entry_usuario.set("")
        self.entry_contraseña.set("")
     
    def limpiar_campos_registro(self):
        
        self.entry_nombre.set("")
        self.entry_apellido.set("")
        self.entry_direccion.set("")
        self.entry_localidad.set("")
        self.entry_telefono.set("")
        self.entry_email.set("")
        self.entry_nombre_usuario.set("")
        self.entry_password.set("")


        
limpiar_campos_registro=funciones()
