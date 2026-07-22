import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import sqlite3


def nearby_stores(tab,notebook,path,lobby,cart,epharmacies,cart_func,orders,offers,services):
    main_frame=ctk.CTkFrame(tab,fg_color="#EAEAEA")
    main_frame.pack(fill="both",expand=True)
    main_frame.columnconfigure(0,weight=2)
    main_frame.rowconfigure(0,weight=0)
    main_frame.rowconfigure(1,weight=0)
    main_frame.rowconfigure(2,weight=2)
    main_frame.rowconfigure(3,weight=1)

    nav=ctk.CTkFrame(main_frame,fg_color="#3B1E54",corner_radius=0)
    nav.grid(row=0,column=0,sticky="wesn")
    nav.columnconfigure(0,weight=0)
    nav.columnconfigure(1,weight=2)

    ctk.CTkLabel(nav,text="Nearby Pharmacies",
                 font=("impact",35),text_color="white").grid(row=0,column=1,pady=5)

    image_path1 = path('back.png')
    tab.back = ctk.CTkImage(light_image=Image.open(image_path1),size=(44,44))

    ctk.CTkButton(nav,text="",image = tab.back,hover_color="#3C1E51",fg_color="#3B1E54",width=55,
                  command = lambda:notebook.select(services)).grid(row=0,column=0,pady=5)

    select_frame=ctk.CTkFrame(main_frame,fg_color="#EAEAEA")
    select_frame.grid(row=2,column=0,sticky="w",padx=20)

    def show_selected(events):
        pharmacies = run()
        new_list=[]
        connection = sqlite3.connect("pharmacy.db")
        cursor = connection.cursor()
        for pharmacy in pharmacies:
            pharmacy = [(pharmacy)]
            cursor.execute("select district from nearby_pharmacy where name=?",(pharmacy))
            district = cursor.fetchone()
            
            
            
            
            if district[0]==option_value.get():
                new_list.append(pharmacy[0])
                
        if option_value.get() == "ALL":
            show_pharmacy()

        else:
            
            row=0
            column=0

            i=0
            body=ctk.CTkScrollableFrame(main_frame,fg_color="#EAEAEA",height=450)
            body.grid(row=3,column=0,sticky="nswe")
            body.columnconfigure(0,weight=1)
            body.columnconfigure(1,weight=1)
            for pharmacy in new_list:

                pharmacy = [(pharmacy)]
                cursor.execute("select address, phone, address2 from nearby_pharmacy where name = ?",(pharmacy))
                items = cursor.fetchall()

                cursor.execute("SELECT image FROM images WHERE name = ?", (pharmacy))
                binary_data = cursor.fetchone()
                
                binary_data = binary_data[0]
                with open('retrieved_image.jpg', 'wb') as file:
                    file.write(binary_data)
                img = Image.open('retrieved_image.jpg')
                img = img.resize((250, 250), Image.LANCZOS)
                img = ImageTk.PhotoImage(img)                
                pharmacy1=ctk.CTkFrame(body,fg_color="white",border_color="#880066",border_width=2)
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

                ctk.CTkLabel(pharmacy1,text="Contact No:",font=("roboto",16,"bold"),
                                 text_color="black").grid(row=3,column=0,padx=20,pady=10,sticky="w")
                ctk.CTkLabel(pharmacy1,text=items[0][1],font=("roboto",16,"bold"),
                                 text_color="black").grid(row=3,column=1,padx=20,pady=10,sticky="w")
                column+=1
                i+=1
                if column==2:
                    row+=1
                    column=0
            connection.close()
                

    districs=["ALL","Ampara", "Anuradhapura", "Badulla", "Batticaloa", "Colombo", "Galle", "Gampaha", "Hambantota", "Jaffna", "Kalutara", "Kandy", "Kegalle",
                                "Kilinochchi", "Kurunegala", "Mannar",
                                "Matale", "Matara", "Monaragala", "Mullaitivu", "Nuwara Eliya", "Polonnaruwa", "Puttalam", "Ratnapura", "Trincomalee", "Vavuniya" ]
    ctk.CTkLabel(select_frame,text="Select Your District:",font=("calibri",18),
                         text_color="black").pack(side="left")
    option_value=tk.StringVar(value=districs[0])
    options=ctk.CTkComboBox(select_frame,variable=option_value,command=show_selected,height=35,border_color="#DB0A41",button_color="#DB0A41",
                                 dropdown_fg_color="#880066",fg_color="white",corner_radius=50,width=200,
                                 text_color="black")
    options.pack(side="left",padx=10)
    options.configure(values=districs)

    

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
        
    
    def show_pharmacy():
        pharmacies = run()
        row=0
        column=0

        connection = sqlite3.connect("pharmacy.db")
        cursor = connection.cursor()
        
        i=0
        body=ctk.CTkScrollableFrame(main_frame,fg_color="#EAEAEA",height=450)
        body.grid(row=3,column=0,sticky="nswe")
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

            ctk.CTkLabel(pharmacy1,text="Contact No:",font=("roboto",16,"bold"),
                             text_color="black").grid(row=3,column=0,padx=20,pady=10,sticky="w")
            ctk.CTkLabel(pharmacy1,text=items[0][1],font=("roboto",16,"bold"),
                             text_color="black").grid(row=3,column=1,padx=20,pady=10,sticky="w")
            column+=1
            i+=1
            if column==2:
                row+=1
                column=0

        connection.close()

    show_pharmacy()

    footer_frame = ctk.CTkFrame(main_frame,fg_color = "#3B1E54",corner_radius=0)
    footer_frame.grid(row=4,column=0,sticky="nswe")

    temp_footer= ctk.CTkFrame(footer_frame,fg_color = "#3B1E54")
    temp_footer.pack(pady=5)

    #homelogo image
    image_path3 = path('home.png')
    tab.home_logo = ctk.CTkImage(light_image=Image.open(image_path3),size=(28,28))

    #mycart logo image
    image_path4 = path('bucket.png')
    tab.mycart_logo = ctk.CTkImage(light_image=Image.open(image_path4),size=(28,28))

    #orders logo image
    image_path5 = path('orders.png')
    tab.myorders_logo = ctk.CTkImage(light_image=Image.open(image_path5),size=(28,28))

    #offers logo image
    image_path6 = path('offer.png')
    tab.offers_logo = ctk.CTkImage(light_image=Image.open(image_path6),size=(28,28))

    #payement logo image
    image_path7 = path('payment.png')
    tab.payement_logo = ctk.CTkImage(light_image=Image.open(image_path7),size=(28,28))

    #store logo image
    image_path8 = path('shop.png')
    tab.shop_logo = ctk.CTkImage(light_image=Image.open(image_path8),size=(28,28))

    def select_cart():
        notebook.select(cart)
        cart_func()
        
        
    #Home icon button frame
    ctk.CTkButton(temp_footer,text="",image=tab.home_logo,width=0,fg_color = "#3B1E54",
                  command=lambda: notebook.select(lobby)).grid(row=0,column=0,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.mycart_logo,fg_color = "#3B1E54",
                  command=select_cart).grid(row=0,column=1,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.shop_logo,fg_color = "#3B1E54",
                  command=lambda: notebook.select(epharmacies)).grid(row=0,column=2,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.myorders_logo,fg_color = "#3B1E54",
                  command=lambda: notebook.select(orders)).grid(row=0,column=3,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.offers_logo,fg_color = "#3B1E54",
                  command=lambda: notebook.select(offers)).grid(row=0,column=4,padx=30)
   

    return show_pharmacy








