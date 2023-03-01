#Author: Marcus H.
#Description: This is the main program, which collects some basic system stats, has menus for sub-windows, and has the ability to refresh itself if needed. 

import psutil 
import platform as plat
from tkinter import *
from tkinter import ttk
from bin import help, account
from PIL import Image,  ImageTk

 

conversion = (9.31*10**-10) #Conversion factor for Bytes to GB and Hz to GHz
mem = psutil.virtual_memory() #This just for ease of use in my code.

def activestats(): #This function collects hardware stats that are constantly changing, such as CPU usage and Ram Usage
    
    cusage.set(f"-CPU Usage: {psutil.cpu_percent()}%")
    cfreq.set(f"-CPU Frequency: {(psutil.cpu_freq().current)/1000} GHz")
    rusage.set(f"-RAM Usage: {round(mem.used*conversion, 1)} GB")
    ravailable.set(f"-RAM Available: {round((mem.available)*conversion, 1)}GB")
    ui.after(1000, activestats)





def main(): #defines the main window, StringVars, and other stuff like icons
    global ui
    global frame
    global cusage,  cpu,  cfreq,  rusage,  rtotal,  ravailable, cpuico, ramico, driveico,  logo
    

    ui = Tk() #window used for the main program
    ui.option_add('*tearOff', FALSE)

    ui.title('Simple Monitor')
    
    posX= int(ui.winfo_screenwidth()/2 - 480/2) #Position of X for the window in the center of the screen
    posY = int(ui.winfo_screenheight()/2 - 480/2 ) #Position of Y for the window in the center of the screen
    
    frame = ttk.Frame(ui,  padding="10") #main frame of the main window
    
    ui.geometry('%dx%d+%d+%d' % (480, 480, posX, posY))
    
    
    #Icons and Images used in main window
    logo = Image.open('bin/icons/logo.ico') #Logo used on the window icon
    cpuico = Image.open('bin/icons/cpu.ico') #CPU icon
    ramico = Image.open("bin/icons/ram.ico") #RAM icon
    driveico = Image.open("bin/icons/drive.ico")# Drive Icon
    cpuico = cpuico.resize((24, 24))
    ramico = ramico.resize((24, 24))
    driveico = driveico.resize((24, 24))
    cpuico = ImageTk.PhotoImage(cpuico)
    ramico = ImageTk.PhotoImage(ramico)
    driveico = ImageTk.PhotoImage(driveico)
    logo = ImageTk.PhotoImage(logo)
    
    
    frame.grid(sticky=(N, W, E, S))
    ui.rowconfigure(0, weight=0)
    ui.iconphoto(False,  logo)
    




    #String Variables
    cusage = StringVar()
    cpu = StringVar()
    cfreq = StringVar()
    rusage = StringVar()
    rtotal = StringVar()
    ravailable= StringVar()
    
    
    #function calls
    stats()
    activestats()
    menus()
    diskstats()
    
    ui.mainloop()



def stats(): #collects stats that are non-changing unlike activestats()
    #cpu stats
    uname = plat.uname()
    cpu.set(f"CPU: {uname.processor}")
    ttk.Label(frame, image=cpuico, textvariable=cpu, compound='left',  background="#c2bebe",width=60, relief="solid").grid(column=0,  row=0, sticky=(W))
    ttk.Label(frame, textvariable=cusage).grid(column=0, row=1, sticky=(N))
    ttk.Label(frame,  textvariable=cfreq,  ).grid(column=0, row=2,  sticky=(N))
    #ram stats
    rtotal.set(f"RAM Total: {round(mem.total*conversion,  1)} GB")
    ttk.Label(frame, image=ramico,   textvariable=rtotal, compound='left',  background="#c2bebe",width=60, relief="solid").grid(column=0, row=3,  sticky=(W))
    ttk.Label(frame,  textvariable=rusage).grid(column=0, row=4,  sticky=(N))
    ttk.Label(frame,  textvariable=ravailable).grid(column=0, row=5,  sticky=(N))

    

    
