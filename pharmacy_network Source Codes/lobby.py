import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import sqlite3




offer1_x = 1
offer1_x1 = 0.041
time_lap=10

def lobby(tab,notebook,epharmacy,path,cart,my_orders,services,offers,bucket,fitness,medicap,pharmeasy,skincare,cart_func,login):

    #main frame in lobby
    lobby_frame = ctk.CTkFrame(tab,fg_color = "white")
    lobby_frame.pack(fill="both", expand=True)

    lobby_frame.columnconfigure(0,weight=2)
    lobby_frame.rowconfigure(0,weight=0)
    lobby_frame.rowconfigure(1,weight=3)
    lobby_frame.rowconfigure(2,weight=0)
    #nave bar frame
    navbar = ctk.CTkFrame(lobby_frame,fg_color = "#3B1E54",corner_radius=0)
    navbar.grid(row=0,column=0,sticky="nswe")
    
    navbar.columnconfigure(0,weight=0)
    navbar.columnconfigure(1,weight=2)

    image_path111 = path('usericon.png')
    tab.user_icon = ctk.CTkImage(light_image=Image.open(image_path111),size=(55,55))
    
    ctk.CTkLabel(navbar,text="Pharmacy Network",font=("impact",30)).grid(row=0,column=0,padx=10)
    ctk.CTkButton(navbar,text="",image=tab.user_icon,fg_color="#3B1E54",
                  hover_color="#3B1E54",command=lambda:notebook.select(login)).grid(row=0,column=1,sticky="e",padx=10,pady=3)
 
    #body frame 
    body_frame = ctk.CTkScrollableFrame(lobby_frame,fg_color = "#EEEEEE")
    body_frame.grid(row=1,column=0,sticky="nswe")

    body_frame.columnconfigure(0,weight=2)
    body_frame.columnconfigure(1,weight=2)
    

    #offer frame
    offers_frame= ctk.CTkFrame(body_frame,fg_color="white",width=470,height=310)                               
    offers_frame.grid(row=1,column=0,pady=40,columnspan=2)

    #offer farme label
    ctk.CTkLabel(offers_frame,text = "Flash Offers",fg_color="white",font=("impact",20),
                 text_color="#3B1E54").place(relx=0.06,rely=0.03)

    #offers_frame.columnconfigure(0,weight=2)

    image_path1 = path('drugstore.png')
    tab.epharmcies = ctk.CTkImage(light_image=Image.open(image_path1),size=(140,140))    

    image_path2 = path('medical.png')
    tab.services = ctk.CTkImage(light_image=Image.open(image_path2),size=(140,140))
    
    image_path3 = path('offer1.png')
    tab.offer1 = ctk.CTkImage(light_image=Image.open(image_path3),size=(420,240))

    image_path4 = path('offer2.jpg')
    tab.offer2 = ctk.CTkImage(light_image=Image.open(image_path4),size=(420,240))

    image_path5 = path('offer3.jpg')
    tab.offer3 = ctk.CTkImage(light_image=Image.open(image_path5),size=(420,240))

    def move_offer_1():
        global offer1_x
        offer1_x-=0.005
        offer1.place(relx=offer1_x,rely=0.15)
        if offer1_x>0.041:
           offers_frame.after(2,move_offer_1)
           
        else:
            time_pass()
            offer1_x=1

    def time_pass():
        global time_lap
        time_lap-=0.5
        if time_lap>0:
            offers_frame.after(200,time_pass)

        else:
            move_2()
            time_lap=10
    
    def move_2():
        global offer1_x1
        offer1_x1-=0.005
        offer1.place(relx=offer1_x1,rely=0.15)
        if offer1_x1>-1:
             offers_frame.after(2,move_2)

        else:
            move_offer_2()
            offer1_x1 = 0.041

#############################################################

    def move_offer_2():
        global offer1_x
        offer1_x-=0.005
        offer2.place(relx=offer1_x,rely=0.15)
        if offer1_x>0.041:
           offers_frame.after(2,move_offer_2)
           
        else:
            time_pass2()
            offer1_x=1

    def time_pass2():
        global time_lap
        time_lap-=0.5
        if time_lap>0:
            offers_frame.after(200,time_pass2)

        else:
            move_21()
            time_lap=10
    
    def move_21():
        global offer1_x1
        offer1_x1-=0.005
        offer2.place(relx=offer1_x1,rely=0.15)
        if offer1_x1>-1:
             offers_frame.after(2,move_21)

        else:
            move_offer_3()
            offer1_x1 = 0.041

