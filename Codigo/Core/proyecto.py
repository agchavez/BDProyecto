"""
    @autor agchavez@unah.hn @david.jacome@unah.hn @Abner.Jimenez.@unah.hn
    @autor tomado con referencia del libro de texto
    @Date 2020/11/26
    @Version 1.0
"""

from Core.actionss import PyList, BeginFillCommand, CircleCommand, PenDownCommand, GoToCommand, EndFillCommand, PenUpCommand
from Core.configUser import *
from Core.User import *
from Core.MySQLEngine import *
from Core.Paint import *
from Core.ColorConf import *
from Core.ConsultasBDB import *
from tkinter import *
from tkinter import Tk
import tkinter as tk 
from tkinter.ttk import Style
from tkinter import ttk
from tkinter import messagebox as mb
import tkinter
import turtle
import xml
import xml.dom.minidom
import xml.etree.ElementTree as ET
import tkinter.colorchooser
import tkinter.filedialog
import json
import configparser


  
class DrawingApplication(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.graphicsCommands = PyList()

    def buildWindow(self, engine=None, user=None, password=None, id= None):
        self.engine = engine  
        self.user = user 
        self.password = password
        self.idUser = id
        self.penColor = '#000000'
        self.fillColor = '#000000' 
        self.master.title("Draw")
        bar = tkinter.Menu(self.master)
        fileMenu = tkinter.Menu(bar,tearoff=0)
        configbdb = configparser.ConfigParser() 
        configbdb.read('config.ini')
        self.engiebdb =  MySQLEngine(configbdb['DATABASERESPALDO'])

        def ColorDefaul():
            query = ColorConf(self.engine).searchColor(self.idUser)
            self.penColor = query[0][1]
            self.fillColor = query[0][0] 
            
        ColorDefaul()

        def newWindow():
            theTurtle.clear()
            theTurtle.penup()
            theTurtle.goto(0,0)
            theTurtle.pendown()
            screen.update()
            screen.listen()
            ColorDefaul()
            penColor.set(self.penColor)
            fillColor.set(self.fillColor)
            self.graphicsCommands = PyList()
            

        fileMenu.add_command(label="New", command=newWindow)

        def parse(data):
            newWindow()
            self.graphicsCommands = PyList()
            graphicsCommands = data['GraphicsCommands']
            for commandElement in graphicsCommands['Commands']:
                command = commandElement['command']
                if command == "GoTo":
                    x = float(commandElement['x'])
                    y = float(commandElement['y'])
                    width = float(commandElement['width'])
                    color = commandElement['color'].strip()
                    cmd = GoToCommand(x,y,width,color)

                elif command == "Circle":
                    radius = float(commandElement['radius'])
                    width = float(commandElement['width'])
                    color = commandElement['color'].strip()
                    cmd = CircleCommand(radius,width,color)

                elif command == "BeginF":
                    color = commandElement['color'].strip()
                    cmd = BeginFillCommand(color)

                elif command == "EndFill":
                    cmd = EndFillCommand()

                elif command == "PenUp":
                    cmd = PenUpCommand()

                elif command == "PenDown":
                    cmd = PenDownCommand()
                else:
                    raise RuntimeError("Unknown Command: " + command)

                self.graphicsCommands.append(cmd)

            for cmd in self.graphicsCommands:
                cmd.draw(theTurtle)

            screen.update()
            downloadMenu(True)
            #print(graphicsCommands)

        #cargar dibujo desde la base de datos solo si pertenecen a ese usuario de acuerdo al id
        def loadFile():
            run()
        
        def addToFile():
            filename = tkinter.filedialog.askopenfilename(title="Select a Graphics File")

            theTurtle.penup()
            theTurtle.goto(0,0)
            theTurtle.pendown()
            theTurtle.pencolor("#000000")
            theTurtle.fillcolor("#000000")
            cmd = PenUpCommand()
            self.graphicsCommands.append(cmd)
            cmd = GoToCommand(0,0,1,"#000000")
            self.graphicsCommands.append(cmd)
            cmd = PenDownCommand()
            self.graphicsCommands.append(cmd)
            screen.update()
            parse(filename)

            for cmd in self.graphicsCommands:
                cmd.draw(theTurtle)

            screen.update()

        def configure():
            config = ConfigUser().buildWindow(self.engine,self.engiebdb)

        if (User(self.engine).searchAdmin(self.user, self.password)[0]):   
            fileMenu.add_command(label="Configure", command=configure)

        def downloadMenu(temp):
            if(temp):
                fileMenu.add_command(label="Download", command=download)
            else:
                if (User(self.engine).searchAdmin(self.user, self.password)[0]):
                    fileMenu.delete(6)
                else:
                    fileMenu.delete(5)

        def write(filename):
            temp = [] 
            json = ""
            for cmd in self.graphicsCommands:
                temp.append(str(cmd))
            json += '{"GraphicsCommands": {"Commands": ['
            json += ','.join(temp)
            json += ']}'
            json += "}"
            
            id = User(self.engine).loginUser(self.user,self.password)
            Paint(self.engine).addPaint(filename, json , id)
            paintBDB(self.engiebdb).addPaint(filename, json , id)
            mb.showinfo("Informacion","Usuario agregado con exito")

        def updateDraw():
            return drawingJson(self.id_P)
        
        def drawingJson(id_Draw):
            temp = [] 
            json = ""
            for cmd in self.graphicsCommands:
                temp.append(str(cmd))
            json += '{"GraphicsCommands": {"Commands": ['
            json += ','.join(temp)
            json += ']}'
            json += "}"
            Paint(self.engine).updatePaint(json , id_Draw)
            paintBDB(self.engiebdb).addPaint(self.namePaint, json , id)
            mb.showinfo("SUCCESS","Dibujo actualizado con exito")
            
        def saveFile():
            run2() 

        def download():
            print(self.idUser,self.namePaint)
            paintdbd = paintBDB(self.engiebdb).showPaints(self.idUser,self.namePaint)
            if(paintdbd[0]):
                filename = tkinter.filedialog.asksaveasfilename(title="Descargar dibujo...")
                file = open(filename, "w")
                file.write(json.loads(paintdbd[1]))
                downloadMenu(False)
                messagebox.showinfo(message="Dibujo descargado con exito", title="SUCCESS")

            else:
                print('ERROR con la base de datos B')

        def viewBinnacle():
            binnacle()
        def exit():
            print('adios')
            self.engine.closeConnection()
            self.engiebdb.closeConnection()
            self.master.quit()
        fileMenu.add_command(label="Save",command=saveFile)
        #fileMenu.add_command(label="Download",command=download)
        fileMenu.add_command(label="Binnacle",command=viewBinnacle)
        fileMenu.add_command(label="Exit",command=exit)
        bar.add_cascade(label="File",menu=fileMenu)
        self.master.config(menu=bar)

        canvas = tkinter.Canvas(self,width=600,height=600)
        canvas.pack(side=tkinter.LEFT)

        theTurtle = turtle.RawTurtle(canvas)

        theTurtle.shape("circle")
        screen = theTurtle.getscreen()
        screen.tracer(0)

        sideBar = tkinter.Frame(self,padx=5,pady=5)
        sideBar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

        pointLabel = tkinter.Label(sideBar,text="Width")
        pointLabel.pack()

        widthSize = tkinter.StringVar()
        widthEntry = tkinter.Entry(sideBar,textvariable=widthSize)
        widthEntry.pack()
        widthSize.set(str(1))

        radiusLabel = tkinter.Label(sideBar,text="Radius")
        radiusLabel.pack()
        radiusSize = tkinter.StringVar()
        radiusEntry = tkinter.Entry(sideBar,textvariable=radiusSize)
        radiusSize.set(str(10))
        radiusEntry.pack()

        def circleHandler():
            cmd = CircleCommand(float(radiusSize.get()), float(widthSize.get()), penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            screen.update()
            screen.listen()

        circleButton = tkinter.Button(sideBar, text = "Draw Circle", command=circleHandler)
        circleButton.pack(fill=tkinter.BOTH)
        screen.colormode()
        penLabel = tkinter.Label(sideBar,text="Pen Color")
        penLabel.pack()
        penColor = tkinter.StringVar()
        penEntry = tkinter.Entry(sideBar,textvariable=penColor)
        penEntry.pack()

        penColor.set(self.penColor)

        def getPenColor():
            color = tkinter.colorchooser.askcolor()
            if color != None:
                penColor.set(str(color)[-9:-2])
                # Se almacena el valor del fillColor seleccionado en la variable Self.fillcolor
                self.penColor = color[1]
                # Se llama a la funcion addBinnacle de la clase Colorconf
                ColorConf(self.engine).addBinnacle(self.idUser,self.penColor, self.fillColor)
                

        penColorButton = tkinter.Button(sideBar, text = "Pick Pen Color", command=getPenColor)
        penColorButton.pack(fill=tkinter.BOTH)

        fillLabel = tkinter.Label(sideBar,text="Fill Color")
        fillLabel.pack()
        fillColor = tkinter.StringVar()
        fillEntry = tkinter.Entry(sideBar,textvariable=fillColor)
        fillEntry.pack()

        fillColor.set(self.fillColor)

        def getFillColor():
            color = tkinter.colorchooser.askcolor()
            if color != None:
                fillColor.set(str(color)[-9:-2])
                # Se almacena el valor del fillColor seleccionado en la variable Self.fillcolor
                self.fillColor = color[1]
                # Se llama a la funcion addBinnacle de la clase Colorconf
                ColorConf(self.engine).addBinnacle(self.idUser,self.penColor, self.fillColor)

        fillColorButton = tkinter.Button(sideBar, text = "Pick Fill Color", command=getFillColor)
        fillColorButton.pack(fill=tkinter.BOTH)


        def beginFillHandler():
            cmd = BeginFillCommand(fillColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)

        beginFillButton = tkinter.Button(sideBar, text = "Begin Fill", command=beginFillHandler)
        beginFillButton.pack(fill=tkinter.BOTH)

        def endFillHandler():
            cmd = EndFillCommand()
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)

        endFillButton = tkinter.Button(sideBar, text = "End Fill", command=endFillHandler)
        endFillButton.pack(fill=tkinter.BOTH)

        penLabel = tkinter.Label(sideBar,text="Pen Is Down")
        penLabel.pack()

        def penUpHandler():
            cmd = PenUpCommand()
            cmd.draw(theTurtle)
            penLabel.configure(text="Pen Is Up")
            self.graphicsCommands.append(cmd),

        penUpButton = tkinter.Button(sideBar, text = "Pen Up", command=penUpHandler)
        penUpButton.pack(fill=tkinter.BOTH)

        def penDownHandler():
            cmd = PenDownCommand()
            cmd.draw(theTurtle)
            penLabel.configure(text="Pen Is Down")
            self.graphicsCommands.append(cmd)

        penDownButton = tkinter.Button(sideBar, text = "Pen Down", command=penDownHandler)
        penDownButton.pack(fill=tkinter.BOTH)

        def clickHandler(x,y):
            
            cmd = GoToCommand(x,y,float(widthSize.get()),penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            screen.update()
            screen.listen()

        screen.onclick(clickHandler)

        def dragHandler(x,y):
            cmd = GoToCommand(x,y,float(widthSize.get()),penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            screen.update()
            screen.listen()

        theTurtle.ondrag(dragHandler)

        def undoHandler():
            if len(self.graphicsCommands) > 0:
                self.graphicsCommands.removeLast()
                theTurtle.clear()
                theTurtle.penup()
                theTurtle.goto(0,0)
                theTurtle.pendown()
                for cmd in self.graphicsCommands:
                    cmd.draw(theTurtle)
                screen.update()
                screen.listen()

        fileMenu.add_command(label="Load",command=lambda: loadFile())
        screen.onkeypress(undoHandler, "u")
        screen.listen()

        #Ventana Load y Delete Draw
        def run():
            self.ventana1 = Tk()
            self.colorFondo = "#222222"
            self.colorLetra = "#FFF"
            ancho_ventana = 300
            alto_ventana = 200
            x_ventana = self.ventana1.winfo_screenwidth() // 2 - ancho_ventana // 2
            y_ventana = self.ventana1.winfo_screenheight() // 2 - alto_ventana // 2
            self.ventana1.configure(background=self.colorFondo)
            self.posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
            self.ventana1.geometry(self.posicion)
            self.ventana1.resizable(0,0)
            self.ventana1.title("Dibujo")
            self.fileNames = tk.StringVar()


            self.opcion=tk.StringVar()
            self.paint = Paint(self.engine)
            
            query = self.engine.management('sp_login',(self.user, self.password, None, None))

            if ((query[2] == 1) or (query[2] == 0)):
                #idDibujo
                #Eliminar sp y de Paint
                #Paint(self.engine).searchPaints(query[2])
                content = self.paint.search(query[3])
            if(len(content) != 0):
                self.label1=ttk.Label(self.ventana1, text="Mis dibujos",foreground="#FFFFFF",background="#222222")
                self.label1.grid(pady=10,padx=85)
                self.combobox1=ttk.Combobox(self.ventana1,width=15,textvariable=self.opcion, values=content)
                self.combobox1.current(0)
                self.a = self.combobox1.current(0)
                self.combobox1.grid(pady=5, padx=85)

                self.boton1 = tk.Button(self.ventana1, text="Load", command = loadDraw, width=8)
                self.boton1.grid(pady=5, padx=85)

                self.boton2 = tk.Button(self.ventana1, text="Delete", command = deleteDraw,width=8)
                self.boton2.grid(pady=5, padx=85)
            else:
                self.label2=ttk.Label(self.ventana1, text="No se han",foreground="#FF0000",background="#222222",font=("Times new roman",18))
                self.label2.grid(pady=10,padx=67)
                self.label3=ttk.Label(self.ventana1, text="registrado dibujos",foreground="#FF0000",background="#222222",font=("Times new roman",18))
                self.label3.grid(pady=10,padx=67)

        def loadDraw():
            r = self.combobox1.get().split(" ")
            id = r[0]   
            self.namePaint = r[1] 
            jsons = self.paint.searchPaint(id)
            b = json.loads(jsons)
            return parse(b)

        def deleteDraw():
            r = self.combobox1.get().split(" ")
            id = r[0]
            jsons = self.paint.searchPaint(id)
            self.paint.dropePaint(id)
            self.ventana1.destroy

        #Ventana de guardado de dibujo
        def run2():
            self.ventana2 = Tk()
            self.colorFondo = "#222222"
            self.colorLetra = "#FFF"
            ancho_ventana = 400
            alto_ventana = 300
            x_ventana = self.ventana2.winfo_screenwidth() // 2 - ancho_ventana // 2
            y_ventana = self.ventana2.winfo_screenheight() // 2 - alto_ventana // 2
            self.ventana2.configure(background=self.colorFondo)
            self.posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
            self.ventana2.geometry(self.posicion)
            self.ventana2.resizable(0,0)
            self.ventana2.title("Dibujo")
            self.fileNames = tk.StringVar()

            self.label1 = Label(self.ventana2, text="Nombre del Dibujo",fg="#FFFFFF",bg="#222222")
            self.label1.grid(pady=20, padx=70)

            self.entry = Entry(self.ventana2,width=20,textvariable=self.fileNames)
            self.entry.grid(pady=5, padx=70)

            self.boton1 = tk.Button(self.ventana2, text="Save", command = check,width=10)
            self.boton1.grid(pady=5, padx=70)

        def check():
            if(self.entry.get() == ""):
                mb.showerror("Error","No puede dejar los cuadros de entrada vacíos")
            else:
                namePaint = self.entry.get()
                result = Paint(self.engine).searchPaintName(namePaint, idUser=self.idUser)
                print(result)
                #Si result es verdadero significa que encontro un dibujo con un nombre igual al que queremos asignar.
                #Por tanto le preguntara al usuario si quiere modificar el dibujo que ya estaba guardado o quiere guardar con un nuevo nombre.
                if(result[1] == False):
                    save()
                else:
                    self.namePaint = self.entry.get()
                    self.id_P = result[1]
                    self.label2 = Label(self.ventana2, text="Nombre de dibujo ya registrado",fg="#FF0000",bg="#222222")
                    self.label2.grid(pady=20, padx=100)
                    self.boton2 = tk.Button(self.ventana2, text="Actualizar dibujo", command = updateDraw,width=15)
                    self.boton2.grid(pady=5, padx=100)

        def save():
            return write(self.entry.get())

        
        def binnacle():
            ventana = Tk()
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
            self.lbl_titulo = Label(ventana, text="Bitacora de usuarios",fg="#FFFFFF",bg="#222222",font=("times new roman",24))
            self.lbl_titulo.grid(pady=20)
            self.tabla = ttk.Treeview(ventana, columns=('#1','#2','3','4'))
            self.tabla.column("#0", width=170)
            self.tabla.column("#1", width=140)
            self.tabla.column("#3", width=125)
            self.tabla.column("#4", width=125)
            self.tabla.grid(row=4,pady=50,padx=30)
            self.tabla.heading("#0", text="Fecha",anchor=CENTER)
            self.tabla.heading("#1", text="Usuario",anchor=CENTER)
            self.tabla.heading("#2", text="Actividad",anchor=CENTER) 
            self.tabla.heading("#3", text="PenColor",anchor=CENTER)
            self.tabla.heading("#4", text="FillColor",anchor=CENTER)
            self.contenedor.configure(background="#222222")
            mostrarDatos()
            self.contenedor.grid()

        def mostrarDatos():
            if(User(self.engine).searchAdmin(self.user, self.password)[0]):
                datos = "SELECT DISTINCT Binnacle.dat_date, CAST(AES_DECRYPT(User.var_userName,'admin')AS CHAR), Binnacle.tex_action, Binnacle.var_penColor, Binnacle.var_fillColor FROM User JOIN Binnacle ON Binnacle.id_user = User.id"
            else: 
                datos = "SELECT DISTINCT Binnacle.dat_date, CAST(AES_DECRYPT(User.var_userName,'admin')AS CHAR), Binnacle.tex_action, Binnacle.var_penColor, Binnacle.var_fillColor FROM User JOIN Binnacle ON Binnacle.id_user = User.id WHERE User.id = %d;" %(self.idUser)

            dates = self.engine.select(datos)
            
            for values in dates:
                date = values[0]
                name = values[1]
                action = values[2]
                penColor1 = values[3]
                fillColor1 = values[4]

                self.tabla.insert('',0,text=date,values=(name, action,penColor1,fillColor1))