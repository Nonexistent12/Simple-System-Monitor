#Author: Marcus H.
#Description: This file controls the create account part of the program, it can take a email, and a password, and verify them as correctly inputted. It does not actually save any passwords or create any accounts, its simply a demonstration of Tkinter and my code writing.
from tkinter import *
from tkinter import ttk
from PIL import Image,  ImageTk


endings = [".com", ".org",  ".edu", ".net"] #common 3 letter email endings, I can't really see anyone using a .info or .us email with this program.

def create(): #this is the main window function, it creates the window and all of its features
    
    global emailvar, passwrdvar, cpasswrdvar,  window1, icon
    window1 = Toplevel() #create account window
    frame = ttk.Frame(window1,  padding="10") #window frame
    window1.title('Create Account')
    
   
    
    window1.geometry('360x150')
    
    
    window1.resizable(False,  False)
        
    frame.grid(sticky=(N, W, E, S))
    frame.rowconfigure(0,  weight=1)
    frame.columnconfigure(0,  weight=1)
   
   #entry variables
    emailvar=StringVar()
    passwrdvar = StringVar()
    cpasswrdvar = StringVar()
    
    icon = ImageTk.PhotoImage(Image.open('bin/icons/logo.ico')) #icon on window
    window1.iconphoto(False, icon)
    
    #Email entry
    ttk.Label(frame,  text="Email: ", font=(10)).grid(column=0, row=0,  sticky=NW)
    ttk.Entry(frame,  textvariable = emailvar).grid(column=1, row=0, sticky=N, ipadx=30)
    
    #First password entry
    ttk.Label(frame,  text="Password: ",  font=(10)).grid(column=0,  row=1,  sticky=NW, pady=10)
    ttk.Entry(frame,  textvariable = passwrdvar, show="*").grid(column=1, row=1, sticky=N, ipadx=30, pady=10)
    
    #Second password entry
    ttk.Label(frame,  text="Confirm Password: ",  font=(10)).grid(column=0,  row=2,  sticky=NW, pady=10)
    ttk.Entry(frame,  textvariable = cpasswrdvar, show="*").grid(column=1, row=2, sticky=N, ipadx=30, pady=10)
    
    #submit and exit buttons
    ttk.Button(frame,  text="Submit", command=submit).grid(column=1, row=6, sticky=S)
    ttk.Button(frame,  text="Exit", command=quit).grid(column=0, row=6,   sticky=SW)
    
    
    window1.mainloop()
    
    
def submit(): #this is used for when you click the submit button, it checks if every entry has been 
   
    suffix = emailvar.get() #gets the email
    suffix = suffix[-4:] #gets the last 4 characters of it
    
    if "@" in emailvar.get() and suffix in endings: #checks if there is a @ symbol
        
        
        if passwrdvar.get() == "" or cpasswrdvar.get() == "": #makes sure there is a entry in both passwords
            popup("Please enter a password into both entries.")
        else:
            
            if passwrdvar.get() == cpasswrdvar.get(): #checks to if both passwords match
                popup("Account created!")
                emailvar.set("")
                passwrdvar.set("")
                cpasswrdvar.set("")
                
            
            else:
                popup("Please make sure both passwords are the same.")
    
    else:
        popup("Please enter a valid email.")


def popup(msg): #creates a popup window that displays a message corresponding to whatever the user is missing in the entries
    pop = Toplevel(window1) #makes the popup a child of the create account window
    pop.iconphoto(False,  icon)
    
    pop.geometry("300x64")
    
    ttk.Label(pop,  text=msg).pack()
    ttk.Button(pop,  text="Ok", command=pop.destroy).pack(pady=10)
    
    pop.resizable(False,  False)
    pop.grab_set() #puts on top of all the other windows, and you can't proceed without closing it
    
    
def quit(): #exits the create account window
    window1.destroy()
    