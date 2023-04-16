#!interpreter [optional-arg]
# -*- coding: utf-8 -*-

"""
With this code I want to add a Graphic User Interface to automatically build my email to send to my coach.
I will need to scrape informations from my intervals.icu account and store them in a nice place
{License_info}
"""
from tkinter import *
import requests

##GUI Development
root = Tk()
root.title("Hello World")
root.geometry("680x680")
root.iconbitmap(r"Icons\AtlLev1.ico")
#Create a canvas
canvas = Canvas(root, width= 310, height= 210)
canvas.grid(row=0, rowspan=10, column=0)
root.mainloop()

response = requests.get('https://intervals.icu/')
print(response.json())