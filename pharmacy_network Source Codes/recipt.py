import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename




def upload_recipt(tab,home,notebook,path,services):

    mainframe=ctk.CTkScrollableFrame(tab,fg_color="#EAEAEA")
    mainframe.pack(expand=True,fill="both")

    mainframe.columnconfigure(0,weight=2)

    sub_frame = ctk.CTkFrame(mainframe,fg_color="#3B1E54")
    sub_frame.grid(row=1,column=0,pady=40)

    image_path1 = path('number-1.png')
    tab.number1 = ctk.CTkImage(light_image=Image.open(image_path1),size=(35,35))

    image_path2 = path('number-2.png')
    tab.number2 = ctk.CTkImage(light_image=Image.open(image_path2),size=(35,35))

    image_path3 = path('number-3.png')
    tab.number3 = ctk.CTkImage(light_image=Image.open(image_path3),size=(35,35))

    sub_frame.columnconfigure(0,weight=2)

    ctk.CTkLabel(sub_frame,text="Simply upload your prescription to get your medication\nDeliverd your Doorstep",
                 font=("calibri",20,"bold"),text_color="white").grid(column=0,row=0,sticky="w",padx=10,pady=10)
    ctk.CTkLabel(sub_frame,image=tab.number1,compound="left",text="  Enter Patient Details",font=("calibri",19,"bold"),text_color="white").grid(column=0,row=1,pady=10,sticky="w",padx=10)
    ctk.CTkLabel(sub_frame,image=tab.number2,compound="left",text="  Enter Patient Address",font=("calibri",19,"bold"),text_color="white").grid(column=0,row=2,pady=10,sticky="w",padx=10)
    ctk.CTkLabel(sub_frame,image=tab.number3,compound="left",text="  Get an Image of a Prescription and upload",font=("calibri",19,"bold"),text_color="white").grid(column=0,row=3,pady=10,sticky="w",padx=10)


    
    message_frame=ctk.CTkFrame(sub_frame,fg_color="white")
    message_frame.grid(column=0,row=4,pady=15,padx=10)

    

    temp_frame=ctk.CTkFrame(mainframe,fg_color="white",corner_radius=0,border_color="black",border_width=2)
    temp_frame.grid(column=0,row=0,sticky="we")
    temp_frame.columnconfigure(0,weight=0)
    temp_frame.columnconfigure(1,weight=2)
    
    ctk.CTkLabel(temp_frame,text="Upload Your Prescription",font=("impact",30),
                 text_color="black",fg_color="white").grid(row=0,column=1)
    
    image_path1 = path('back.png')
    tab.back = ctk.CTkImage(light_image=Image.open(image_path1),size=(44,44))

    ctk.CTkButton(temp_frame,text="",image = tab.back,hover_color="white",fg_color="white",width=55,
                  command = lambda:notebook.select(services)).grid(row=0,column=0,pady=5,padx=10)
    

    ctk.CTkLabel(message_frame,text="Name",font=("calibri",15,"bold"),
                 text_color="black").grid(column=0,row=0,pady=10,sticky="w",padx=20)

    
    ctk.CTkEntry(message_frame,placeholder_text="First Name",height=35,width=200,corner_radius=5,text_color="black",fg_color="white",
                 border_color="#DB0A41").grid(row=1,column=0,padx=20)

   
    ctk.CTkEntry(message_frame,placeholder_text="Last Name",height=35,width=200,corner_radius=5,text_color="black",fg_color="white",
                 border_color="#DB0A41").grid(row=1,column=1,padx=20)


    ctk.CTkLabel(message_frame,text="Address",font=("calibri",15,"bold"),
                 text_color="black").grid(row=5,column=0,pady=10,sticky="w",padx=20)

    address_var=tk.StringVar()
    ctk.CTkEntry(message_frame,height=35,width=250,textvariable=address_var,
                                             corner_radius=5,text_color="black",fg_color="white",
                                             border_color="#DB0A41").grid(row=6,column=0,padx=20,columnspan=2,sticky="w")

    ctk.CTkLabel(message_frame,text="Age",font=("calibri",15,"bold"),
                 text_color="black").grid(row=7,column=0,pady=10,sticky="w",padx=20)

    age_var=tk.StringVar()
    ctk.CTkEntry(message_frame,height=35,width=250,textvariable=age_var,
                                             corner_radius=5,text_color="black",fg_color="white",
                                             border_color="#DB0A41").grid(row=8,column=0,padx=20,columnspan=2,sticky="w")

    ctk.CTkLabel(message_frame,text="Invoice Date",font=("calibri",15,"bold"),
                 text_color="black").grid(row=9,column=0,pady=10,sticky="w",padx=20)

    date_var=tk.StringVar()
    ctk.CTkEntry(message_frame,height=35,width=250,textvariable=date_var,
                                             corner_radius=5,text_color="black",fg_color="white",
                                             border_color="#DB0A41").grid(row=10,column=0,padx=20,columnspan=2,sticky="w")

    ctk.CTkLabel(message_frame,text="Any Other Comments",font=("calibri",15,"bold"),
                 text_color="black").grid(row=11,column=0,pady=10,sticky="w",padx=20)

    ctk.CTkTextbox(message_frame,height=90,width=440,corner_radius=5,text_color="black",fg_color="white",
                   border_color="#DB0A41",border_width=2).grid(row=12,column=0,columnspan=2)
    filename=None
    def upload():
        ftypes=[("Jpg files","*.jpg"),("PNG files","*.png")]
        filename=tk.filedialog.askopenfilename(filetypes=ftypes)

    
    ctk.CTkLabel(message_frame,text="Please Attach Your Invoice",font=("calibri",15,"bold"),
                 text_color="black").grid(row=13,column=0,pady=10,sticky="w",padx=20)

    ctk.CTkButton(message_frame,height=60,width=440,corner_radius=5,text_color="black",command=upload,
                  fg_color="white",border_width=2,text="Brows Files",font=("calibri",15,"bold"),
                  border_color="#DB0A41").grid(row=14,column=0,columnspan=2)

    ctk.CTkButton(message_frame,text="Submit",width=150,height=35,font=("verdana",15,"bold"),text_color="black",
                      fg_color="light green",corner_radius=5).grid(row=15,column=0,pady=20)

    ctk.CTkButton(message_frame,text="Cancel",width=150,height=35,font=("verdana",15,"bold"),text_color="black",
                      fg_color="light green",command=lambda:notebook.select(home),corner_radius=5).grid(row=15,column=1,pady=30)





