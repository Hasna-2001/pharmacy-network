import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk


def services(tab,notebook,path,upload_recipt,nearby_pharmacy,doctors,my_orders,donate,feedback,home,all_items):

    #main frame in lobby
    lobby_frame = ctk.CTkFrame(tab,fg_color = "#EEEEEE",corner_radius=0)
    lobby_frame.pack(fill="both", expand=True)

    lobby_frame.columnconfigure(0,weight=2)
    lobby_frame.rowconfigure(0,weight=0)
    lobby_frame.rowconfigure(1,weight=3)
 

    temp_frame=ctk.CTkFrame(lobby_frame,fg_color="#EEEEEE")
    temp_frame.grid(row=0,column=0,pady=30,sticky="nswe")
    body=ctk.CTkFrame(lobby_frame,fg_color="white")
    body.grid(row=1,column=0)

    image_path1 = path('back.png')
    tab.back = ctk.CTkImage(light_image=Image.open(image_path1),size=(50,50))

    image_path2 = path('file.png')
    tab.upload = ctk.CTkImage(light_image=Image.open(image_path2),size=(120,120))

    image_path3 = path('drugs.png')
    tab.all_drugs = ctk.CTkImage(light_image=Image.open(image_path3),size=(120,120))

    image_path4 = path('nearbypharmacy.png')
    tab.nearby_pharmacy = ctk.CTkImage(light_image=Image.open(image_path4),size=(120,120))

    image_path5 = path('doctors.png')
    tab.doctors = ctk.CTkImage(light_image=Image.open(image_path5),size=(120,120))

    image_path6 = path('donate.png')
    tab.donate = ctk.CTkImage(light_image=Image.open(image_path6),size=(120,120))

    image_path7 = path('feedback.png')
    tab.feedback = ctk.CTkImage(light_image=Image.open(image_path7),size=(120,120))

    
    
    ctk.CTkLabel(temp_frame,text="OUR SERVICES",font=("impact",40),text_color="#3B1E54").grid(row=0,column=1,pady=30,padx=330)

    ctk.CTkButton(temp_frame,image=tab.back,text="",command=lambda:notebook.select(home),width=55,fg_color="#EEEEEE",hover_color="#EEEEEE").grid(row=0,column=0,pady=30,sticky="w",padx=10)
    
    ctk.CTkButton(body,text="Upload Prescription",image=tab.upload,compound="top",font=("impact",20),text_color="white",fg_color="#3B1E54",
                  width=280,height=180,command=lambda:notebook.select(upload_recipt)).grid(row=0,column=0,padx=10,pady=10)

    ctk.CTkButton(body,text="Order Drugs",image=tab.all_drugs,compound="top",font=("impact",20),text_color="white",fg_color="#3B1E54",
                  width=280,height=180,command=lambda:notebook.select(all_items)).grid(row=0,column=1,padx=10,pady=10)

    ctk.CTkButton(body,text="Nearby Pharmacies",image=tab.nearby_pharmacy,compound="top",font=("impact",20),text_color="white",fg_color="#3B1E54",
                  width=280,height=180,command=lambda:notebook.select(nearby_pharmacy)).grid(row=0,column=2,padx=10,pady=10)

    ctk.CTkButton(body,text="Doctors Conseltation",image=tab.doctors,compound="top",font=("impact",20),text_color="white",fg_color="#3B1E54",
                  width=280,height=180,command=lambda:notebook.select(doctors)).grid(row=1,column=0,padx=10,pady=10)

    ctk.CTkButton(body,text="Donate Us",image=tab.donate,compound="top",font=("impact",20),text_color="white",fg_color="#3B1E54",
                  width=280,height=180,command=lambda:notebook.select(donate)).grid(row=1,column=1,padx=10,pady=10)

    ctk.CTkButton(body,text="Feedback",image=tab.feedback,compound="top",font=("impact",20),text_color="white",fg_color="#3B1E54",
                  width=280,height=180,command=lambda:notebook.select(feedback)).grid(row=1,column=2,padx=10,pady=10)
    













