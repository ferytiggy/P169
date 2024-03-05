# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 21:42:11 2024

@author: Aidan
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root = Tk()  
root.geometry("900x600")
root.title("Clases")


gui_elements = ["Etiqueta", "Botón", "Menú despegable"]
dropdown = ttk.Combobox(root,state="readonly" , values = gui_elements)
dropdown.pack()


class CreateElements:
   
    def __init__(self):
        print("Esta es la clase CreateElements")
       
    def createLabel(self):
        label = Label(root,text ="Se ha creado una nueva etiqueta usando la clase", fg="red")
        label.pack()
       
    def createButton(self):
        class_btn = Button(root, text ="Botón", command = self.message)
        class_btn.pack(padx=20, pady = 10)
       
    def createDropdown(self):
        value = [1,2,3,4]
        class_dropdown = ttk.Combobox(root,state="readonly" ,values = value)
        class_dropdown.pack()
       
    def choose(self):
        global dropdown
        element = dropdown.get()
        if(element == "Etiqueta"):
            self.createLabel()
        elif(element == "Botón"):
            self.createButton()
        elif(element == "Menú despegable"):
            self.createDropdown()
                   
    def message(self):
        showinfo("Mostrar información", "Has presionado el botón creado con la clase")
       
obj_of_CreateElements = CreateElements()
btn = Button(root, text ="Crear elemento", command = obj_of_CreateElements.choose)
btn.pack(padx=20, pady = 10)


root.mainloop()






