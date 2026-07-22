import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3

def create_username3(tab,home,back,notebook,details,user_run,state):

    mainframe=ctk.CTkFrame(tab,fg_color="tomato")
    mainframe.pack(fill="both",expand=True)
    mainframe.columnconfigure(0,weight=2)
    mainframe.rowconfigure(0,weight=2)

    container = ctk.CTkFrame(mainframe,fg_color="white")
    container.grid(row=0,column=0)

    user_var=ctk.StringVar()
    ctk.CTkLabel(container,text="Create Username",font=("calibri",17),text_color="black").grid(row=0,column=0,pady=10,sticky="w",padx=20,columnspan=2)
    ctk.CTkEntry(container,textvariable=user_var,width=280,height=35,corner_radius=5).grid(row=1,column=0,padx=20,columnspan=2)

    password_var = ctk.StringVar()
    ctk.CTkLabel(container,text="Create Password",font=("calibri",17),text_color="black").grid(row=2,column=0,pady=10,sticky="w",padx=20,columnspan=2)
    ctk.CTkEntry(container,width=280,textvariable=password_var,height=35,corner_radius=5).grid(row=3,column=0,padx=20,columnspan=2)

    ctk.CTkLabel(container,text="Conform Password",font=("calibri",17),text_color="black").grid(row=4,column=0,pady=10,sticky="w",padx=20,columnspan=2)

    temp_frame=ctk.CTkFrame(container,fg_color="white")
    temp_frame.grid(row=5,column=0,columnspan=2)

    conform_var=ctk.StringVar()
    ctk.CTkEntry(temp_frame,width=280,height=35,corner_radius=5,textvariable=conform_var).grid(row=0,column=0,padx=20)

    if password_var.get()!= conform_var.get():
        valid_var.set("Not Matching")

    valid_var=ctk.StringVar(value="")
    ctk.CTkLabel(container,textvariable=valid_var,font=("calibri",15),text_color="red").grid(row=1,column=0,sticky="w")

    def add():
        if user_var.get()=="" or password_var.get()=="" or conform_var.get()=="":
            messagebox.showwarning(title="WARNING", message="Please Fill Required Details")

        elif password_var.get()!= conform_var.get():
                messagebox.showwarning(title="WARNING", message="Passwords Not Match")
            
        else:
            connection = sqlite3.connect("pharmacy.db")
            cursor = connection.cursor()
            cursor.execute("insert into users_details (name) values(?)",(details[0],))
            cursor.execute("insert into login_details values(?,?)",(user_var.get(),conform_var.get(),))
            connection.commit()
            connection.close()
            state.set("Logedin")
            user_run()
            notebook.select(home)

    ctk.CTkButton(container,text="Conform",font=("calibri",15,"bold"),command=add,
                  fg_color="#3cd99e",height=35,text_color="white").grid(row=6,column=0,pady=20)
    ctk.CTkButton(container,text="Cancel",font=("calibri",15,"bold"),command=lambda:notebook.select(back),
                  fg_color="#3cd99e",height=35,text_color="white").grid(row=6,column=1,pady=20)

