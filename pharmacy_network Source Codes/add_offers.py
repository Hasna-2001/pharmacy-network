import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import sqlite3

def add_offers_form(tab,notebook,path,restart,offers,admin_pannel):

        signin_frame = ctk.CTkFrame(tab,fg_color="#EAEAEA")
        signin_frame.pack(fill="both",expand=True)

        
        signin_frame.columnconfigure(0,weight=2)

        user_form1 = ctk.CTkFrame(signin_frame,fg_color="white")
        user_form1.grid(row=0,column=0,padx=20,pady=80)

        user_frame = ctk.CTkFrame(user_form1,fg_color="white")
        user_frame.grid(row=0,column=0,padx=10,pady=10)
    
        image_path1 = path('uload_image.png')
        tab.my_image = ctk.CTkImage(light_image=Image.open(image_path1),size=(46,46))

        ctk.CTkLabel(user_frame,text="OFFER DETAILS",text_color="black",font=("roboto",20,"bold")).grid(row=0,column=0,columnspan=3,pady=10)

        
        ctk.CTkLabel(user_frame,text="Item Name: ",text_color="black").grid(row=3,column=0)
        name_value = tk.StringVar()
        name = ctk.CTkEntry(user_frame,textvariable=name_value,text_color="black",font=("calibri",16),width=300,fg_color="white",border_color="#DB0A41",corner_radius=50,height=35,)
        name.grid(row=3,column=1,columnspan=2,pady=10,sticky="w",padx=10)
        
        ctk.CTkLabel(user_frame,text="Price: ",text_color="black").grid(row=4,column=0)
        price_var = ctk.StringVar()
        price = ctk.CTkEntry(user_frame,textvariable = price_var,text_color="black",font=("calibri",16),width=300,fg_color="white",border_color="#DB0A41",corner_radius=50,height=35,)
        price.grid(row=4,column=1,columnspan=2,pady=10,sticky="w",padx=10)

        discount_var = ctk.StringVar()
        ctk.CTkLabel(user_frame,text="Offer Percentage: ",text_color="black").grid(row=5,column=0)
        discount = ctk.CTkEntry(user_frame,textvariable= discount_var,text_color="black",font=("calibri",16),width=300,fg_color="white",border_color="#DB0A41",corner_radius=50,height=35,)
        discount.grid(row=5,column=1,columnspan=2,pady=10,sticky="w",padx=10)

    

        img = [None]
        def upload():
                file_path = askopenfilename()
                binary_img = convert_to_binary(file_path)
                img[0] = binary_img
        
        ctk.CTkLabel(user_frame,text="Upload Item\nPhoto: ",text_color="black").grid(row=7,column=0)
        ctk.CTkButton(user_frame,text = "",width=80,image=tab.my_image,command = upload,border_width=2,
                      border_color="#DB0A41",fg_color="white").grid(row=7,column=1,columnspan=2,sticky="w",padx=10)
        
        btn_farme= ctk.CTkFrame(user_frame,fg_color="white")
        btn_farme.grid(row=8,column=0,columnspan=3,pady=30)

        def reset():
            name_value.set("")
            price_var.set("")
            discount_var.set("")

        def convert_to_binary(file_path):
            with open(file_path, 'rb') as file:
                binary_data = file.read()
            return binary_data

        def store_image(file_path,name):
                
                items = (name,file_path[0])
                connection = sqlite3.connect("pharmacy.db")
                cursor = connection.cursor()
                cursor.execute("insert into images values(?,?)",items)
                connection.commit()
                connection.close()
            


        def add_now():
                if name_value.get()=="" or price_var.get()=="" or discount_var.get()=="":
                        messagebox.showwarning(title="WARNING", message="Please Fill Required Details")
                
                elif img[0] == None:
                        messagebox.showwarning(title="WARNING", message="Please Upload Image")

                else:
                        store_image(img,name_value.get())
                        inputs = (name_value.get(),price.get(),discount.get())
                        all_items_add = (name_value.get(),price.get())
                        connection = sqlite3.connect("pharmacy.db")
                        cursor = connection.cursor()
                        cursor.execute("insert into offers values(?,?,?)",inputs)
                        cursor.execute("insert into all_items values(?,?)",all_items_add)
                        connection.commit()
                        connection.close()
                        restart()
                        notebook.select(offers)
                    

        
        ctk.CTkButton(btn_farme,text="ADD NOW",height=35,fg_color="#880066",command=add_now,
                      font=("calibri",17,"bold"),
                      border_color="white",corner_radius=50).pack(side="left",padx=10)
        ctk.CTkButton(btn_farme,text="RESET",height=35,fg_color="#880066",font=("calibri",17,"bold"),
                      border_color="white",corner_radius=50,command=reset).pack(side="left",padx=10)
        ctk.CTkButton(btn_farme,text="CANCEL",height=35,fg_color="#880066",font=("calibri",17,"bold"),
                      border_color="white",corner_radius=50,command=lambda:notebook.select(admin_pannel)).pack(side="left",padx=10)

       
       
        
        


        
       



        
       

        

        
        

        
        
                
        
        

        






        
