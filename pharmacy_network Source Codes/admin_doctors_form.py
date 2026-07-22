import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import sqlite3


def admin_doctor_form(tab,notebook,path,restart,doctors,admin_pannel,remove_refresh,table_refresh):

        doctor_form_fram = ctk.CTkScrollableFrame(tab,fg_color="#EAEAEA")
        doctor_form_fram.pack(fill="both",expand=True)

        doctor_form_fram.rowconfigure(0,weight=0)
        doctor_form_fram.rowconfigure(1,weight=0)
        doctor_form_fram.columnconfigure(0,weight=2)

        user_form1 = ctk.CTkFrame(doctor_form_fram,fg_color="white")
        user_form1.grid(row=0,column=0,padx=20,pady=80)

        user_frame = ctk.CTkFrame(user_form1,fg_color="white")
        user_frame.grid(row=1,column=0,padx=10,pady=10)

        ctk.CTkLabel(user_frame,text="Doctor Details",text_color="black",font=("calibri",25,"bold")).grid(row=0,column=0,columnspan=3,pady=10)

        image_path1 = path('uload_image.png')
        tab.my_image = ctk.CTkImage(light_image=Image.open(image_path1),size=(46,46))

        ctk.CTkLabel(user_frame,text="Name: ",text_color="black").grid(row=3,column=0)
        
        name = ctk.CTkEntry(user_frame,width=300,fg_color="white",text_color = "black",font=("calibri",16),border_color="#DB0A41",corner_radius=50,height=35,)
        name.grid(row=3,column=1,columnspan=2,pady=10,sticky="w",padx=10)
        
        ctk.CTkLabel(user_frame,text="Working Hospitel: ",text_color="black").grid(row=4,column=0)
        address_value = tk.StringVar()
        address = ctk.CTkEntry(user_frame,textvariable=address_value,text_color = "black",font=("calibri",16),width=300,fg_color="white",border_color="#DB0A41",corner_radius=50,height=35,)
        address.grid(row=4,column=1,columnspan=2,pady=10,sticky="w",padx=10)

        ctk.CTkLabel(user_frame,text="Phone: ",text_color="black").grid(row=6,column=0)
        phone_value = tk.StringVar()
        phone = ctk.CTkEntry(user_frame,textvariable=phone_value,width=300,text_color = "black",font=("calibri",16),fg_color="white",border_color="#DB0A41",corner_radius=50,height=35,)
        phone.grid(row=6,column=1,columnspan=2,pady=10,sticky="w",padx=10)

        ctk.CTkLabel(user_frame,text="Position: ",text_color="black").grid(row=7,column=0)
        types = ["CARDIOLOGIST","PHYSICIAN","PEDIATRICIAN","NEUROLOGIST","EYE SURGEON"]
        ctk.CTkLabel(user_frame,text="Position: ",text_color="black").grid(row=9,column=0)
        position_value = tk.StringVar()
        position=ctk.CTkComboBox(user_frame,height=35,variable=position_value,border_color="#DB0A41",button_color="#DB0A41",
                             dropdown_fg_color="#880066",fg_color="white",corner_radius=50,width=200,
                             text_color="black")
        position.configure(values=types)
        position.grid(row=7,column=1,columnspan=2,pady=10,sticky="w",padx=10)


        image_doc = [None]
        
        def upload():
                file_path = askopenfilename()
                binary_img = convert_to_binary(file_path)
                image_doc[0] = binary_img

        ctk.CTkLabel(user_frame,text="Upload Photo: ",text_color="black").grid(row=9,column=0)
        workid_value = tk.StringVar()
        pica_upload = ctk.CTkButton(user_frame,width=80,text="",border_width=2,border_color="#DB0A41",image=tab.my_image,command = upload,fg_color="white",corner_radius=50,height=35,)
        pica_upload.grid(row=9,column=1,columnspan=2,pady=10,sticky="w",padx=10)
        
        btn_farme= ctk.CTkFrame(user_frame,fg_color="white")
        btn_farme.grid(row=10,column=0,columnspan=3,pady=10)

        def reset():
                name.delete(0,tk.END)
                address_value.set("")
                phone_value.set("")
                postion_value.set("")

        def convert_to_binary(file_path):
            with open(file_path, 'rb') as file:
                binary_data = file.read()
            return binary_data
                

        def add_now():
                if name.get()=="" or address_value.get()=="" or phone_value.get()=="" or postion_value.get()=="":
                        messagebox.showwarning(title="WARNING", message="Please Fill Required Details")
                        
                elif image_doc[0] == None:
                        messagebox.showwarning(title="WARNING", message="Please Upload Image")

                else:  
                    add_doctor=(name.get(),address_value.get(),phone_value.get(),postion_value.get())
                    connection = sqlite3.connect("pharmacy.db")
                    cursor = connection.cursor()
                    cursor.execute("insert into doctors_details values(?,?,?,?)",add_doctor)
                    cursor.execute("insert into images values(?,?)",(name.get(),image_doc[0]))
                    cursor.execute("insert into doctor_names (name)values(?)",(name.get(),))
                    connection.commit()
                    connection.close()
                    table_refresh()
                    remove_refresh()
                    restart()
                    notebook.select(doctors)

        ctk.CTkButton(btn_farme,text="Add Now",height=35,fg_color="#880066",command=add_now,
                      font=("calibri",17,"bold"),
                      border_color="white",corner_radius=50).pack(side="left",padx=10)
        ctk.CTkButton(btn_farme,text="Reset",height=35,fg_color="#880066",font=("calibri",17,"bold"),command=reset,
                      border_color="white",corner_radius=50).pack(side="left",padx=10)
        ctk.CTkButton(btn_farme,text="Cancel",height=35,fg_color="#880066",font=("calibri",17,"bold"),
                      border_color="white",corner_radius=50,command = lambda:notebook.select(admin_pannel)).pack(side="left",padx=10)

        

                

        
        
       



        
       

        

        
        

        
        
                
        
        

        






        
