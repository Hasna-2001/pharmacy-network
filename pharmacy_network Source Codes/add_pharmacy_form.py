import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

def add_pharmacy_frm(tab,home,notebook,path,pharmacient_from,username):

        signin_frame = ctk.CTkFrame(tab,fg_color="#EAEAEA")
        signin_frame.pack(fill="both",expand=True)

        details = []
        signin_frame.columnconfigure(0,weight=2)

        user_form1 = ctk.CTkFrame(signin_frame,fg_color="white")
        user_form1.grid(row=0,column=0,padx=20,pady=80)

        user_frame = ctk.CTkFrame(user_form1,fg_color="white")
        user_frame.grid(row=0,column=0,padx=10,pady=10)

        image_path1 = path('uload_image.png')
        tab.my_image = ctk.CTkImage(light_image=Image.open(image_path1),size=(46,46))
        

        ctk.CTkLabel(user_frame,text="Pharmacy Details",text_color="black",font=("calibri",20,"bold")).grid(row=0,column=0,columnspan=3,pady=10)

        
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
        ctk.CTkButton(user_frame,text = "",border_width=3,border_color="#DB0A41",width=80,
                      image=tab.my_image,command = upload,fg_color="white").grid(row=8,column=1,columnspan=2,sticky="w",padx=10)
        
        btn_farme= ctk.CTkFrame(user_frame,fg_color="white")
        btn_farme.grid(row=9,column=0,columnspan=3,pady=30)

        def validate():

                if name_value.get()=="" or address_value.get()=="" or district_value.get()=="" or phone_value.get()=="" or address_value2.get()=="":
                        messagebox.showwarning(title="WARNING", message="Please Fill Required Details")

                elif image_place[0] == None:
                        messagebox.showwarning(title="WARNING", message="Please Upload Image")
                
                else:
                        details.append((name_value.get()).capitalize())
                        details.append((address_value.get()).capitalize())
                        details.append(phone_value.get())
                        details.append(image_place[0])
                        details.append(district_value.get())
                        details.append((address_value2.get()).capitalize())
                        notebook.select(username)

        def reset():
                name_value.set("")
                address_value.set("")
                district_value.set("")
                phone_value.set("")
                address_value2.set("")
                
                                
        
        ctk.CTkButton(btn_farme,text="Join Now",height=35,fg_color="#880066",command=validate,
                      font=("calibri",17,"bold"),
                      border_color="white",corner_radius=50).pack(side="left",padx=10)
        ctk.CTkButton(btn_farme,text="Reset",height=35,fg_color="#880066",font=("calibri",17,"bold"),command=reset,
                      border_color="white",corner_radius=50).pack(side="left",padx=10)
        ctk.CTkButton(btn_farme,text="Cancel",height=35,fg_color="#880066",font=("calibri",17,"bold"),command=lambda:notebook.select(pharmacient_from),
                      border_color="white",corner_radius=50).pack(side="left",padx=10)

        
        return details
        
        


        
       



        
       

        

        
        

        
        
                
        
        

        






        
