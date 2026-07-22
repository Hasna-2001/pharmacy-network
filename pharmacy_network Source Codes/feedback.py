import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk


def reviwe(tab,notebook,path,home,cart_func,cart,my_orders,epharmacies,offers,services):

    main_frame=ctk.CTkFrame(tab,fg_color="white")
    main_frame.pack(fill="both",expand=True)

    main_frame.columnconfigure(0,weight=2)
    main_frame.rowconfigure(0,weight=0)
    main_frame.rowconfigure(1,weight=2)

    nav=ctk.CTkFrame(main_frame,fg_color="#3B1E54",corner_radius=0)
    nav.grid(row=0,column=0,sticky="we")
    nav.columnconfigure(0,weight=0)
    nav.columnconfigure(1,weight=2)
            

    ctk.CTkLabel(nav,text="",
                 font=("impact",35),text_color="white").grid(row=0,column=1,pady=5)

    image_path1 = path('back.png')
    tab.back = ctk.CTkImage(light_image=Image.open(image_path1),size=(44,44))

    ctk.CTkButton(nav,text="",image = tab.back,hover_color="#3C1E51",fg_color="#3B1E54",width=55,
                  command = lambda:notebook.select(services)).grid(row=0,column=0,pady=5)

    body_frame=ctk.CTkFrame(main_frame,fg_color="#EAEAEA")
    body_frame.grid(row=1,column=0,sticky="nswe")

    body_frame.columnconfigure(0,weight=2)
                               
    content=ctk.CTkFrame(body_frame,fg_color="white")
    content.grid(row=0,column=0,pady=90)


    review_var=ctk.StringVar()
    ctk.CTkLabel(content,text="Write Your Feedbacks",text_color="black",
                 font=("calibri",20,"bold")).grid(column=0,row=0,pady=20)
    ctk.CTkTextbox(content,width=400,height=300,border_width=2,border_color="#DB0A41",text_color="black",fg_color="white").grid(row=1,column=0,padx=15)
    ctk.CTkButton(content,text="Submit",font=("calibri",15,"bold"),height=35,width=70,fg_color="#DB0A41").grid(row=2,column=0,pady=20)                           


    footer_frame = ctk.CTkFrame(main_frame,fg_color = "#3B1E54",corner_radius=0)
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
    ctk.CTkButton(temp_footer,text="",image=tab.home_logo,width=0,fg_color = "#3B1E54",
                  command=lambda: notebook.select(home)).grid(row=0,column=0,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.mycart_logo,fg_color = "#3B1E54",
                  command=select_cart).grid(row=0,column=1,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.myorders_logo,fg_color = "#3B1E54",
                  command=lambda: notebook.select(my_orders)).grid(row=0,column=3,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.shop_logo,fg_color = "#3B1E54",
                  command=lambda: notebook.select(epharmacies)).grid(row=0,column=2,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.offers_logo,fg_color = "#3B1E54",
                  command=lambda:notebook.select(offers)).grid(row=0,column=4,padx=30)
    






