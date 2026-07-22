import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

def doctor_form(tab,login,home,notebook,path,userfrom,pharmacient_frame,username):

        doctor_form_fram = ctk.CTkScrollableFrame(tab,fg_color="#EAEAEA")
        doctor_form_fram.pack(fill="both",expand=True)

        doctor_form_fram.rowconfigure(0,weight=0)
        doctor_form_fram.rowconfigure(1,weight=0)
        doctor_form_fram.columnconfigure(0,weight=2)

        user_form1 = ctk.CTkFrame(doctor_form_fram,fg_color="white")
        user_form1.grid(row=0,column=0,padx=20,pady=80)

        user_frame = ctk.CTkFrame(user_form1,fg_color="white")
        user_frame.grid(row=1,column=0,padx=10,pady=10)

        temp_frame = ctk.CTkFrame(user_form1,fg_color="white")
        temp_frame.grid(row=0,column=0,sticky="w",padx=10,pady=10)

        image_path1 = path('uload_image.png')
        tab.my_image = ctk.CTkImage(light_image=Image.open(image_path1),size=(46,46))

        def change_table(choice):
                
                if choice == "USER":
                        notebook.select(userfrom)
                        

                elif choice == "PARMECIENT":
                        notebook.select(pharmacient_frame)

                else:
                        notebook.select(tab)
                        
        
        ctk.CTkLabel(temp_frame,text="Select Your role: ",text_color="black").pack(side="left",padx=10)
        roles=["USER","PARMECIENT","DOCTOR"]
        role_value = tk.StringVar(value="DOCTOR")
        role=ctk.CTkComboBox(temp_frame,height=35,variable=role_value,border_color="#DB0A41",button_color="#DB0A41",
                             dropdown_fg_color="#880066",fg_color="white",corner_radius=50,width=200,
                             text_color="black",command= change_table)
        role.configure(values=roles)
        role.pack(side="left")
    
        details = []
        
        ctk.CTkLabel(user_frame,text="JOIN AS A DOCTOR",text_color="black",font=("calibri",20,"bold")).grid(row=0,column=0,columnspan=3,pady=20)

        ctk.CTkLabel(user_frame,text="Name: ",text_color="black").grid(row=1,column=0,padx=30)

        
        first_name = ctk.CTkEntry(user_frame,placeholder_text = "FIRST NAME",text_color="black",
                                  fg_color="white",border_color="#DB0A41",corner_radius=50,height=35,
                                  width=200)
        first_name.grid(row=1,column=1,pady=10,sticky="w",padx=10)

        
        last_name = ctk.CTkEntry(user_frame,placeholder_text = "LAST NAME",text_color="black",
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
        
        dob = ctk.CTkEntry(user_frame,placeholder_text="DD/MM/YY",width=300,fg_color="white",text_color = "black",font=("calibri",16),border_color="#DB0A41",corner_radius=50,height=35,)
        dob.grid(row=3,column=1,columnspan=2,pady=10,sticky="w",padx=10)
        
        ctk.CTkLabel(user_frame,text="Address: ",text_color="black").grid(row=4,column=0)
        address_value = tk.StringVar()
        address = ctk.CTkEntry(user_frame,textvariable=address_value,text_color = "black",font=("calibri",16),width=300,fg_color="white",border_color="#DB0A41",corner_radius=50,height=35,)
        address.grid(row=4,column=1,columnspan=2,pady=10,sticky="w",padx=10)

        ctk.CTkLabel(user_frame,text="Email: ",text_color="black").grid(row=5,column=0)
        email_value = tk.StringVar()
        email = ctk.CTkEntry(user_frame,textvariable=email_value,width=300,fg_color="white",text_color = "black",font=("calibri",16),border_color="#DB0A41",corner_radius=50,height=35,)
        email.grid(row=5,column=1,columnspan=2,pady=10,sticky="w",padx=10)

        ctk.CTkLabel(user_frame,text="Phone: ",text_color="black").grid(row=6,column=0)
        phone_value = tk.StringVar()
        phone = ctk.CTkEntry(user_frame,textvariable=phone_value,width=300,text_color = "black",font=("calibri",16),fg_color="white",border_color="#DB0A41",corner_radius=50,height=35,)
        phone.grid(row=6,column=1,columnspan=2,pady=10,sticky="w",padx=10)

        ctk.CTkLabel(user_frame,text="Work Place: ",text_color="black").grid(row=7,column=0)
        workplace_value = tk.StringVar()
        workplace = ctk.CTkEntry(user_frame,textvariable=workplace_value,text_color = "black",font=("calibri",16),width=300,fg_color="white",border_color="#DB0A41",corner_radius=50,height=35,)
        workplace.grid(row=7,column=1,columnspan=2,pady=10,sticky="w",padx=10)

        ctk.CTkLabel(user_frame,text="WorkID Number: ",text_color="black").grid(row=8,column=0)
        workid_value = tk.StringVar()
        workid = ctk.CTkEntry(user_frame,textvariable=workid_value,width=300,text_color = "black",font=("calibri",16),fg_color="white",border_color="#DB0A41",corner_radius=50,height=35,)
        workid.grid(row=8,column=1,columnspan=2,pady=10,sticky="w",padx=10)

        types = ["CARDIOLOGIST","PHYSICIAN","PEDIATRICIAN","NEUROLOGIST","EYE SURGEON"]
        ctk.CTkLabel(user_frame,text="Position: ",text_color="black").grid(row=9,column=0)
        position_value = tk.StringVar()
        position=ctk.CTkComboBox(user_frame,height=35,variable=position_value,border_color="#DB0A41",button_color="#DB0A41",
                             dropdown_fg_color="#880066",fg_color="white",corner_radius=50,width=200,
                             text_color="black")
        position.configure(values=types)
        position.grid(row=9,column=1,columnspan=2,pady=10,sticky="w",padx=10)
        
        image_doc = [None]
        
        def upload():
                file_path = askopenfilename()
                binary_img = convert_to_binary(file_path)
                image_doc[0] = binary_img

        def convert_to_binary(file_path):
            with open(file_path, 'rb') as file:
                binary_data = file.read()
            return binary_data

        ctk.CTkLabel(user_frame,text="Upload Your Photo: ",text_color="black").grid(row=10,column=0)
        workid = ctk.CTkButton(user_frame,width=80,text="",image=tab.my_image,command = upload,fg_color="white",
                               border_width=2,border_color="#DB0A41",corner_radius=50,height=35,)
        workid.grid(row=10,column=1,columnspan=2,pady=10,sticky="w",padx=10)
        
        btn_farme= ctk.CTkFrame(user_frame,fg_color="white")
        btn_farme.grid(row=11,column=0,columnspan=3,pady=10)

        def reset():
                first_name.delete(0,tk.END)
                last_name.delete(0,tk.END)
                address_value.set("")
                phone_value.set("")
                last_name.delete(0,tk.END)
                dob.delete(0,tk.END)
                address_value.set("")
                email_value.set("")
                phone_value.set("")
                workplace_value.set("")
                workid_value.set("")
                position_value.set("")
                

        def validate():
                if first_name.get()=="" or address_value.get()=="" or phone_value.get()=="" or last_name.get()=="" or dob.get()=="" or address_value.get()=="" or email_value.get()=="" or phone_value.get()=="" or workplace_value.get()=="" or workid_value.get()=="" or position_value.get()=="":
                                messagebox.showwarning(title="WARNING", message="Please Fill Required Details")

                elif image_doc[0] == None:
                        messagebox.showwarning(title="WARNING", message="Please Upload Image")
                      
                else:
                        details.append(last_name.get())
                        details.append(workplace_value.get())
                        details.append(phone_value.get())
                        details.append(image_doc[0])
                        details.append(position_value.get())
                        notebook.select(username)

        ctk.CTkButton(btn_farme,text="Join Now",height=35,fg_color="#880066",command=validate,
                      font=("calibri",17,"bold"),
                      border_color="white",corner_radius=50).pack(side="left",padx=10)
        ctk.CTkButton(btn_farme,text="Reset",height=35,fg_color="#880066",font=("calibri",17,"bold"),command=reset,
                      border_color="white",corner_radius=50).pack(side="left",padx=10)
        ctk.CTkButton(btn_farme,text="Cancel",height=35,fg_color="#880066",font=("calibri",17,"bold"),
                      border_color="white",corner_radius=50,command = lambda:notebook.select(home)).pack(side="left",padx=10)

        temp_frame2=ctk.CTkFrame(user_form1,fg_color="white")
        temp_frame2.grid(row=2,column=0,sticky="w",padx=20,pady=20)

        ctk.CTkLabel(temp_frame2,text="If you Alredy Member Of Our Network?",text_color="black").pack(side="left")
        ctk.CTkButton(temp_frame2,text="Signin Now",fg_color="#DB0A41",text_color="white",
                      command=lambda:notebook.select(login),font=("calibri",17,"bold")).pack(side="left",padx=20)
        

        return details
        
       



        
       

        

        
        

        
        
                
        
        

        






        