def menus(): #Creates the menus seen at the top of the window.
    #main menubar creation
    menubar = Menu(ui) #menubar
    menu_account = Menu(menubar,  tearoff=0)
    menu_help = Menu(menubar,  tearoff=0)
    
    #account menu 
    menubar.add_cascade(menu=menu_account,  label='Account')
    menu_account.add_command(label="Create Account",  command=account.create)
    
    #Help menu
    menubar.add_cascade(menu=menu_help,  label='Help')
    menu_help.add_command(label="User Manual",  command=help.create)
    menu_help.add_command(label="About",  command=about)
    
    
    ui.config(menu=menubar)



def diskstats(): #gets info about the disks connected to the system, which include USBs. Because of the ever changing disks in a system, it will has to run a for loop to get all of them when refreshed. So if you plug a USB drive in, it will add it to the list.
   
    index = 6 #index used for loop
    partitions = psutil.disk_partitions() #gets a list of partitions on the system
    

    for partition in partitions:
        try: #Some disks have higher permissions or unmounted partitions, so we have to use the try method to prevent a program halt
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue 
        except OSError:
            break
            
        
        ttk.Label(frame, image=driveico,   text=(f"Drive: {partition.device}"), compound='left',  background="#c2bebe", relief="solid").grid(column=0,  row=index,   sticky=(W,  E))
        index+=1
        ttk.Label(frame,  text=(f"-Total Capacity: {round(int(partition_usage.total)*conversion, 1)} GB")).grid(column=0,  row=index,   sticky=(N))
        index+=1
        ttk.Label(frame,  text=(f"-Free space: {round(int(partition_usage.free)*conversion,  1)} GB")).grid(column=0,  row=index,   sticky=(N))
        index+=1
    
    
    ttk.Button(ui, text="Exit",  command=quit).grid(column=0, row=index, pady=150,  sticky=SW) #although these buttons are not related the diskstats, its easier to create them here after the index is run through.
    ttk.Button(ui, text="Refresh", command=refresh).grid(column=0, row=index, padx=75, pady=150,  sticky=SW)
        
   

def refresh(): #Destroys the main window then restarts it by running main() again
    ui.destroy()
    main()
    
    
def about(): #Creates a basic about window.
    global aboutwindow
    try:
        if aboutwindow.state() == "normal":
            aboutwindow.focus()
    except:
        aboutwindow=Toplevel()
        
        
        #Center image creation
        centerimage = Image.open('bin/icons/logo.png')
        centerimage = centerimage.resize((96, 96))
        centerimage = ImageTk.PhotoImage(centerimage)
        
        posX= int(aboutwindow.winfo_screenwidth()/2 - 240/2)
        posY = int(aboutwindow.winfo_screenheight()/2 - 190/2 ) 
        aboutwindow.geometry('%dx%d+%d+%d' % (240, 190, posX, posY))
        aboutwindow.title("About")
        aboutwindow.iconphoto(True, logo)
        aboutwindow.resizable(False,  False)
        
        
        #About info
        ttk.Label(aboutwindow,  image=centerimage).grid(column=0,  row=0, padx=70, pady=5)
        ttk.Label(aboutwindow,  text="Author: Marcus(Max) H.", font=("Arial", 10)).grid(column=0,   row=1, sticky=(N))
        ttk.Label(aboutwindow,  text="Version: 0.7.1", font=("Arial", 10)).grid(column=0,   row=2, sticky=(N))
        ttk.Label(aboutwindow,  text="Contact: mhrejsa1@ivytech.edu", font=("Arial", 10)).grid(column=0,   row=3, sticky=(N))
        
        aboutwindow.mainloop()


def quit(): #Quits the program
    ui.quit()
    ui.destroy()
    
if __name__  == "__main__":
    main()




