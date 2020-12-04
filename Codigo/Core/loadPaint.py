import tkinter as tk 
from tkinter import ttk 
  
class LoadDraw:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.opcion=tk.StringVar()
    
    def run(self,content = None):
        self.label1=ttk.Label(self.ventana1, text="Mis dibujos")
        self.label1.grid(column=0, row=0)

        self.combobox1=ttk.Combobox(self.ventana1,width=10,textvariable=self.opcion, values=content)
        self.combobox1.current(0)
        self.a = self.combobox1.current(0)
        self.combobox1.grid(column=0, row=1)

        self.boton1=tk.Button(self.ventana1, text="Cargar", command=self.recuperar)
        self.boton1.grid(column=0, row=2)

        self.label2=ttk.Label(self.ventana1, text="Dibujo seleccionado:")
        self.label2.grid(column=0, row=3)
        self.ventana1.mainloop()

    def recuperar(self):
        print(self.combobox1.get())
        self.label2.configure(text = self.combobox1.get())
        return (self.combobox1.get())