#############################################################

    def move_offer_3():
        global offer1_x
        offer1_x-=0.005
        offer3.place(relx=offer1_x,rely=0.15)
        if offer1_x>0.041:
           offers_frame.after(2,move_offer_3)
           
        else:
            time_pass3()
            offer1_x=1

    def time_pass3():
        global time_lap
        time_lap-=0.5
        if time_lap>0:
            offers_frame.after(200,time_pass3)

        else:
            move_211()
            time_lap=10
    
    def move_211():
        global offer1_x1
        offer1_x1-=0.005
        offer3.place(relx=offer1_x1,rely=0.15)
        if offer1_x1>-1:
             offers_frame.after(2,move_211)

        else:
            move_offer_1()
            offer1_x1 = 0.041



    
    #offers
    offer1 =ctk.CTkButton(offers_frame,text="",image=tab.offer1,width=300,height=170,hover_color="white",
                          fg_color="white",command = lambda:notebook.select(offers))
    offer1.place(relx=offer1_x,rely=0)

    offer2 =ctk.CTkButton(offers_frame,text="",image=tab.offer2,width=300,height=170,hover_color="white",
                          fg_color="white",command = lambda:notebook.select(offers))
    offer2.place(relx=offer1_x,rely=0)

    offer3 =ctk.CTkButton(offers_frame,text="",image=tab.offer3,width=300,height=170,hover_color="white",
                          fg_color="white",command = lambda:notebook.select(offers))
    offer3.place(relx=offer1_x,rely=0)

    #services
    services_Frame = ctk.CTkFrame(body_frame,fg_color="#EEEEEE")
    services_Frame.grid(row=2,column=0,pady=50,padx=15,columnspan=2)

    epharmacies=ctk.CTkButton(services_Frame,text="E-Pharmacies",image=tab.epharmcies,compound="top",font=("impact",20),
                              text_color="#3B1E54",fg_color="white",
                              command= lambda:notebook.select(epharmacy),width=300,height=200,hover_color="aqua")
    epharmacies.grid(row=1,column=0,padx=10,pady=10)

    recipt=ctk.CTkButton(services_Frame,image=tab.services,compound="top",text="Our Services",hover_color="aqua",width=300,font=("impact",20),text_color="#3B1E54",fg_color="white",
                         height=200,command=lambda:notebook.select(services))
    recipt.grid(row=1,column=1,padx=10,pady=10)

    ##Top selling Products##

    state = "logged_in"

            
    connection = sqlite3.connect("pharmacy.db")
    cursor = connection.cursor()
    
    container = ctk.CTkFrame(body_frame,fg_color="#EEEEEE")
    container.grid(row=3,column=0,padx=53,pady=70,sticky="we")
    container.columnconfigure(0,weight=1)
    container.columnconfigure(1,weight=1)
    
    ctk.CTkLabel(container,text = "Top Selling Products",
                 font=("impact",25),text_color="black").grid(row=0,column=0,sticky="w",pady=10)
    
    top_selling_frame = ctk.CTkFrame(container,fg_color="aqua")
    top_selling_frame.grid(row=1,column=0,pady=35,sticky="w")
    
    name1 = "BPI Whey HD"

    cursor.execute("select image from images where name = ?",(name1,))
    binary_data = cursor.fetchone()
            
    binary_data = binary_data[0]
    with open('retrieved_image.jpg', 'wb') as file:
        file.write(binary_data)
    img = Image.open('retrieved_image.jpg')
    img = img.resize((200, 200), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
   
    ctk.CTkLabel(top_selling_frame,text=name1,font=("impact",20),
                 text_color="black").grid(row=0,column=0,padx=20,pady=10)
    ctk.CTkLabel(top_selling_frame,text="Crunchiest Chocolate\nIn The World",font=("calibri",15),text_color="black").grid(row=1,column=0,pady=10)
    ctk.CTkLabel(top_selling_frame,text="Starting At Rs.600",font=("calibri",18,"bold"),text_color="black").grid(row=2,column=0)

    label_top = ctk.CTkLabel(top_selling_frame,text="",image = img)
    label_top.grid(row=0,column=1,rowspan = 4)
    ctk.CTkButton(top_selling_frame,text="SHOP NOW",corner_radius = 5,font=("calibri",16,"bold"),height=35,
                  fg_color="black",command =lambda:notebook.select(fitness)).grid(row=3,column=0,sticky="es",padx=20,pady=10)

    
    
    top_selling_frame2 = ctk.CTkFrame(container,fg_color="aqua")
    top_selling_frame2.grid(row=1,column=1,pady=25,padx=30)

    name2 = [("HELIOCARE 60'S")]

    cursor.execute("select image from images where name = ?",name2)
    binary_data = cursor.fetchone()
            
    binary_data = binary_data[0]
    with open('retrieved_image.jpg', 'wb') as file:
        file.write(binary_data)
    img = Image.open('retrieved_image.jpg')
    img = img.resize((200, 200), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    
    ctk.CTkLabel(top_selling_frame2,text=name2[0],font=("impact",20),
                 text_color="black").grid(row=0,column=0,padx=20,pady=10)
    ctk.CTkLabel(top_selling_frame2,text="Crunchiest Chocolate\nIn The World",font=("calibri",15),text_color="black").grid(row=1,column=0,pady=10)
    ctk.CTkLabel(top_selling_frame2,text="Starting At Rs.600",font=("calibri",18,"bold"),text_color="black").grid(row=2,column=0)

    label_top1 = ctk.CTkLabel(top_selling_frame2,text="",image = img)
    label_top1.grid(row=0,column=1,rowspan = 4)
    ctk.CTkButton(top_selling_frame2,text="SHOP NOW",corner_radius = 5,font=("calibri",16,"bold"),height=35,
                  fg_color="black",command =lambda:notebook.select(medicap)).grid(row=3,column=0,sticky="es",padx=20,pady=10)
    

    top_selling_frame3 = ctk.CTkFrame(container,fg_color="aqua")
    top_selling_frame3.grid(row=2,column=0,pady=25,sticky="w")

    name3 = [("Now Vitamin D-3")]

    cursor.execute("select image from images where name = ?",name3)
    binary_data = cursor.fetchone()
            
    binary_data = binary_data[0]
    with open('retrieved_image.jpg', 'wb') as file:
        file.write(binary_data)
    img = Image.open('retrieved_image.jpg')
    img = img.resize((200, 200), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
 
    ctk.CTkLabel(top_selling_frame3,text=name3[0],font=("impact",20),
                 text_color="black").grid(row=0,column=0,padx=20,pady=10)
    ctk.CTkLabel(top_selling_frame3,text="Crunchiest Chocolate\nIn The World",font=("calibri",15),text_color="black").grid(row=1,column=0,pady=10)
    ctk.CTkLabel(top_selling_frame3,text="Starting At Rs.600",font=("calibri",18,"bold"),text_color="black").grid(row=2,column=0)

    label_top2 = ctk.CTkLabel(top_selling_frame3,text="",image = img)
    label_top2.grid(row=0,column=1,rowspan = 4)
    ctk.CTkButton(top_selling_frame3,text="SHOP NOW",corner_radius = 5,font=("calibri",16,"bold"),height=35,
                  fg_color="black",command =lambda:notebook.select(pharmeasy)).grid(row=3,column=0,sticky="es",padx=20,pady=10)
    
    top_selling_frame4 = ctk.CTkFrame(container,fg_color="aqua")
    top_selling_frame4.grid(row=2,column=1,pady=25,padx=30)

    name4 = [("Now Vitamin D-3")]

    cursor.execute("select image from images where name = ?",name4)
    binary_data = cursor.fetchone()
            
    binary_data = binary_data[0]
    with open('retrieved_image.jpg', 'wb') as file:
        file.write(binary_data)
    img = Image.open('retrieved_image.jpg')
    img = img.resize((200, 200), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    
    ctk.CTkLabel(top_selling_frame4,text=name4[0],font=("impact",20),
                 text_color="black").grid(row=0,column=0,padx=20,pady=10)
    ctk.CTkLabel(top_selling_frame4,text="Crunchiest Chocolate\nIn The World",font=("calibri",15),text_color="black").grid(row=1,column=0,pady=10)
    ctk.CTkLabel(top_selling_frame4,text="Starting At Rs.600",font=("calibri",18,"bold"),text_color="black").grid(row=2,column=0)

    label_top3 = ctk.CTkLabel(top_selling_frame4,text="",image = img)
    label_top3.grid(row=0,column=1,rowspan = 4)
    ctk.CTkButton(top_selling_frame4,text="SHOP NOW",corner_radius = 5,font=("calibri",16,"bold"),height=35,
                  fg_color="black",command =lambda:notebook.select(pharmeasy)).grid(row=3,column=0,sticky="es",padx=20,pady=10)
    
    connection.close()

    details_frame = ctk.CTkFrame(body_frame,fg_color="black",corner_radius=0)
    details_frame.grid(row=5,column=0,columnspan=2,sticky="we")
    details_frame.columnconfigure(0,weight=1)
    details_frame.columnconfigure(1,weight=1)
    details_frame.columnconfigure(2,weight=1)

    ctk.CTkLabel(details_frame,text="Pharmacy Network",fg_color="black",font=("roboto",20,"bold")).grid(row=0,column=0,columnspan=3,pady=15)

    ctk.CTkLabel(details_frame,text="",fg_color="white",font=("roboto",0.5,),height=0.5).grid(row=2,column=0,columnspan=3,sticky="we",padx=30,pady=10)

    image_path13 = path('whatsapp.png')
    tab.whatsapp = ctk.CTkImage(light_image=Image.open(image_path13),size=(28,28))

    image_path14 = path('circle-phone-flip.png')
    tab.call = ctk.CTkImage(light_image=Image.open(image_path14),size=(28,28))

    image_path15 = path('envelope.png')
    tab.mail = ctk.CTkImage(light_image=Image.open(image_path15),size=(28,28))

    contact_frame = ctk.CTkFrame(details_frame,fg_color="black")
    contact_frame.grid(row=4,column=0)
    ctk.CTkLabel(details_frame,text="Contact Us",fg_color="black",font=("roboto",17,"bold")).grid(row=3,column=0,pady=10)
    ctk.CTkLabel(contact_frame,text="   071723454",fg_color="black",compound="left",image=tab.call,font=("roboto",15)).grid(row=0,column=0,sticky="w",pady=5)
    ctk.CTkLabel(contact_frame,text="   071723454",fg_color="black",compound="left",image=tab.whatsapp,font=("roboto",15)).grid(row=1,column=0,sticky="w",pady=5)
    ctk.CTkLabel(contact_frame,text="   pharmacy@gmail.com",compound="left",image=tab.mail,fg_color="black",font=("roboto",15)).grid(row=2,column=0,sticky="w",pady=5)

    ctk.CTkButton(details_frame,text="Privacy Policy",hover_color="black",fg_color="black",font=("roboto",16,"bold")).grid(row=3,column=1,pady=10)
    ctk.CTkLabel(details_frame,text="Copyright © 2024 Pharmacy Network\nAn Desktop Application Developed By Classy Coders",
                 font=("roboto",15)).grid(row=4,column=1)
    
    image_path10 = path('facebook.png')
    tab.fb = ctk.CTkImage(light_image=Image.open(image_path10),size=(28,28))

    image_path11 = path('instagram.png')
    tab.insta = ctk.CTkImage(light_image=Image.open(image_path11),size=(28,28))

    image_path12 = path('twitter-alt-circle.png')
    tab.x = ctk.CTkImage(light_image=Image.open(image_path12),size=(28,28))

    image_path16 = path('telegram.png')
    tab.telegram = ctk.CTkImage(light_image=Image.open(image_path16),size=(28,28))
    
    follow_frame = ctk.CTkFrame(details_frame,fg_color="black")
    follow_frame.grid(row=4,column=2,pady=10)
    ctk.CTkLabel(details_frame,text="Follow Us",fg_color="black",font=("roboto",17,"bold")).grid(row=3,column=2,pady=10,columnspan=3)
    ctk.CTkLabel(follow_frame,text="",image=tab.fb,fg_color="black",).grid(row=1,column=0,padx=8)
    ctk.CTkLabel(follow_frame,text="",image=tab.insta,fg_color="black",).grid(row=1,column=1,padx=8)
    ctk.CTkLabel(follow_frame,text="",image=tab.x,fg_color="black",).grid(row=1,column=2,padx=8)
    ctk.CTkLabel(follow_frame,text="",image=tab.telegram,fg_color="black",).grid(row=1,column=3,padx=8)

    ctk.CTkLabel(details_frame,text="",fg_color="black").grid(row=5,column=0,pady=5)
    
    
    footer_frame = ctk.CTkFrame(lobby_frame,fg_color = "#3B1E54",corner_radius=0)
    footer_frame.grid(row=2,column=0,sticky="nswe")

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
    ctk.CTkButton(temp_footer,text="",image=tab.home_logo,width=0,fg_color = "#3B1E54").grid(row=0,column=0,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.mycart_logo,fg_color = "#3B1E54",
                  command=select_cart).grid(row=0,column=1,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.myorders_logo,fg_color = "#3B1E54",
                  command=lambda: notebook.select(my_orders)).grid(row=0,column=3,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.shop_logo,fg_color = "#3B1E54",
                  command=lambda: notebook.select(epharmacy)).grid(row=0,column=2,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.offers_logo,fg_color = "#3B1E54",
                  command=lambda: notebook.select(offers)).grid(row=0,column=4,padx=30)
    
    move_offer_1()

    return bucket

















