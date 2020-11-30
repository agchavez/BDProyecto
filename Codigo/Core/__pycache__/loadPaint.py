import tkinter as tk 
from tkinter import ttk 
  
# Creating tkinter window 
window = tk.Tk() 
window.title('Load File') 
window.geometry('400x250') 
  
# label text for title 
ttk.Label(window, text = "Sus dibujos",  
          background = 'green', foreground ="white",  
          font = ("Times New Roman", 15)).grid(row = 0, column = 1) 
  
# label 
ttk.Label(window, text = "Seleccione el dibujo :", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 5, padx = 10, pady = 25) 
  
# Combobox creation 
monthchoosen = ttk.Combobox(window, width = 27) 
  
# Adding combobox drop down list 
monthchoosen['values'] = (' dibujo1',  
                          ' dibujo2', 
                          ' dibujo3', 
                          ' dibujo4') 

  
monthchoosen.grid(column = 1, row = 5) 
monthchoosen.current() 
window.mainloop() 