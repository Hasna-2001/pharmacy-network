import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import sqlite3
import warnings


def Doctors(tab,notebook,path,lobby,cart,epharmacies,cart_func,orders,offers,services):
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

    ctk.CTkLabel(nav,text="Doctors Consultation",
                 font=("impact",35),text_color="white").grid(row=0,column=1,pady=5)

    image_path1 = path('back.png')
    tab.back = ctk.CTkImage(light_image=Image.open(image_path1),size=(44,44))

    ctk.CTkButton(nav,text="",image = tab.back,hover_color="#3C1E51",fg_color="#3B1E54",width=55,
                  command = lambda:notebook.select(services)).grid(row=0,column=0,pady=5)

    sub_frame  = ctk.CTkScrollableFrame(main_frame,fg_color="#EAEAEA",height=525)
    sub_frame.grid(row=3,column=0,sticky="nswe",pady=10)
    sub_frame.columnconfigure(0,weight =2)
    
    

    

         

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

            ctk.CTkLabel(doctor1,text="Working Hospitel:",font=("roboto",16,"bold"),
                             text_color="black").grid(row=2,column=0,padx=20,pady=10,sticky="w")
            ctk.CTkLabel(doctor1,text=details[0][0],font=("roboto",16,"bold"),
                             text_color="black").grid(row=2,column=1,padx=20,pady=10,sticky="w")

            ctk.CTkLabel(doctor1,text="Contact No:",font=("roboto",16,"bold"),
                             text_color="black").grid(row=3,column=0,padx=20,pady=10,sticky="w")
            ctk.CTkLabel(doctor1,text=details[0][1],font=("roboto",16,"bold"),
                             text_color="black").grid(row=3,column=1,padx=20,pady=10,sticky="w")

            ctk.CTkLabel(doctor1,text="Position:",font=("roboto",16,"bold"),
                             text_color="black").grid(row=4,column=0,padx=20,pady=10,sticky="w")
            ctk.CTkLabel(doctor1,text=details[0][2],font=("roboto",16,"bold"),
                             text_color="black").grid(row=4,column=1,padx=20,pady=10,sticky="w")

            column+=1
            
            if column==2:
                row+=1
                column=0

        connection.close()



    show_doctors()

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
    
    return show_doctors







        







