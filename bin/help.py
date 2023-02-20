#Author: Marcus H.  
#This module exclusively handles the the User manual in the help menu, it uses a treeview to represent entries, and each entry has a associated text file.

from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,  ImageTk

paths = ["bin/text/blank.txt", "bin/text/Intro.txt", "bin/text/What.txt", "bin/text/CPU.txt", "bin/text/RAM.txt"]



def doubleclick(event): #on doubleclick on one of the entries, it gets the entry index and posts the associated txt file
    global selected
    selected_item = tree.selection()
    
    if not selected_item:
        return
    else:
        selected=paths[int(tree.selection()[0])]
        setpane()



def create(): #creates the user manual window
    global tree, mwindow, selected,  textLabel
    
    selected=paths[0]
    mwindow = Toplevel()
    mwindow.title("User Manual")
    mwindow.geometry("640x640")
    mwindow.rowconfigure(0,  weight=1)
    mwindow.columnconfigure(0,  weight=1)
    mwindow.iconphoto(False,  ImageTk.PhotoImage(Image.open('bin/icons/logo.ico')))
    mwindow.resizable(False,  False)
        
    pane1 =PanedWindow(mwindow, orient=VERTICAL)
    pane2 = PanedWindow(mwindow,  orient=VERTICAL, width=400, bg='white', relief='sunken')
    textLabel = Text(pane2)
    tree = ttk.Treeview(pane1, selectmode="browse")

    tree.heading('#0', text="Contents",anchor=tk.W)
    tree.insert('', tk.END,  text="Introduction", iid=1, open=False)
    tree.insert('', tk.END,  text="What does this mean?", iid=2, open=False)

    tree.insert('', tk.END,  text="CPU", iid=3, open=False)
    tree.insert('', tk.END,  text="RAM", iid=4, open=False)

    tree.move(3, 2, 0)
    tree.move(4, 2, 1)
        
    pane1.add(tree)
    pane1.grid(column=0, row=0, sticky=tk.NW, ipady=100)
    pane2.add(textLabel)
    pane2.grid(column=0, row=0, sticky=tk.NE,ipadx=10, ipady=500)
    tree.bind("<Double-1>",  doubleclick)
    ttk.Button(mwindow, text="Exit",  command=quit).grid(column=0, row=0, sticky=tk.SW)
    
    mwindow.grab_set()
    setpane()
    mwindow.mainloop()

def setpane(): #opens a text file and displays the text inside of the second paned window
    global textLabel
    text = open(selected)
    textLabel.delete(1.0, END)
    textLabel.insert(END, text.read())
    text.close()
    
def quit(): #exits the user manual
    mwindow.destroy()






