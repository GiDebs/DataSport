#setting up the GUI interface in which 
#I ask to select the database .csv for the import
#Then I import it in web_app

#from binhex import getfileinfo
from importlib.resources import path
import ntpath
import shutil
from textwrap import fill
from tkinter import*
from tkinter import filedialog
#from tkinter.ttk import Labelframe
from PIL import Image,ImageTk

root = Tk()
root.title("Importazione dati")
root.geometry("680x220")
root.iconbitmap(r"C:\Users\Giulio\Documents\GitHub\DataSport\Icons\AtlLev1.ico")
# Create a class which include different global variables
class Globals:
    filename = None

# Fuunction that ask the path of the new origin and save it in the Origin directory
def Openfile():
    Globals.filename = filedialog.askopenfilenames(initialdir="\Desktop ", 
    title="Seleziona file", filetypes=(("Formato testo","*.csv"),("All Files","*.*")))
    origin = str(Globals.filename)
    origin1 = origin.replace("(","").replace(",", "").replace(")", "").replace("/", "\\").replace("'","")
    origin2 = ntpath.basename(origin1)
    targhet = "C:/Users/Giulio/Documents/GitHub/DataSport/Origini" + "/" + origin2
    targhet1 = targhet.replace("/", "\\")
    print(targhet1)
    shutil.copyfile(origin1, targhet1)
#
# Add Image to the left
#Create a canvas
canvas= Canvas(root, width= 310, height= 210)
canvas.grid(row=0, rowspan=10, column=0)
#Load an image in the script
img= (Image.open(r"C:\Users\Giulio\Documents\GitHub\DataSport\Icons\LOGO-ATLETICA-LEVANTE.png"))
#Resize the Image using resize method
resized_image= img.resize((300,200), Image.Resampling.LANCZOS )
new_image= ImageTk.PhotoImage(resized_image)
#Add image to the Canvas Items
canvas.create_image(10,10, anchor=NW, image=new_image)

#Frame 1
frame1 = LabelFrame(root)
frame1.grid(row=0, column=1, padx=10, pady=10)
#defining objects in frame 1
label1 = Label(frame1, text="Importa nuovi dati da PC", font='Helvetica 11 bold')
Selectbtn = Button(frame1, text="Seleziona file", command= Openfile, borderwidth=2, font='Helvetica 10')
#packing in frame 1
label1.grid(row=0, column=0, padx=10, pady=10)
Selectbtn.grid(row=0, column=1, padx=10, pady=10)

#Frame 2
frame2 = LabelFrame(root)
frame2.grid(row=1, column=1, padx=10, pady=10)
#defining objects in frame 1
label2 = Label(frame2, text="Vedere analisi                      ", font='Helvetica 11 bold')
Dashbtn = Button(frame2, text="Dashboard", font='Helvetica 10')
#packing in frame 2
label2.grid(row=0, column=0, padx=10, pady=10)
Dashbtn.grid(row=0, column=1, padx=10, pady=10)

#Frame 3
frame3 = LabelFrame(root)
frame3.grid(row=2, column=1, padx=10, pady=10)
#defining objects in frame 1
label3 = Label(frame3, text="Uscire dal programma                  ", font='Helvetica 11 bold')
Extbtn = Button(frame3, text="Exit", font='Helvetica 10', command=root.destroy)
#packing in frame 2
label3.grid(row=0, column=0, padx=10, pady=10)
Extbtn.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()