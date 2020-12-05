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
from Core.configUser import *
from Core.User import *
import json
import re

temp = []
      
class ConfigUser(tkinter.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

    def buildWindow(self,engie=None):
        self.master.title("Configure User")

        def saveFile():
            print('guardo')
            filename = tkinter.filedialog.asksaveasfilename(title="Save Picture As...")

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

        def getUserName():
            return name.get()

        def getPassword():
            return password.get()

        def getFillColor():
            if (re.match("#[A-F0-F]{6}",fillColor.get())):
                return fillColor.get()

        def getPenColor():
            if (re.match("#[A-F0-F]{6}",pentColor.get())):
                return pentColor.get()     

        def save():
            a = User(engie)
            a.addUser(getUserName(), getPassword(), 1, getPenColor(), getFillColor())

        def delete(idUser = None):
            a = User(engie)
            id =  a.loginUser(getUserName(),getPassword())
            a.dropUser(id)

        def update():
            a = User(engie)
            id =  a.loginUser(getUserName(),getPassword())
            a.updateUser(getUserName(),getPassword(),1,getPenColor(), getFillColor(),id)

        circleButton = tkinter.Button(sideBar, text = "Save", command=save).place(x=180, y=100)
        circleButton2 = tkinter.Button(sideBar, text = "Delete", command=delete)
        circleButton2.place(x=180, y=180)
        circleButton3 = tkinter.Button(sideBar, text = "Update", command=update).place(x=250, y=180)
        
        circleButton.pack(fill=tkinter.BOTH)

def main():
    root = tkinter.Tk()
    drawingApp = ConfigUser(root)
    drawingApp.mainloop()
    print("Program Execution Completed.")

if __name__ == "__main__":
    main()