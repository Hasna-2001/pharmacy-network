import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
from tkinter.filedialog import askopenfilename

def admin_pharmacy_frm(tab,notebook,path,restart,pharmacies,admin_pannel,refresh_remove_pharmacy):

        signin_frame = ctk.CTkFrame(tab,fg_color="#EAEAEA")
        signin_frame.pack(fill="both",expand=True)

        
        signin_frame.columnconfigure(0,weight=2)

        user_form1 = ctk.CTkFrame(signin_frame,fg_color="white")
        user_form1.grid(row=0,column=0,padx=20,pady=80)

        user_frame = ctk.CTkFrame(user_form1,fg_color="white")
        user_frame.grid(row=0,column=0,padx=10,pady=10)
    
        image_path1 = path('uload_image.png')
        tab.my_image = ctk.CTkImage(light_image=Image.open(image_path1),size=(46,46))

        ctk.CTkLabel(user_frame,text="Pharmacy Details",text_color="black",font=("calibri",25,"bold")).grid(row=0,column=0,columnspan=3,pady=10)

        
        ctk.CTkLabel(user_frame,text="Pharmacy Name: ",text_color="black").grid(row=3,column=0)
        name_value = tk.StringVar()
        name = ctk.CTkEntry(user_frame,textvariable=name_value,text_color="black",font=("calibri",16),width=300,fg_color="white",border_color="#DB0A41",corner_radius=50,height=35,)
        name.grid(row=3,column=1,columnspan=2,pady=10,sticky="w",padx=10)
        
        ctk.CTkLabel(user_frame,text="Address Line 1: ",text_color="black").grid(row=4,column=0)
        address_value = tk.StringVar()
        address = ctk.CTkEntry(user_frame,textvariable=address_value,text_color="black",font=("calibri",16),width=300,fg_color="white",border_color="#DB0A41",corner_radius=50,height=35,)
        address.grid(row=4,column=1,columnspan=2,pady=10,sticky="w",padx=10)

        ctk.CTkLabel(user_frame,text="Address Line 2: ",text_color="black").grid(row=5,column=0)
        address_value2 = tk.StringVar()
        address = ctk.CTkEntry(user_frame,textvariable=address_value2,text_color="black",font=("calibri",16),width=300,fg_color="white",border_color="#DB0A41",corner_radius=50,height=35,)
        address.grid(row=5,column=1,columnspan=2,pady=10,sticky="w",padx=10)

        ctk.CTkLabel(user_frame,text="District: ",text_color="black").grid(row=6,column=0)
        district_value = tk.StringVar()
        sri_lanka_districts = [ "Ampara", "Anuradhapura", "Badulla", "Batticaloa", "Colombo", "Galle", "Gampaha", "Hambantota", "Jaffna", "Kalutara", "Kandy", "Kegalle",
                                "Kilinochchi", "Kurunegala", "Mannar",
                                "Matale", "Matara", "Monaragala", "Mullaitivu", "Nuwara Eliya", "Polonnaruwa", "Puttalam", "Ratnapura", "Trincomalee", "Vavuniya" ]
        select_district = ctk.CTkComboBox(user_frame,variable=district_value,text_color="black",font=("calibri",16),width=300,fg_color="white",border_color="#DB0A41",corner_radius=50,height=35,)
        select_district.configure(values=sri_lanka_districts)
        select_district.grid(row=6,column=1,columnspan=2,pady=10,sticky="w",padx=10)

        ctk.CTkLabel(user_frame,text="Phone: ",text_color="black").grid(row=7,column=0)
        phone_value = tk.StringVar()
        phone = ctk.CTkEntry(user_frame,textvariable=phone_value,width=300,text_color="black",font=("calibri",16),fg_color="white",border_color="#DB0A41",corner_radius=50,height=35,)
        phone.grid(row=7,column=1,columnspan=2,pady=10,sticky="w",padx=10)

        image_place = [None]
        def upload():
                file_path = askopenfilename()
                binary_img = convert_to_binary(file_path)
                image_place[0] = binary_img

        def convert_to_binary(file_path):
            with open(file_path, 'rb') as file:
                binary_data = file.read()
            return binary_data
        
        ctk.CTkLabel(user_frame,text="Upload Pharmacy\nPhoto: ",text_color="black").grid(row=8,column=0)
        ctk.CTkButton(user_frame,text = "",width=80,image=tab.my_image,border_width=2,border_color="#DB0A41",
                      command = upload,fg_color="white").grid(row=8,column=1,columnspan=2,sticky="w",padx=10)
        
        btn_farme= ctk.CTkFrame(user_frame,fg_color="white")
        btn_farme.grid(row=9,column=0,columnspan=3,pady=30)

        def reset():
            name_value.set("")
            address_value.set("")
            phone_value.set("")
            address_value.set("")
            address_value2.set("")
            


        def add_now():
                if name_value.get()=="" or address_value.get()=="" or phone_value.get()=="" or address_value.get()=="":
                        messagebox.showwarning(title="WARNING", message="Please Fill Required Details")
                        
                elif image_place[0] == None:
                        messagebox.showwarning(title="WARNING", message="Please Upload Image")
                else:
                    
                    connection = sqlite3.connect("pharmacy.db")
                    cursor = connection.cursor()
                    place_details=(name_value.get(),(address_value.get()).capitalize(),phone_value.get(),address_value2.get(),district_value.get())
                    cursor.execute("insert into nearby_pharmacy (name,address,phone,address2,district) values(?,?,?,?,?)",place_details)
                    cursor.execute("insert into images (name,image)values(?,?)",(name_value.get(),image_place[0]))
                    connection.commit()
                    connection.close()
                    refresh_remove_pharmacy()
                    restart()
                    notebook.select(pharmacies)
                    

        
        ctk.CTkButton(btn_farme,text="ADD NOW",height=35,fg_color="#880066",command=add_now,
                      font=("calibri",17,"bold"),
                      border_color="white",corner_radius=50).pack(side="left",padx=10)
        ctk.CTkButton(btn_farme,text="RESET",height=35,fg_color="#880066",font=("calibri",17,"bold"),
                      border_color="white",corner_radius=50,command=reset).pack(side="left",padx=10)
        ctk.CTkButton(btn_farme,text="CANCEL",height=35,fg_color="#880066",font=("calibri",17,"bold"),
                      border_color="white",corner_radius=50,command=lambda:notebook.select(admin_pannel)).pack(side="left",padx=10)

        
       
        
        


        
       



        
       

        

        
        

        
        
                
        
        

        






        
