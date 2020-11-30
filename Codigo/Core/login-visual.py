from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style
from tkinter import messagebox

ventana = Tk()
colorFondo = "#0033FF"
colorLetra = "#FFF"
ancho_ventana = 700
alto_ventana = 300
x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)

ventana.configure(background=colorFondo)
s = Style()
s.configure ('My.TFrame', background = colorFondo, foreground=colorLetra)
usuario = StringVar()
password = StringVar()
Label(ventana, text = "  Usuario   = ", fg=colorLetra, bg=colorFondo).place(x=250, y=80)
Label(ventana, text = "Contraseña =", fg=colorLetra, bg=colorFondo).place(x=250, y=120)
entry = Entry(ventana, textvariable=usuario)
entry.place(x=325, y=80)
entry = Entry(ventana, textvariable=password)
entry.place(x=325, y=120)
Button(ventana, text="Ingresar", bg="#003333", fg=colorLetra).place(x=340, y=165)
ventana.geometry(posicion)
ventana.resizable(0,0)
ventana.title("Login")
ventana.mainloop()