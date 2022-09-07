from tkinter import *

class Aplicacion (Frame):
    def __init__(self, master:None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()