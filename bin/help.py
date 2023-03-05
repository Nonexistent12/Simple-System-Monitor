#Author: Marcus H.  
#This module exclusively handles the the User manual in the help menu, it uses a treeview to represent entries, and each entry has a associated text file.

from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,  ImageTk

paths = ["bin/text/blank.txt", "bin/text/Intro.txt", "bin/text/What.txt", "bin/text/CPU.txt", "bin/text/RAM.txt"] #creates a array that contains a path for each text file in the text folder



def doubleclick(event): #on doubleclick on one of the entries, it gets the entry index and sends the associated txt file to setpane()
   
    selected=paths[int(tree.selection()[0])] #sets selected to a text file path
    setpane(selected)



def create(): #creates the user manual window
    global mwindow, textLabel, tree
    
    selected=paths[0] #sets selected to blank text file
    
    #window creation
    mwindow = Toplevel()
    mwindow.title("User Manual")
    
    #centers the window
    posX= int(mwindow.winfo_screenwidth()/2 - 640/2) 
    posY = int(mwindow.winfo_screenheight()/2 - 640/2 ) 
    mwindow.geometry('%dx%d+%d+%d' % (640, 640, posX, posY))
    
    #window configuration
    mwindow.rowconfigure(0,  weight=1)
    mwindow.columnconfigure(0,  weight=1)
    
    #sets icon on window
    mwindow.iconphoto(False,  ImageTk.PhotoImage(Image.open('bin/icons/logo.ico')))
    mwindow.resizable(False,  False)
        
    #paned window creation
    pane1 =PanedWindow(mwindow, orient=VERTICAL) #left side paned window, which contains the tree
    pane2 = PanedWindow(mwindow,  orient=VERTICAL, width=400, bg='white', relief='sunken') #right side paned window, which contains the text file label
   
    
    textLabel = Text(pane2) #creates text label used for pane2
    
    #tree view creation and configuration
    tree = ttk.Treeview(pane1, selectmode="browse")
    tree.heading('#0', text="Contents",anchor=tk.W)
    tree.insert('', tk.END,  text="Introduction", iid=1, open=False)
    tree.insert('', tk.END,  text="What does this mean?", iid=2, open=False)
    tree.insert('', tk.END,  text="CPU", iid=3, open=False)
    tree.insert('', tk.END,  text="RAM", iid=4, open=False)
    tree.move(3, 2, 0)
    tree.move(4, 2, 1)
  
    #adds widgets tree and textLabel to paned windows
    pane1.add(tree)
    pane1.grid(column=0, row=0, sticky=tk.NW, ipady=100)
    pane2.add(textLabel)
    pane2.grid(column=0, row=0, sticky=tk.NE,ipadx=10, ipady=500)
    
    #binds doubleclick event to function doubleclick in the treewview
    tree.bind("<Double-1>",  doubleclick)
    
    #quit button creation
    ttk.Button(mwindow, text="Exit",  command=quit).grid(column=0, row=0, sticky=tk.SW)
    
    mwindow.grab_set() #makes window focused over main window
    
    setpane(selected) #sets text label to blank text file
    
    mwindow.mainloop()

def setpane(selected): #opens a text file and displays the text inside of the second paned window
   
    text = open(selected) #opens text file using selected path
    textLabel.delete(1.0, END) #clears text label
    textLabel.insert(END, text.read()) #inserts the text file text
    text.close() #closes text file
    
def quit(): #exits the user manual
    mwindow.destroy()






