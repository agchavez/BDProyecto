"""
    @autor agchavez@unah.hn @david.jacome@unah.hn 
    @Date 2020/11/26
    @Version 1.0
"""

import tkinter
import turtle
import tkinter.colorchooser
import tkinter.filedialog
import json

      
class ConfigUser(tkinter.Frame):
    def __init__(self, master=None, data = {}):
        super().__init__(master)
        self.data = data 
        self.pack()
        self.buildWindow()
        
    def buildWindow(self):
        self.master.title("Guardar Dibujo")
        bar = tkinter.Menu(self.master)
        fileMenu = tkinter.Menu(bar,tearoff=0)


        sideBar = tkinter.Frame(self,padx=60,pady=60)
        sideBar.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH)

        radiusLabel = tkinter.Label(sideBar,text="Nombre del dibujo: ")
        radiusLabel.pack()
        radiusSize = tkinter.StringVar()
        radiusEntry = tkinter.Entry(sideBar,textvariable=radiusSize)
        radiusEntry.pack()

        def save():
            #data es el JSON del dibujo
            #Aqui va la consulta para guardar el archivo
            print(self.data)

        circleButton = tkinter.Button(sideBar, text = "Save", command=save)
        circleButton.pack(fill=tkinter.BOTH)

        def clickHandler(x,y):      
            cmd = GoToCommand(x,y,float(widthSize.get()),penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)

def main():
    data = {"Command": 152}
    root = tkinter.Tk()
    drawingApp = ConfigUser(root, data)

    drawingApp.mainloop()
    print("Program Execution Completed.")

if __name__ == "__main__":
    main()