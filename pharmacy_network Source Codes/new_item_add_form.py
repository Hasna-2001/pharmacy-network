import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk, ImageFile
from tkinter.filedialog import askopenfilename
from tkinter import messagebox 
import sqlite3

def add_new_items(tab,home,notebook,path,admin_panel,pharmeasy,fitness,medicap,babycare,skincare,
                  restart_pharmeasy,restart_medicap,restart_fitness,restart_babycare,restart_skincare,all_drugs_restart):

        add_item_frame = ctk.CTkFrame(tab,fg_color="#EAEAEA",corner_radius= 0)
        add_item_frame.pack(fill="both",expand=True)

        add_item_frame.rowconfigure(0,weight=0)
        add_item_frame.rowconfigure(1,weight=0)
        add_item_frame.columnconfigure(0,weight=2)

        user_form1 = ctk.CTkFrame(add_item_frame,fg_color="white")
        user_form1.grid(row=1,column=0,padx=20,pady=40)

        user_frame = ctk.CTkFrame(user_form1,fg_color="white")
        user_frame.grid(row=1,column=0,padx=10,pady=10)

        temp_frame1 = ctk.CTkFrame(user_frame,fg_color="white")
        temp_frame1.grid(row=2,column=0,sticky="w",padx=10,pady=10,columnspan=2)

        temp_frame2 = ctk.CTkFrame(user_frame,fg_color="white")
        temp_frame2.grid(row=3,column=0,sticky="w",padx=10,pady=10,columnspan=2)

        def change(events):
                if pharmacies_value.get() == "PharmEasy":
                        item_type.configure(values=pharm_easy_types)

                elif pharmacies_value.get() == "Medicap":
                        item_type.configure(values=medicap_types)

                elif pharmacies_value.get() == "Fit By Choice":
                        item_type.configure(values=infinity_gym_types)

                elif pharmacies_value.get() == "Baby Care":
                        item_type.configure(values=baby_care_types)

                elif pharmacies_value.get() == "Skin Care":
                        item_type.configure(values=skin_care_types)

        image_path2 = path('home-button.png')
        tab.home = ctk.CTkImage(light_image=Image.open(image_path2),size=(50,50))

        ctk.CTkButton(add_item_frame,text ="",font=("Rooboto",16,"bold"),fg_color="#EAEAEA",hover_color="#EAEAEA",
                      image=tab.home,width=50,command = lambda:notebook.select(home)).grid(row=0,column=0,sticky="w",padx=20,pady=15)
        
        image_path1 = path('uload_image.png')
        tab.my_image = ctk.CTkImage(light_image=Image.open(image_path1),size=(46,46))
        
        ctk.CTkLabel(temp_frame1,text="Select Pharmacy: ",text_color="black",font=("calibri",17)).pack(side="left",padx=10)
        pharmacies=["PharmEasy","Medicap","Fit By Choice","Baby Care","Skin Care"]
        pharmacies_value = tk.StringVar()
        pharmacies_combo=ctk.CTkComboBox(temp_frame1,height=35,variable=pharmacies_value,border_color="#DB0A41",button_color="#DB0A41",
                             dropdown_fg_color="#880066",fg_color="white",corner_radius=50,width=200,command = change,
                             text_color="black")
        pharmacies_combo.configure(values=pharmacies)
        pharmacies_combo.pack(side="left",padx=30)

        ctk.CTkLabel(temp_frame2,text="Select Type: ",text_color="black",font=("calibri",17)).pack(side="left",padx=41)
        pharm_easy_types = ["Tablets","Vitamins"]
        medicap_types = ["Capsules","Drops"]
        infinity_gym_types = ["Protein Powders","Protein Bars"]
        baby_care_types = ["Baby Medicines","Baby Care Items","Mom care"]
        skin_care_types = ["Skrubs","Serums","Sunscreen","Lip Balm"]
               
        item_type_value = tk.StringVar()
        item_type=ctk.CTkComboBox(temp_frame2,height=35,variable=item_type_value,border_color="#DB0A41",button_color="#DB0A41",
                             dropdown_fg_color="#880066",fg_color="white",corner_radius=50,width=200,
                             text_color="black")
        

        
        item_type.pack(side="left",padx=5)
        
        ctk.CTkLabel(user_frame,text="ADD ITEM FORM",text_color="black",font=("calibri",25,"bold")).grid(row=0,column=0,columnspan=2,pady=20)

        ctk.CTkLabel(user_frame,text="Items Name: ",text_color="black",font=("calibri",17)).grid(row=4,column=0,padx=30)

        item_name_value = tk.StringVar()
        item_name = ctk.CTkEntry(user_frame,textvariable=item_name_value,text_color="black",
                                  fg_color="white",border_color="#DB0A41",corner_radius=50,height=35,
                                  width=300)
        item_name.grid(row=4,column=1,pady=10,sticky="w",padx=20,columnspan=2)
        
        ctk.CTkLabel(user_frame,text="Price: ",text_color="black",font=("calibri",17)).grid(row=5,column=0)
        
        price = ctk.CTkEntry(user_frame,width=300,fg_color="white",border_color="#DB0A41",
                             corner_radius=50,height=35,text_color="black")
        price.grid(row=5,column=1,columnspan=2,pady=10,sticky="w",padx=20)
        
        
        img = [None]
        def upload():
                file_path = askopenfilename()
                binary_img = convert_to_binary(file_path)
                img[0] = binary_img
                        
                
        ctk.CTkButton(user_frame,text="Upload Pic",width=80,fg_color="white",compound="right",image=tab.my_image,corner_radius=50,
                      font = ("calibri",17,"bold"),
                      command=upload,border_width=2,border_color="#DB0A41",text_color="black").grid(row=6,column=1,columnspan=2,pady = 15,sticky = "w",padx = 22)
        


        btn_farme= ctk.CTkFrame(user_frame,fg_color="white")
        btn_farme.grid(row=9,column=0,columnspan=3,pady=10)

        def convert_to_binary(file_path):
            with open(file_path, 'rb') as file:
                binary_data = file.read()
            return binary_data

        def reset():
                item_name_value.set("")
                price.delete(0,tk.END)

        def store_image(file_path,name):
                
                items = (name,file_path[0])
                connection = sqlite3.connect("pharmacy.db")
                cursor = connection.cursor()
                cursor.execute("insert into images values(?,?)",items)
                connection.commit()
                connection.close()

        def add():
                
                if item_name_value.get()=="" or price.get()=="":
                        messagebox.showwarning(title="WARNING", message="Please Fill Required Details")

                elif img==None:
                        messagebox.showwarning(title="WARNING", message="Please Upload Image")  

                else:      
                        store_image(img,item_name_value.get())
                        
                        if pharmacies_value.get() == "PharmEasy":

                                if item_type_value.get() == "Tablets":

                                        item_tuple = (item_name_value.get(),price.get())
                                        connection = sqlite3.connect("pharmacy.db")
                                        cursor = connection.cursor()
                                        cursor.execute("insert into pharmeasy_tablets values(?,?)",item_tuple)
                                        cursor.execute("insert into all_items values(?,?)",item_tuple)
                                        connection.commit()
                                        connection.close()
                                        restart_pharmeasy()
                                        notebook.select(pharmeasy)

                                elif item_type_value.get() == "Vitamins":
                                        item_tuple = (item_name_value.get(),price.get())
                                        connection = sqlite3.connect("pharmacy.db")
                                        cursor = connection.cursor()
                                        cursor.execute("insert into vitamins values(?,?)",item_tuple)
                                        cursor.execute("insert into all_items values(?,?)",item_tuple)
                                        connection.commit()
                                        connection.close()
                                        restart_pharmeasy()
                                        notebook.select(pharmeasy)
                                

                        elif pharmacies_value.get() == "Medicap":
                                
                                if item_type_value.get() == "Capsules":

                                        item_tuple = (item_name_value.get(),price.get())
                                        connection = sqlite3.connect("pharmacy.db")
                                        cursor = connection.cursor()
                                        cursor.execute("insert into capsules values(?,?)",item_tuple)
                                        cursor.execute("insert into all_items values(?,?)",item_tuple)
                                        connection.commit()
                                        connection.close()
                                        restart_medicap()
                                        notebook.select(medicap)


                                elif item_type_value.get() == "Drops":

                                        item_tuple = (item_name_value.get(),price.get())
                                        connection = sqlite3.connect("pharmacy.db")
                                        cursor = connection.cursor()
                                        cursor.execute("insert into drops values(?,?)",item_tuple)
                                        cursor.execute("insert into all_items values(?,?)",item_tuple)
                                        connection.commit()
                                        connection.close()
                                        restart_medicap()
                                        notebook.select(medicap)

                        elif pharmacies_value.get() == "Fit By Choice":

                                if item_type_value.get() == "Protein Powders":

                                        item_tuple = (item_name_value.get(),price.get())
                                        connection = sqlite3.connect("pharmacy.db")
                                        cursor = connection.cursor()
                                        cursor.execute("insert into protein_powders values(?,?)",item_tuple)
                                        cursor.execute("insert into all_items values(?,?)",item_tuple)
                                        connection.commit()
                                        connection.close()
                                        restart_fitness()
                                        notebook.select(fitness)

                                elif item_type_value.get() == "Protein Bars":

                                        item_tuple = (item_name_value.get(),price.get())
                                        connection = sqlite3.connect("pharmacy.db")
                                        cursor = connection.cursor()
                                        cursor.execute("insert into protein_bars values(?,?)",item_tuple)
                                        cursor.execute("insert into all_items values(?,?)",item_tuple)
                                        connection.commit()
                                        connection.close()
                                        restart_fitness()
                                        notebook.select(fitness)


                        elif pharmacies_value.get() == "Baby Care":

                                if item_type_value.get() == "Baby Medicines":

                                        item_tuple = (item_name_value.get(),price.get())
                                        connection = sqlite3.connect("pharmacy.db")
                                        cursor = connection.cursor()
                                        cursor.execute("insert into baby_medicines values(?,?)",item_tuple)
                                        cursor.execute("insert into all_items values(?,?)",item_tuple)
                                        connection.commit()
                                        connection.close()
                                        restart_babycare()
                                        notebook.select(babycare)

                                elif item_type_value.get() == "Baby Care Items":

                                        item_tuple = (item_name_value.get(),price.get())
                                        connection = sqlite3.connect("pharmacy.db")
                                        cursor = connection.cursor()
                                        cursor.execute("insert into baby_care_items values(?,?)",item_tuple)
                                        cursor.execute("insert into all_items values(?,?)",item_tuple)
                                        connection.commit()
                                        connection.close()
                                        restart_babycare()
                                        notebook.select(babycare)

                                elif item_type_value.get() == "Mom care":

                                        item_tuple = (item_name_value.get(),price.get())
                                        connection = sqlite3.connect("pharmacy.db")
                                        cursor = connection.cursor()
                                        cursor.execute("insert into mom_care values(?,?)",item_tuple)
                                        cursor.execute("insert into all_items values(?,?)",item_tuple)
                                        connection.commit()
                                        connection.close()
                                        restart_babycare()
                                        notebook.select(babycare)

                        elif pharmacies_value.get() == "Skin Care":


                                if item_type_value.get() == "Skrubs":

                                        item_tuple = (item_name_value.get(),price.get())
                                        connection = sqlite3.connect("pharmacy.db")
                                        cursor = connection.cursor()
                                        cursor.execute("insert into mosturaizers values(?,?)",item_tuple)
                                        cursor.execute("insert into all_items values(?,?)",item_tuple)
                                        connection.commit()
                                        connection.close()
                                        restart_skincare()
                                        notebook.select(skincare)

                                elif item_type_value.get() == "Serums":

                                        item_tuple = (item_name_value.get(),price.get())
                                        connection = sqlite3.connect("pharmacy.db")
                                        cursor = connection.cursor()
                                        cursor.execute("insert into serums values(?,?)",item_tuple)
                                        cursor.execute("insert into all_items values(?,?)",item_tuple)
                                        connection.commit()
                                        connection.close()
                                        restart_skincare()
                                        notebook.select(skincare)

                                elif item_type_value.get() == "Sunscreen":

                                        item_tuple = (item_name_value.get(),price.get())
                                        connection = sqlite3.connect("pharmacy.db")
                                        cursor = connection.cursor()
                                        cursor.execute("insert into sunscreen values(?,?)",item_tuple)
                                        cursor.execute("insert into all_items values(?,?)",item_tuple)
                                        connection.commit()
                                        connection.close()
                                        restart_skincare()
                                        notebook.select(skincare)

                                elif item_type_value.get() == "Lip Balm":

                                        item_tuple = (item_name_value.get(),price.get())
                                        connection = sqlite3.connect("pharmacy.db")
                                        cursor = connection.cursor()
                                        cursor.execute("insert into lip_balm values(?,?)",item_tuple)
                                        cursor.execute("insert into all_items values(?,?)",item_tuple)
                                        connection.commit()
                                        connection.close()
                                        restart_skincare()
                                        notebook.select(skincare)

                        all_drugs_restart()
                                
                        
                
                

        

        ctk.CTkButton(btn_farme,text="Add Now",height=35,fg_color="#880066",font=("calibri",17,"bold"),
                      border_color="white",corner_radius=50,command=add).pack(side="left",padx=10)
        ctk.CTkButton(btn_farme,text="Reset",height=35,fg_color="#880066",font=("calibri",17,"bold"),
                      border_color="white",corner_radius=50,command=reset).pack(side="left",padx=10)
        ctk.CTkButton(btn_farme,text="Cancel",height=35,fg_color="#880066",font=("calibri",17,"bold"),
                      border_color="white",corner_radius=50,command=lambda:notebook.select(admin_panel)).pack(side="left",padx=10)

      


  
       


        
        

        
        
                
        
        

        






        
