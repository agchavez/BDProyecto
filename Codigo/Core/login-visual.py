from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style
from tkinter import Tk
import tkinter as tk
from tkinter import messagebox
from proyecto import *

class LoginInit:
    def __init__(self):
        self.ventana = Tk()
        self.colorFondo = "#0033FF"
        self.colorLetra = "#FFF"
        ancho_ventana = 750
        alto_ventana = 600
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
        Label(self.ventana, text = "  Usuario   = ", fg=self.colorLetra, bg=self.colorFondo).place(x=250, y=80)
        Label(self.ventana, text = "Contraseña =", fg=self.colorLetra, bg=self.colorFondo).place(x=250, y=120)
        entry = Entry(self.ventana, textvariable=self.usuario)
        entry.place(x=325, y=80)
        entry = Entry(self.ventana,show="*", textvariable=self.password)
        entry.place(x=325, y=120)
        self.abrirvenSecundaria = tk.Button(self.ventana, text="Ingresar", bg="#003333", fg=self.colorLetra, command = self.send).place(x=340, y=165)
        self.ventana.geometry(self.posicion)
        self.ventana.resizable(0,0)
        self.ventana.title("Login")
        self.ventana.mainloop()

    def send(self):
        drawWindows = DrawingApplication().buildWindow()
        self.ventana.quit

a = LoginInit()