"""
    @autor agchavez@unah.hn @david.jacome@unah.hn @aajimezez@unah.hn
    @Date 2020/11/26
    @Version 1.0
"""

#from actionss import PyList, BeginFillCommand, CircleCommand, PenDownCommand, GoToCommand, EndFillCommand, PenUpCommand
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style
from tkinter import messagebox

import tkinter
import turtle
import xml
import xml.dom.minidom
import xml.etree.ElementTree as ET
import tkinter.colorchooser
import tkinter.filedialog
from Core.configUser import *
from Core.User import *
import json
import re

temp = []   
class ConfigUser:
    def __init__(self):
        pass

    def buildWindow(self, engie=None,engiebdb = None): 
        def getUserName():
            return nameEntry.get()

        def getPassword():
            return passwordEntry.get()

        def getFillColor():
            if (re.match("^#(?:[0-9a-fA-F]{3}){1,2}$",fillColorEntry.get())):
                return fillColorEntry.get()

        def getPenColor():
            if (re.match("^#(?:[0-9a-fA-F]{3}){1,2}$",pentEntry.get())):
                return pentEntry.get()     

        def save():
            a = User(engie)
            if (getFillColor() != None and getPenColor() != None):
                a.addUser(getUserName(), getPassword(), 1, getPenColor(), getFillColor())
                UserBDB(engiebdb).addUser(getUserName(), getPassword(), 1, getPenColor(), getFillColor())
                messagebox.showinfo(message="Usuario registrado con éxito", title="SUCCESS")
            else:
                messagebox.showwarning(message="Ingrese un hexadecimal en las casillas PenColor y FillColor", title="ERROR")

        def delete(idUser = None):
            a = User(engie)
            id =  a.loginUser(getUserName(),getPassword())
            a.dropUser(id)

        def update():
            a = User(engie)
            id =  a.loginUser(getUserName(),getPassword())
            a.updateUser(getUserName(),getPassword(),1,getPenColor(), getFillColor(),id)

        ventana = Tk()
        ventana.configure(background="#222222")
        ancho_ventana = 600
        alto_ventana = 600
        x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        ventana.geometry(posicion)
        ventana.resizable(0,0)
        ventana.title("Configuración de usuarios")

        instruccionLabel = Label(ventana,text="Intrucciones",fg="#FF0000",bg="#222222")
        instruccionLabel.grid(pady=3,padx=2)
        instruccionLabel1 = Label(ventana,text="* Eliminar: Ingrese solo el usuario",fg="#FF0000",bg="#222222")
        instruccionLabel1.grid(pady=3,padx=3)
        instruccionLabel2 = Label(ventana,text="* Actualizar: Ingrese usuario y contraseña",fg="#FF0000",bg="#222222")
        instruccionLabel2.grid(pady=3,padx=3)

        nameLabel = Label(ventana,text="Nombre",fg="#FFFFFF",bg="#222222")
        nameLabel.grid(pady=15,padx=225)
        name = StringVar()
        nameEntry = Entry(ventana, textvariable = name)
        nameEntry.grid(pady=5,padx=225)

        passwordLabel = Label(ventana,text="Contraseña",fg="#FFFFFF",bg="#222222")
        passwordLabel.grid(pady=5,padx=225)
        password = StringVar()
        passwordEntry = Entry(ventana,textvariable=password)
        passwordEntry.grid(pady=5,padx=225)

        pentColorLabel = Label(ventana,text="Pent-Color",fg="#FFFFFF",bg="#222222")
        pentColorLabel.grid(pady=5,padx=225)
        pentColor = StringVar()
        pentEntry = Entry(ventana,textvariable = pentColor)
        pentEntry.grid(pady=5,padx=225)

        fillColorLabel = Label(ventana,text="Fill-color",fg="#FFFFFF",bg="#222222")
        fillColorLabel.grid(pady=5,padx=225)
        fillColor = StringVar()
        fillColorEntry = Entry(ventana,textvariable=fillColor)
        fillColorEntry.grid(pady=5,padx=225)

        circleButton =  Button(ventana, text = "Save", command=save)
        circleButton.grid(pady=5,padx=225)
        circleButton2 = Button(ventana, text = "Delete", command=delete)
        circleButton2.grid(pady=5,padx=225)
        circleButton3 = Button(ventana, text = "Update",command=update)
        circleButton3.grid(pady=5,padx=225)

        ventana.grid()