import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import sqlite3
from functools import partial


def remove_pharmacy_tab(tab,notebook,path,admin_pannel,refresh):
    main_frame=ctk.CTkFrame(tab,fg_color="#EAEAEA")
    main_frame.pack(fill="both",expand=True)
    main_frame.columnconfigure(0,weight=2)
    main_frame.rowconfigure(0,weight=0)
    main_frame.rowconfigure(1,weight=2)
  

    nav=ctk.CTkFrame(main_frame,fg_color="#3B1E54",corner_radius=0)
    nav.grid(row=0,column=0,sticky="wesn")
    nav.columnconfigure(0,weight=0)
    nav.columnconfigure(1,weight=2)

    ctk.CTkLabel(nav,text="REMOVE PHARMACIES",
                 font=("impact",35),text_color="white").grid(row=0,column=1,pady=5)

    image_path1 = path('back.png')
    tab.back = ctk.CTkImage(light_image=Image.open(image_path1),size=(44,44))

    ctk.CTkButton(nav,text="",image = tab.back,hover_color="#3C1E51",fg_color="#3B1E54",width=55,
                  command = lambda:notebook.select(admin_pannel)).grid(row=0,column=0,pady=5)

    def run():
        pharmacies=[]

        connection = sqlite3.connect("pharmacy.db")
        cursor = connection.cursor()
        cursor.execute("select * from nearby_pharmacy")
        items = cursor.fetchall()
        for item in items:
            pharmacies.append(item[0])
        connection.close()
        return pharmacies

    def remove(name):
        connection = sqlite3.connect("pharmacy.db")
        cursor = connection.cursor()
        cursor.execute("delete from nearby_pharmacy where name = ?",(name,))
        cursor.execute("delete from images where name = ?",(name,))
        connection.commit()
        connection.close()
        refresh()
        show_pharmacy()
    
    def show_pharmacy():
        pharmacies = run()
        row=0
        column=0

        connection = sqlite3.connect("pharmacy.db")
        cursor = connection.cursor()
        
        i=0
        body=ctk.CTkScrollableFrame(main_frame,fg_color="#EAEAEA",height=450)
        body.grid(row=1,column=0,sticky="nswe")
        body.columnconfigure(0,weight=1)
        body.columnconfigure(1,weight=1)
        for pharmacy in pharmacies:
            pharmacy = [(pharmacy)]
            
            cursor.execute("select address, phone,address2 from nearby_pharmacy where name = ?",(pharmacy))
            items = cursor.fetchall()
            

            cursor.execute("SELECT image FROM images WHERE name = ?", (pharmacy))
            binary_data = cursor.fetchone()
            binary_data = binary_data[0]
            with open('retrieved_image.jpg', 'wb') as file:
                file.write(binary_data)
            img = Image.open('retrieved_image.jpg')
            img = img.resize((250, 250), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            
            
            pharmacy1=ctk.CTkFrame(body,fg_color="white",border_color="#880066",border_width=2,width=600)
            pharmacy1.grid(row=row,column=column,pady=20,padx=20)

            ctk.CTkLabel(pharmacy1,text = "",image = img,font=("roboto",16,"bold"),
                             text_color="black").grid(row=0,column=0,columnspan=2,pady=15)
            ctk.CTkLabel(pharmacy1,text="Name:",font=("roboto",16,"bold"),
                             text_color="black").grid(row=1,column=0,padx=20,pady=10,sticky="w")
            ctk.CTkLabel(pharmacy1,text=pharmacy[0],font=("roboto",16,"bold"),
                             text_color="black").grid(row=1,column=1,padx=20,pady=10,sticky="w")

            ctk.CTkLabel(pharmacy1,text="Address:",font=("roboto",16,"bold"),
                             text_color="black").grid(row=2,column=0,padx=20,pady=10,sticky="w")
            ctk.CTkLabel(pharmacy1,text=f"{items[0][2]},\n{items[0][0]}",font=("roboto",16,"bold"),
                             text_color="black").grid(row=2,column=1,padx=20,pady=10,sticky="w")

            ctk.CTkButton(pharmacy1,text="Remove",font=("impact",15),
                          command =partial(remove,pharmacy[0])).grid(row=3,column=0,columnspan=2,pady=10)

            column+=1
            i+=1
            if column==2:
                row+=1
                column=0

        connection.close()

    show_pharmacy()

    return show_pharmacy








