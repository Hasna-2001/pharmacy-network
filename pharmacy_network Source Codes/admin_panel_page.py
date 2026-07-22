import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import sqlite3

def admin_pannel(tab,notebook,path,home,add_items,add_place,add_doctor,add_offer,login,
                 remove_doctors,remove_pharmacy):

    mainframe = ctk.CTkFrame(tab,corner_radius = 0,fg_color="#3B1E54")
    mainframe.pack(fill="both",expand = True)
    mainframe.columnconfigure(0,weight=1)
    mainframe.rowconfigure(0,weight=0)
    mainframe.rowconfigure(1,weight=1)


    image_path1 = path('box.png')
    tab.add_items = ctk.CTkImage(light_image=Image.open(image_path1),size=(100,100))

    image_path2 = path('user.png')
    tab.add_doctors = ctk.CTkImage(light_image=Image.open(image_path2),size=(100,100))

    image_path3 = path('pharmacy.png')
    tab.add_pharmacy = ctk.CTkImage(light_image=Image.open(image_path3),size=(100,100))

    image_path4 = path('discount-tag.png')
    tab.add_offers = ctk.CTkImage(light_image=Image.open(image_path4),size=(100,100))

    image_path5 = path('back.png')
    tab.back = ctk.CTkImage(light_image=Image.open(image_path5),size=(45,45))

    image_path6 = path('remove-user.png')
    tab.remove_doc = ctk.CTkImage(light_image=Image.open(image_path6),size=(100,100))

    image_path7 = path('wrong.png')
    tab.remove_pharmacy = ctk.CTkImage(light_image=Image.open(image_path7),size=(100,100))
        
    navframe = ctk.CTkFrame(mainframe,corner_radius = 0,fg_color="#3B1E54")
    navframe.grid(row=0,column=0,sticky = "nswe")
    ctk.CTkLabel(navframe,text = "ADMIN PANNEL",font=("impact",30),fg_color="#3B1E54").pack(pady=20,fill="both",expand=True)

    body = ctk.CTkScrollableFrame(mainframe,fg_color = "#F2EDF3",corner_radius = 0)
    body.grid(row=1,column=0,sticky="nswe")
    body.columnconfigure(0,weight=1)
    body.columnconfigure(1,weight=1)
    body.columnconfigure(2,weight=1)

    ctk.CTkButton(body,text="",width = 55,image = tab.back,command=lambda:notebook.select(login),hover_color="white",fg_color="#F2EDF3").grid(row=0,column=0,sticky= "w",pady=15,padx=10)

    ctk.CTkButton(body,text="ADD NEW\nITEMS",font = ("calibri",20,"bold"),width=230,
                  hover_color="white",height=150,text_color="#3B1E54",command=lambda:notebook.select(add_items),
                  corner_radius =4,fg_color = "#4AA4EC",image =tab.add_items,compound="left").grid(row = 1,column=0,pady=50)
    ctk.CTkButton(body,text="ADD NEW\nPHARMACY",font = ("calibri",20,"bold"),width=230,
                  hover_color="white",height=150,text_color="#3B1E54",command=lambda:notebook.select(add_place),
                  corner_radius =4,fg_color = "#FE9696",image =tab.add_pharmacy,compound="left").grid(row = 1,column=1)
    ctk.CTkButton(body,text="ADD NEW\nDOCTORS",font = ("calibri",20,"bold"),width=230,
                  hover_color="white",height=150,text_color="#3B1E54",command =lambda:notebook.select(add_doctor),
                  corner_radius =4,fg_color = "#4DD4C2",image =tab.add_doctors,compound="left").grid(row = 1,column=2)
    ctk.CTkButton(body,text="ADD NEW\nOFFERS",font = ("calibri",20,"bold"),width=230,
                  hover_color="white",height=150,text_color="#3B1E54",command=lambda:notebook.select(add_offer),
                  corner_radius =4,fg_color = "#FFB996",image =tab.add_offers,compound="left").grid(row = 2,column=0)

    ctk.CTkButton(body,text="REMOVE\nDOCTORS",font = ("calibri",20,"bold"),width=230,
                  hover_color="white",height=150,text_color="#3B1E54",command=lambda:notebook.select(remove_doctors),
                  corner_radius =4,fg_color = "#4DD4C2",image =tab.remove_doc,compound="left").grid(row = 2,column=1)

    ctk.CTkButton(body,text="REMOVE\nPHARMACY",font = ("calibri",20,"bold"),width=230,
                  hover_color="white",height=150,text_color="#3B1E54",command=lambda:notebook.select(remove_pharmacy),
                  corner_radius =4,fg_color = "#4AA4EC",image =tab.remove_pharmacy,compound="left").grid(row = 2,column=2)

    users_frame = ctk.CTkFrame(body,fg_color="#F2EDF3")
    users_frame.grid(row=3,column=0,columnspan = 3,pady=50)

    ctk.CTkLabel(users_frame,text="Current Users",corner_radius = 10,fg_color="#F2EDF3",text_color="black",font=("impact",20)).pack(pady=10)

    users_frame2 = ctk.CTkFrame(users_frame,fg_color="#2A3650",corner_radius=25)
    users_frame2.pack()
  
    show_frame = ctk.CTkFrame(users_frame2,fg_color="#2A3650",corner_radius=5)
    show_frame.pack(pady=10,padx=10)

    ctk.CTkLabel(show_frame,text="Users",corner_radius = 10,fg_color="#2A3650",text_color="white",font=("roboto",17,"bold")).grid(row=0,column=0,pady=5)
    ctk.CTkLabel(show_frame,text="Doctors",corner_radius = 10,fg_color="#2A3650",text_color="white",font=("roboto",17,"bold")).grid(row=0,column=1,pady=5)
    ctk.CTkLabel(show_frame,text="Pharmacient",corner_radius = 10,fg_color="#2A3650",text_color="white",font=("roboto",17,"bold")).grid(row=0,column=2,pady=5)


    def run():
        user_names = []
        pharmacient_names = []
        doctor_names = []
       
        connection = sqlite3.connect("pharmacy.db")
        cursor = connection.cursor()

        cursor.execute("select name from users_details")
        details = cursor.fetchall()
        for i in details:
            user_names.append(i)

        cursor.execute("select name from pharmacient_names")
        details = cursor.fetchall()
        for i in details:
            pharmacient_names.append(i)

        cursor.execute("select name from doctor_names")
        details = cursor.fetchall()
        for i in details:
            doctor_names.append(i)
        
        connection.close()
        
        row=1
        for name in user_names:
            ctk.CTkLabel(show_frame,text=name[0].capitalize(),corner_radius = 10,fg_color="white",width=250,
                             text_color="black",font=("roboto",15)).grid(row=row,column=0,pady=10,padx=5)
            row+=1

        row=1
        for name in pharmacient_names:
            ctk.CTkLabel(show_frame,text=name[0].capitalize(),corner_radius = 10,fg_color="white",width=250,
                             text_color="black",font=("roboto",15)).grid(row=row,column=2,pady=10,padx=5)
            row+=1

        row=1
        for name in doctor_names:
            ctk.CTkLabel(show_frame,text=name[0].capitalize(),corner_radius = 10,fg_color="white",width=250,
                             text_color="black",font=("roboto",15)).grid(row=row,column=1,pady=10,padx=5)
            row+=1
        
        

    run()
        
    
    sales_frame = ctk.CTkFrame(body,fg_color="#F2EDF3",corner_radius=25)
    sales_frame.grid(row=4,column=0,columnspan = 3,pady=45,padx=50)
    ctk.CTkLabel(sales_frame,text="Sales History",corner_radius = 10,fg_color="#F2EDF3",text_color="black",font=("impact",20)).pack()

    sales_frame2 = ctk.CTkFrame(sales_frame,fg_color="#2A3650",corner_radius=25)
    sales_frame2.pack(pady=10)
    
    sales_show_frame = ctk.CTkFrame(sales_frame2,fg_color="#2A3650",corner_radius=25)
    sales_show_frame.pack(pady=10,padx=10)
    
    ctk.CTkLabel(sales_show_frame,text="Date",corner_radius = 10,fg_color="#2A3650",text_color="white",font=("roboto",17,"bold")).grid(row=0,column=0,pady=5)
    ctk.CTkLabel(sales_show_frame,text="Sales",corner_radius = 10,fg_color="#2A3650",text_color="white",font=("roboto",17,"bold")).grid(row=0,column=1,pady=5)

    def run_sales_table():
        
        row=1
        column=0
        sales=[]
        connection = sqlite3.connect("pharmacy.db")
        cursor = connection.cursor()
        cursor.execute("select * from sales_record")
        details = cursor.fetchall()
        connection.close()
        
        for i in details:
            sales.append(i)
         
        for sale in sales:
            ctk.CTkLabel(sales_show_frame,text=sale[0],corner_radius = 10,fg_color="white",width=200,
                         text_color="black",font=("roboto",15)).grid(row=row,column=column,padx=5,pady=10)

            ctk.CTkLabel(sales_show_frame,text=f"Rs.{sale[1]}.00",corner_radius = 10,fg_color="white",width=200,
                         text_color="black",font=("roboto",15)).grid(row=row,column=column+1,padx=5,pady=10)
            

            row+=1

    run_sales_table()
    
    def graphs():
        
        daily_sales_graph_frame = ctk.CTkFrame(body,fg_color = "white")
        daily_sales_graph_frame.grid(row=5,column=0,columnspan = 2)

        ctk.CTkLabel(daily_sales_graph_frame,text  = "Daily Sales",text_color = "black",font=("roboto",20,"bold")).grid(column=0,row=0)
        graph_frame = ctk.CTkFrame(daily_sales_graph_frame,fg_color = "blue",width=400,height=300)
        graph_frame.grid(row=1,column=0)

        monthy_sales_graph_frame = ctk.CTkFrame(body,fg_color = "white")
        monthy_sales_graph_frame.grid(row=5,column=2,columnspan = 2)


        ctk.CTkLabel(monthy_sales_graph_frame,text  = "Monthly Sales",text_color = "black",font=("roboto",20,"bold")).grid(column=0,row=0)
        graph_frame = ctk.CTkFrame(monthy_sales_graph_frame,fg_color = "blue",width=400,height=300)
        graph_frame.grid(row=1,column=0)


    return run, run_sales_table








