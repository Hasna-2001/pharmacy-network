import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import sqlite3
import warnings
from functools import partial

def remove_doc(tab,notebook,path,admin_pannel,refresh,refresh_table):
    main_frame=ctk.CTkFrame(tab,fg_color="#EAEAEA")
    main_frame.pack(fill="both",expand=True)
    main_frame.columnconfigure(0,weight=2)

    main_frame.rowconfigure(0,weight=0)
    main_frame.rowconfigure(1,weight=2)
    main_frame.rowconfigure(2,weight=0)
    warnings.filterwarnings("ignore", category=UserWarning, module="customtkinter")

    nav=ctk.CTkFrame(main_frame,fg_color="#3B1E54",corner_radius=0)
    nav.grid(row=0,column=0,sticky="we")
    nav.columnconfigure(0,weight=0)
    nav.columnconfigure(1,weight=2)

    ctk.CTkLabel(nav,text="Remove Doctors",
                 font=("impact",35),text_color="white").grid(row=0,column=1,pady=5)

    image_path1 = path('back.png')
    tab.back = ctk.CTkImage(light_image=Image.open(image_path1),size=(44,44))

    ctk.CTkButton(nav,text="",image = tab.back,hover_color="#3C1E51",fg_color="#3B1E54",width=55,
                  command = lambda:notebook.select(admin_pannel)).grid(row=0,column=0,pady=5)

    sub_frame  = ctk.CTkScrollableFrame(main_frame,fg_color="#EAEAEA",height=525)
    sub_frame.grid(row=3,column=0,sticky="nswe",pady=10)
    sub_frame.columnconfigure(0,weight =2)
    
    
    def remove(name):
        connection = sqlite3.connect("pharmacy.db")
        cursor = connection.cursor()
        cursor.execute("delete from doctors_details where name = ?",(name,))
        cursor.execute("delete from images where name = ?",(name,))
        cursor.execute("delete from doctor_names where name = ?",(name,))
        connection.commit()
        connection.close()
        
        refresh()
        show_doctors()
    

         

    def show_doctors():
        row=0
        column=0

        Doctors=[]
        connection = sqlite3.connect("pharmacy.db")
        cursor = connection.cursor()
        cursor.execute("select name from doctors_details")
        lst = cursor.fetchall()
        for i in lst:
            Doctors.append(i)
        connection.commit()
        connection.close()

        connection = sqlite3.connect("pharmacy.db")
        cursor = connection.cursor()
        
        body=ctk.CTkFrame(sub_frame,fg_color="#EAEAEA",height=525)
        body.grid(row=0,column=0,sticky="nswe",pady=10)
        body.columnconfigure(0,weight=1)
        body.columnconfigure(1,weight=1)
        
        for doctor in Doctors:

                      
            cursor.execute("select address,phone,role from doctors_details where name = ?",doctor)
            details = cursor.fetchall()

            cursor.execute("SELECT image FROM images WHERE name = ?", (doctor[0],))
            binary_data = cursor.fetchone()
            
            binary_data = binary_data[0]
            with open('retrieved_image.jpg', 'wb') as file:
                file.write(binary_data)
            img = Image.open('retrieved_image.jpg')
            img = img.resize((250, 250), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            
            doctor1=ctk.CTkFrame(body,fg_color="white",border_color="#880066",border_width=2)
            doctor1.grid(row=row,column=column,pady=30,padx=20)

            ctk.CTkLabel(doctor1,text="",image =img,font=("roboto",16,"bold"),
                             text_color="black").grid(row=0,column=0,columnspan=2,pady=15,padx=10)
            ctk.CTkLabel(doctor1,text="Name:",font=("roboto",16,"bold"),
                             text_color="black").grid(row=1,column=0,padx=20,pady=10,sticky="w")
            ctk.CTkLabel(doctor1,text=doctor[0],font=("roboto",16,"bold"),
                             text_color="black").grid(row=1,column=1,padx=20,pady=10,sticky="w")

            ctk.CTkButton(doctor1,text="Remove",font=("roboto",16,"bold"),
                          command=partial(remove,doctor[0])).grid(row=2,column=0,columnspan=2,pady=10)
            

            column+=1
            
            if column==2:
                row+=1
                column=0

        connection.close()



    show_doctors()

    
    return show_doctors







        







