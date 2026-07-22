import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox 

def signin_tab(tab,login,home,notebook,path,pharmacient_from,doctor_frame,username):

        signin_frame = ctk.CTkFrame(tab,fg_color="#EAEAEA")
        signin_frame.pack(fill="both",expand=True)

        signin_frame.rowconfigure(0,weight=0)
        signin_frame.rowconfigure(1,weight=0)
        signin_frame.columnconfigure(0,weight=2)

        user_form1 = ctk.CTkFrame(signin_frame,fg_color="white")
        user_form1.grid(row=0,column=0,padx=20,pady=80)

        user_frame = ctk.CTkFrame(user_form1,fg_color="white")
        user_frame.grid(row=1,column=0,padx=10,pady=10)

        temp_frame = ctk.CTkFrame(user_form1,fg_color="white")
        temp_frame.grid(row=0,column=0,sticky="w",padx=10,pady=10)    

        details=[]
        
        def change_table(choice):
                
                if choice == "USER":
                        pass
                        

                elif choice == "PARMECIENT":
                        notebook.select(pharmacient_from)

                else:
                        notebook.select(doctor_frame)

        def validate():
                if first_name.get()=="" or last_name.get()=="" or address_value.get()=="" or phone_value.get()=="" or dob.get()=="":
                        messagebox.showwarning(title="WARNING", message="Please Fill Required Details")

                else:
                        details.append(last_name.get())
                        notebook.select(username)

        def reset():
                first_name.delete(0,tk.END)
                last_name.delete(0,tk.END)
                address_value.set("")
                email_value.set("")
                phone_value.set("")
                dob.delete(0,tk.END)
                
        
        ctk.CTkLabel(temp_frame,text="Select Your role: ",text_color="black").pack(side="left",padx=10)
        roles=["USER","PARMECIENT","DOCTOR"]
        role_value = tk.StringVar(value=roles[0])
        role=ctk.CTkComboBox(temp_frame,height=35,variable=role_value,border_color="#DB0A41",button_color="#DB0A41",
                             dropdown_fg_color="#880066",fg_color="white",corner_radius=50,width=200,
                             text_color="black",command= change_table)
        role.configure(values=roles)
        role.pack(side="left")
    
        

        ctk.CTkLabel(user_frame,text="JOIN AS A USER",text_color="black",font=("calibri",20,"bold")).grid(row=0,column=0,columnspan=3,pady=15)

        ctk.CTkLabel(user_frame,text="Name: ",text_color="black").grid(row=1,column=0,padx=30)

        
        first_name = ctk.CTkEntry(user_frame,placeholder_text="FIRST NAME",text_color="black",
                                  fg_color="white",border_color="#DB0A41",corner_radius=50,height=35,
                                  width=200)
        first_name.grid(row=1,column=1,pady=10,sticky="w",padx=10)

        
        last_name = ctk.CTkEntry(user_frame,placeholder_text="LAST NAME",text_color="black",
                                 width=200,fg_color="white",border_color="#DB0A41",corner_radius=50,height=35,)
        last_name.grid(row=1,column=2,padx=10)

        ctk.CTkLabel(user_frame,text="Gender: ",text_color="black").grid(row=2,column=0,pady=10)
        gender_frame = ctk.CTkFrame(user_frame,fg_color="white")
        gender_frame.grid(row=2,column=1,columnspan=2,sticky="w",padx=10)
        gender_value=tk.StringVar()

        male = ctk.CTkRadioButton(gender_frame,border_color="#DB0A41",
                                    variable=gender_value,
                                    value="Male",text="Male",text_color="black")
        male.pack(side = "left")

        female = ctk.CTkRadioButton(gender_frame,border_color="#DB0A41",
                                    variable=gender_value,
                                    value="Female",text="Female",text_color="black")
        female.pack(side = "left")
        
        ctk.CTkLabel(user_frame,text="DOB: ",text_color="black").grid(row=3,column=0)
        
        dob = ctk.CTkEntry(user_frame,placeholder_text="DD/MM/YY",text_color="black",font=("calibri",16),width=300,fg_color="white",border_color="#DB0A41",corner_radius=50,height=35,)
        dob.grid(row=3,column=1,columnspan=2,pady=10,sticky="w",padx=10)
        
        ctk.CTkLabel(user_frame,text="Address: ",text_color="black").grid(row=4,column=0)
        address_value = tk.StringVar()
        address = ctk.CTkEntry(user_frame,textvariable=address_value,text_color="black",font=("calibri",16),width=300,fg_color="white",border_color="#DB0A41",corner_radius=50,height=35,)
        address.grid(row=4,column=1,columnspan=2,pady=10,sticky="w",padx=10)

        ctk.CTkLabel(user_frame,text="Email: ",text_color="black").grid(row=5,column=0)
        email_value = tk.StringVar()
        email = ctk.CTkEntry(user_frame,textvariable=email_value,text_color="black",font=("calibri",16),width=300,fg_color="white",border_color="#DB0A41",corner_radius=50,height=35,)
        email.grid(row=5,column=1,columnspan=2,pady=10,sticky="w",padx=10)

        ctk.CTkLabel(user_frame,text="Phone: ",text_color="black").grid(row=6,column=0)
        phone_value = tk.StringVar()
        phone = ctk.CTkEntry(user_frame,textvariable=phone_value,width=300,text_color="black",font=("calibri",16),fg_color="white",border_color="#DB0A41",corner_radius=50,height=35,)
        phone.grid(row=6,column=1,columnspan=2,pady=10,sticky="w",padx=10)

        btn_farme= ctk.CTkFrame(user_frame,fg_color="white")
        btn_farme.grid(row=7,column=1,columnspan=3,pady=10)

        ctk.CTkButton(btn_farme,text="Join Now",height=35,fg_color="#880066",command=validate,
                      font=("calibri",17,"bold"),
                      border_color="white",corner_radius=50).pack(side="left",padx=10)
        ctk.CTkButton(btn_farme,text="Reset",height=35,fg_color="#880066",font=("calibri",17,"bold"),
                      border_color="white",corner_radius=50,command = reset).pack(side="left",padx=10)
        ctk.CTkButton(btn_farme,text="Cancel",height=35,fg_color="#880066",font=("calibri",17,"bold"),
                      border_color="white",corner_radius=50,command=lambda:notebook.select(home)).pack(side="left",padx=10)

        temp_frame2=ctk.CTkFrame(user_form1,fg_color="white")
        temp_frame2.grid(row=2,column=0,sticky="w",padx=20,pady=10)

        ctk.CTkLabel(temp_frame2,text="If you Alredy Member Of Our Network?",text_color="black").pack(side="left")
        ctk.CTkButton(temp_frame2,text="Signin Now",fg_color="#DB0A41",text_color="white",
                      command=lambda:notebook.select(login),font=("calibri",17,"bold")).pack(side="left",padx=20)

        
        return details


        
       



        
       

        

        
        

        
        
                
        
        

        






        
