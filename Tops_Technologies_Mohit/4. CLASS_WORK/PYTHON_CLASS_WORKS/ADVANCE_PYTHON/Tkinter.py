"""
Tkinter --->>> It is used to build GUI desktop applications using python.
               It is one kind of module.
                

GUI --->>> Graphical User Interface.

"""

import tkinter

from tkinter.ttk import Combobox
from tkinter import messagebox


window  = tkinter.Tk()

window.geometry("500x600") # For give to Size.
window.config(bg="lightblue") # For give to Color.
window.title("FirstApp") # For change To File Title name.

# tkinter.Label(text="FirstName").pack()
# tkinter.Label(text="LastName").pack()

tkinter.Label(text="FirstName").place(x=0,y=0)
tkinter.Label(text="LastName").place(x=0,y=30)


tkinter.Label(text="FirstName",bg="lightpink",font="cambria 15 bold",fg="red").grid(row=0,column=0,sticky="w")
tkinter.Label(text="LastName",bg="lightpink",font="cambria 15 bold",fg="red").grid(row=1,column=0,sticky="w")

tkinter.Entry().grid(row=0,column=1,sticky="w")
tkinter.Entry().grid(row=1,column=1,sticky="w")

# For  items select :-

tkinter.Radiobutton(value=0,text="Male",bg="lightpink",font="cambria 15 bold",fg="red").grid(row=2,column=0,sticky="w")
tkinter.Radiobutton(value=1,text="Female",bg="lightpink",font="cambria 15 bold",fg="red").grid(row=2,column=1,sticky="w")

# For Multiple items Select :-

tkinter.Checkbutton(text="Python",bg="lightpink",font="cambria 15 bold",fg="red").grid(row=3,column=0,sticky="w")
tkinter.Checkbutton(text="Java",bg="lightpink",font="cambria 15 bold",fg="red").grid(row=4,column=0,sticky="w")
tkinter.Checkbutton(text="Android",bg="lightpink",font="cambria 15 bold",fg="red").grid(row=5,column=0,sticky="w")
tkinter.Checkbutton(text="PHP",bg="lightpink",font="cambria 15 bold",fg="red").grid(row=6,column=0,sticky="w")
tkinter.Checkbutton(text="ios",bg="lightpink",font="cambria 15 bold",fg="red").grid(row=7,column=0,sticky="w")

# For DropDown menu using Combobox :-

city = ["Rajkot","Ahemdabad","Surat","Vadodara","Gandhinagar"]
Combobox(values=city).grid(row=8,column=0,sticky="w")

def btnclick():
    # print("This is Button!")
    # messagebox.showerror("Error!","Something went wrong!")
    # messagebox.showwarning("Warning","Your disk is full!")
    # messagebox.showinfo("Success","Your profile has been created!")

    # messagebox.askokcancel("Download","Do you want to continue?")
    # messagebox.askquestion("Download","Do you want to continue?")
    # messagebox.askquestion("Download","Do you want to continue?")
    # messagebox.askyesno("Download","Do you want to continue?")
    messagebox.askyesnocancel("Download","Do you want to continue?")
tkinter.Button(text="Submit",command=btnclick).place(x=220,y=300)


tkinter.mainloop()

