import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox

def cart_login_tab(tab,sign,notebook,path,state,cart,shipping_frm,refresh_total):

        login_frame = ctk.CTkFrame(tab,fg_color="#EAEAEA")
        login_frame.pack(fill="both",expand=True)

        login_frame.rowconfigure(0,weight=0)
        login_frame.rowconfigure(1,weight=0)
        login_frame.columnconfigure(0,weight=2)
        login_frame.columnconfigure(1,weight=0)
        login_frame.columnconfigure(2,weight=0)

        
        nav=tk.Label(login_frame,bg="white")
        nav.grid(row=0,column=0,columnspan=3,sticky="nswe")

        nav.rowconfigure(0,weight=0)
        nav.columnconfigure(0,weight=2)
        nav.columnconfigure(1,weight=0)
        nav.columnconfigure(2,weight=0)


        image_path1 = path('back.png')
        tab.back_button = ctk.CTkImage(light_image=Image.open(image_path1),size=(40,40))

        ctk.CTkButton(nav,text="",width=20,
                   command=lambda: notebook.select(cart),
                      fg_color="white",hover_color="white",
                   image=tab.back_button).grid(row=0,column=0,padx=5,pady=5,sticky="w")

        ctk.CTkLabel(login_frame,text="Sign in to Continue!",font=("roboto",20,"bold"),
                     text_color="black").grid(row=1,column=0,pady=50)
        
        entry_frame1= ctk.CTkFrame(login_frame,fg_color="white")
        entry_frame1.grid(row=2,column=0,columnspan=3)

        

        entry_frame= ctk.CTkFrame(entry_frame1,fg_color="white")
        entry_frame.grid(row=1,column=0,columnspan=3,pady=10,padx=10)

        entry_frame.columnconfigure(0,weight=2)
        entry_frame.columnconfigure(1,weight=2)

        login_box=ctk.CTkFrame(entry_frame,fg_color="white",corner_radius=10)
        login_box.grid(row=0,column=0)

        signin_box=ctk.CTkFrame(entry_frame,fg_color="#DB0A41",corner_radius=10)
        signin_box.grid(row=0,column=1)

        ctk.CTkLabel(login_box,text="Sign In",text_color="black",font=("calibri",20,"bold")).grid(row=0,column=0,pady=10)
        #ctk.CTkLabel(login_box,text="",text_color="black").grid(row=0,column=1)

        alig_frame1=ctk.CTkFrame(login_box,fg_color="white")
        alig_frame1.grid(row=1,column=0,columnspan=2,sticky="w",padx=10,pady=10)
        
        ctk.CTkLabel(alig_frame1,text="SELECT YOUR ROLE",text_color="black").grid(row=0,column=0,sticky="w")

        roles=["USER","PARMECIANT","DOCTOR"]
        role_value = tk.StringVar(value=roles[0])
        role=ctk.CTkComboBox(alig_frame1,height=35,variable=role_value,width=200,
                             corner_radius=50,text_color="black",fg_color="white",
                             border_color="#DB0A41",button_color="#DB0A41",dropdown_fg_color="#880066")
        role.configure(values=roles)
        role.grid(row=1,column=0,sticky="w",padx=5)

        alig_frame2=ctk.CTkFrame(login_box,fg_color="white")
        alig_frame2.grid(row=2,column=0,columnspan=2,pady=10,padx=10)

        ctk.CTkLabel(alig_frame2,text="USERNAME",text_color="black").grid(row=0,column=0,sticky="w")
        username=ctk.CTkEntry(alig_frame2,corner_radius=50,width=270,height=35,fg_color="white",
                              text_color = "black",border_color="#DB0A41")
        username.grid(row=1,column=0)

        alig_frame3=ctk.CTkFrame(login_box,fg_color="white")
        alig_frame3.grid(row=3,column=0,columnspan=2,pady=10)
        
        ctk.CTkLabel(alig_frame3,text="PASSWORD",text_color="black").grid(row=0,column=0,sticky="w")
        password=ctk.CTkEntry(alig_frame3,corner_radius=50,width=270,height=35,fg_color="white",
                              text_color = "black",border_color="#DB0A41")
        password.grid(row=1,column=0,columnspan=2)

        def validate():

                connection = sqlite3.connect("pharmacy.db")
                cursor = connection.cursor()
                cursor.execute("select password from login_details where username=?",(username.get(),))
                pswrd = cursor.fetchone()
                
                
                if username.get() == "" or password.get() == "":
                        messagebox.showwarning(title="WARNING", message="Please Fill Required Details")

                elif role_value.get() == "ADMIN" and password.get() == "admin123" and username.get() == "admin123":
                        notebook.select(admin_pannel)

                elif pswrd == None:
                        messagebox.showwarning(title="WARNING", message="Wrong Username or Password")

                elif password.get() == pswrd[0]:
                        state.set("Logedin")
                        refresh_total()
                        notebook.select(shipping_frm)

                else:
                        messagebox.showwarning(title="WARNING", message="Wrong Username or Password")
                        
                        
                connection.close()
        
        login_btn = ctk.CTkButton(login_box,text="Sign In",corner_radius=50,font=("calibri",17,"bold"),
                                  width=270,height=35,fg_color="#DB0A41",border_color="white",command=validate)                                                             
        login_btn.grid(row=4,column=0,columnspan=2,pady=10)

        forgot_password = ctk.CTkButton(login_box,text="Forgot Password",fg_color="white",
                                        text_color="dark blue",hover_color="white")                                                             
        forgot_password.grid(row=5,column=1,sticky="e",pady=10)


        image_path = path('bgframe2.jpg')

        ctk.CTkLabel(signin_box,text="").pack(pady=61)

        ctk.CTkLabel(signin_box,text="Welcome Back To Our Network",font=("impact",20)).pack(padx=15)
        ctk.CTkLabel(signin_box,text="If you not a member of our Network,",font=("calibri",17)).pack(padx=5)

        join_now=ctk.CTkButton(signin_box,text="Join Now",corner_radius=50,
                               fg_color="white",text_color="#880066",
                               command = lambda:notebook.select(sign))
        join_now.pack(pady=10)

        ctk.CTkLabel(signin_box,text="").pack(pady=61)


        

        

        
        

       










        
