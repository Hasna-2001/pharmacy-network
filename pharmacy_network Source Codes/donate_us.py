import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk


def donate(tab,notebook,path,lobby,cart,epharmacies,cart_func,payment,orders,offers,services):
    
    main_frame=ctk.CTkFrame(tab,fg_color="#EAEAEA")
    main_frame.pack(fill="both",expand=True)
    main_frame.columnconfigure(0,weight=2)

    main_frame.rowconfigure(0,weight=0)
    main_frame.rowconfigure(1,weight=0)
    main_frame.rowconfigure(2,weight=2)
    main_frame.rowconfigure(3,weight=0)



    nav=ctk.CTkFrame(main_frame,fg_color="#3B1E54",corner_radius=0)
    nav.grid(row=0,column=0,sticky="we")
    nav.columnconfigure(0,weight=0)
    nav.columnconfigure(1,weight=2)

    ctk.CTkLabel(nav,text="Donate For Charity",
                 font=("impact",35),text_color="white").grid(row=0,column=1,pady=5)

    image_path1 = path('back.png')
    tab.back = ctk.CTkImage(light_image=Image.open(image_path1),size=(44,44))

    ctk.CTkButton(nav,text="",image = tab.back,hover_color="#3C1E51",fg_color="#3B1E54",width=55,
                  command = lambda:notebook.select(services)).grid(row=0,column=0,pady=5)

    body_frame=ctk.CTkFrame(main_frame,fg_color="#EAEAEA")
    body_frame.grid(row=2,column=0,sticky="nswe")

    body_frame.columnconfigure(0,weight=2)
    donation_frame=ctk.CTkFrame(body_frame,fg_color="white")
    donation_frame.grid(row=0,column=0,pady=50)

    amount_var=ctk.IntVar()
    ctk.CTkLabel(donation_frame,text="Donation Information",text_color="black",font=("calibri",25,"bold")).grid(row=0,column=0,columnspan=3,pady=10)
    ctk.CTkButton(donation_frame,text="$10",fg_color="#016177",text_color="white",width=70,font=("calibri",15,"bold"),command=lambda:amount_var.set(10)).grid(row=1,column=0,padx=10,pady=10)
    ctk.CTkButton(donation_frame,text="$50",fg_color="#016177",text_color="white",width=70,font=("calibri",15,"bold"),command=lambda:amount_var.set(50)).grid(row=1,column=1,padx=10)
    ctk.CTkButton(donation_frame,text="$100",fg_color="#016177",text_color="white",width=70,font=("calibri",15,"bold"),command=lambda:amount_var.set(100)).grid(row=1,column=2,padx=18)

    ctk.CTkEntry(donation_frame,textvariable=amount_var,fg_color="white",border_color="#016177",
                 width=280,text_color="black",font=("calibri",15,"bold")).grid(row=2,column=0,columnspan=3,pady=10,padx=20)

    email_var=ctk.StringVar()
    ctk.CTkLabel(donation_frame,text="Email Adress",text_color="black",font=("calibri",15,"bold")).grid(row=3,column=0,pady=10,padx=15)
    ctk.CTkEntry(donation_frame,textvariable=email_var,fg_color="white",width=280,text_color="black",border_color="#016177",
                 font=("calibri",15,"bold")).grid(row=4,column=0,columnspan=3)
    ctk.CTkLabel(donation_frame,text="Full Name",text_color="black",font=("calibri",15,"bold")).grid(row=5,column=0,pady=10)

    nam_var=ctk.StringVar()
    ctk.CTkEntry(donation_frame,textvariable=nam_var,fg_color="white",text_color="black",border_color="#016177",
                 font=("calibri",15,"bold"),width=280).grid(row=6,column=0,columnspan=3)

    ctk.CTkButton(donation_frame,text="Donate Now",text_color="white",command=lambda:notebook.select(payment),
                  fg_color="#016177",font=("calibri",20,"bold"),height=35).grid(row=7,column=0,columnspan=3,pady=30)

   
 
    footer_frame = ctk.CTkFrame(main_frame,fg_color = "#3B1E54",corner_radius=0)
    footer_frame.grid(row=3,column=0,sticky="nswe")

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
    






        







