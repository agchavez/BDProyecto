from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style
from tkinter import messagebox

class Binnacle():
    def __init__(self):
        pass
    def a(self,ventana = Tk()):
        ventana.configure(background="#222222")
        ancho_ventana = 850
        alto_ventana = 800
        x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        ventana.geometry(posicion)
        ventana.resizable(0,0)
        ventana.title("Bitacora de usuarios")

        self.contenedor = Frame(ventana)
        self.lbl_titulo = Label(self.contenedor, text="Bitacora de usuarios",fg="#FFFFFF",bg="#222222",font=("times new roman",24))
        self.lbl_titulo.grid(pady=20)
        self.tabla = ttk.Treeview(self.contenedor, columns=('#1','#2'))
        self.tabla.column("#2", width=395, stretch=NO)
        self.tabla.grid(row=3,pady=20,padx=25)
        self.tabla.heading("#0", text="Fecha",anchor=CENTER)
        self.tabla.heading("#1", text="Usuario",anchor=CENTER)
        self.tabla.heading("#2", text="Actividad",anchor=CENTER)
        self.tabla.insert('',0,text="5/12/2020",values=("Jacome","Enamorando a Vanessa"))
        self.tabla.insert('',0,text="5/12/2020",values=("Jacome","Enamorando a Vanessa parte II"))
        self.contenedor.configure(background="#222222")
        self.contenedor.grid()
        ventana.mainloop()

        
        #def mostrarDatos(self):
        #datos = self.consultaBitacora(consulta)
        #for(nombre,clave) in datos:
            #self.tabla.insert('',0,text=nombre,values=clave)
        


#ventana = Tk()
aplicacion = Binnacle().a()
