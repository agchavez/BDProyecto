from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style
from tkinter import Tk
import tkinter as tk
from tkinter import messagebox
from Core.proyecto import *
from Core.User import *
from Core.MySQLEngine import *

import configparser

class LoginInit:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.iconbitmap(r'Codigo/iconoAPP.ico')
        self.colorFondo = "#222222"
        self.colorLetra = "#FFF"
        ancho_ventana = 750
        alto_ventana = 550
        x_ventana = self.ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.ventana.winfo_screenheight() // 2 - alto_ventana // 2
        self.ventana.configure(background=self.colorFondo)
        s = Style()
        s.configure ('My.TFrame', background = self.colorFondo, foreground=self.colorLetra)
        self.posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.usuario = StringVar()
        self.password = StringVar()
        self.run()
    
    def run(self):
        Label(self.ventana, text = "   Usuario    =", fg=self.colorLetra, bg=self.colorFondo).place(x=250, y=150)
        Label(self.ventana, text = "Contraseña = ", fg=self.colorLetra, bg=self.colorFondo).place(x=250, y=225)
        entry = Entry(self.ventana, textvariable=self.usuario)
        entry.place(x=345, y=150)
        entry = Entry(self.ventana,show="*", textvariable=self.password)
        entry.place(x=345, y=225)
        self.abrirvenSecundaria = tk.Button(self.ventana, text="Ingresar", bg="#003333", fg=self.colorLetra, command = self.send).place(x=350, y=300)
        self.ventana.geometry(self.posicion)
        self.ventana.resizable(0,0)
        self.ventana.title("Login")
        self.ventana.mainloop()


    def getUser(self):
        return self.usuario.get()
    
    def getPassword(self):
        return self.password.get()
    
    def send(self):
        config = configparser.ConfigParser() 
        config.read('config.ini')
        engie =  MySQLEngine(config['DATABASE'])

        temp = User(engie).searchUsers(self.getUser(),self.getPassword())
        if (temp[0]):  
            drawWindows = DrawingApplication().buildWindow(engie, self.getUser(),self.getPassword(),temp[1])

        self.ventana.quit

a = LoginInit()