"""
    @autor agchavez@unah.hn @david.jacome@unah.hn 
    @Date 2020/11/26
    @Version 1.0
"""

#from actionss import PyList, BeginFillCommand, CircleCommand, PenDownCommand, GoToCommand, EndFillCommand, PenUpCommand
import tkinter
import turtle
import xml
import xml.dom.minidom
import xml.etree.ElementTree as ET
import tkinter.colorchooser
import tkinter.filedialog
import json
import re
temp = []
      
class ConfigUser(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.buildWindow()
        
    def buildWindow(self):
        self.master.title("Configure User")
        bar = tkinter.Menu(self.master)
        fileMenu = tkinter.Menu(bar,tearoff=0)

        def newWindow():
            theTurtle.clear()
            theTurtle.penup()
            theTurtle.goto(0,0)
            theTurtle.pendown()

        def saveFile():
            print('guardo')
            filename = tkinter.filedialog.asksaveasfilename(title="Save Picture As...")

        bar.add_cascade(label="Menu",menu=fileMenu)
        fileMenu.add_command(label="Exit",command=self.master.quit)
        self.master.config(menu=bar)

        sideBar = tkinter.Frame(self,padx=300,pady=300)
        sideBar.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH)

        nameLabel = tkinter.Label(sideBar,text="Nombre")
        nameLabel.pack()
        name = tkinter.StringVar()
        widthEntry = tkinter.Entry(sideBar,textvariable=name)
        widthEntry.pack()

        passwordLabel = tkinter.Label(sideBar,text="Contraseña")
        passwordLabel.pack()
        password = tkinter.StringVar()
        radiusEntry = tkinter.Entry(sideBar,textvariable=password)
        radiusEntry.pack()

        #Validar con expresion regular que solo permita hexadecimal
        pentColorLabel = tkinter.Label(sideBar,text="Pent-Color")
        pentColorLabel.pack()
        pentColor = tkinter.StringVar()
        radiusEntry = tkinter.Entry(sideBar,textvariable = pentColor)
        radiusEntry.pack()

        fillColorLabel = tkinter.Label(sideBar,text="Fill-color")
        fillColorLabel.pack()
        fillColor = tkinter.StringVar()
        radiusEntry = tkinter.Entry(sideBar,textvariable=fillColor)
        radiusEntry.pack()

        #widthSize.set(str(1))
        #radiusSize.set(str(10))
        #radiusSize.set(str(10))
        #radiusSize.set(str(10))

        def getUserName():
            return name.get()

        def getPassword():
            return password.get()

        def getFillColor():
            return fillColor.get()

        def getPentColor():
            return pentColor.get()        

        def save():
            pass

        circleButton = tkinter.Button(sideBar, text = "Save", command=save)
        circleButton.pack(fill=tkinter.BOTH)

def main():
    root = tkinter.Tk()
    drawingApp = ConfigUser(root)

    drawingApp.mainloop()
    print("Program Execution Completed.")

if __name__ == "__main__":
    main()