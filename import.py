#setting up the GUI interface in which 
#I ask to select the database .csv

from pydoc import text
from tkinter import*
from tkinter import filedialog
from tkinter.ttk import Labelframe

root = Tk()
root.title("Importazione dati")
root.geometry("700x200")
root.iconbitmap(r"C:\Users\Giulio\Documents\GitHub\DataSport\AtlLev.ico")

def Openfile():
    filename = filedialog.askopenfilenames(initialdir="\Origini ", 
    title="Seleziona file", filetypes=(("formato","*.csv"),("All Files","*.*")))

#Frame 1
frame1 = LabelFrame(root, text="Selezione")
frame1.pack(fill='x', padx=10, pady=10)
#defining objects in frame 1
label1 = Label(frame1, text="Percorso File:")
Selectbtn = Button(frame1, text="Seleziona file", command= Openfile)
#packing in frame 1
label1.grid(row=0, column=0)
Selectbtn.grid(row=1, column=1)

# Frame 2
frame2 = Labelframe(root, text="Importazione")
#frame2.pack(padx=10, pady=10)
#frame2.pack_propagate(0)
frame2.pack(fill='x', padx=10, pady=10)
##defining objects in frame 2
Importbtn = Button(frame2,text="Importa")
#e = Label(frame2, text=filename)
#packing in frame 2
Importbtn.grid(row=0, column=1)
#e.grid(row=0, column=0)
root.mainloop()