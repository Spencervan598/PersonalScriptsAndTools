#!/usr/bin/env python3

from tkinter import *
from math import pi

def CFM():
    a = (pi * (float(radius.get())/12)**2)
    f = float(fpm.get())
    
    label1 = Label(root, text="CFM: " + str(f*a))
    box.create_window(300, 375, window=label1)

root = Tk()
root.title("Conversions")

box = Canvas(root, width=600, height=600)
box.pack()

fpm = Entry(root)
box.create_window(300, 100, window=fpm)

radius = Entry(root)
box.create_window(300, 200, window=radius)

fpml = Label(root, text="Enter FPM:")
box.create_window(200, 100, window=fpml)

radiusl = Label(root, text="Enter Duct Radius:")
box.create_window(175, 200, window=radiusl)


button1 = Button(root, text="Calculate!", command=CFM)
box.create_window(300, 250, window=button1)
root.mainloop()