import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk






def epharmacy(tab,signin,signup,notebook,home,pharm_easy,
              path,medicap,cart,cart_func,offers,my_orders,fitness_store,baby_care,skincare):

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
    #profile icon button frame
    profil_icon_frame = ctk.CTkFrame(navbar,fg_color = "#3B1E54")
    profil_icon_frame.grid(row=0,column=0,sticky="w",pady=5)

    ctk.CTkLabel(profil_icon_frame,text="",corner_radius=50).pack(side="left")
    
    #body frame 
    body_frame = ctk.CTkScrollableFrame(lobby_frame,fg_color = "#EEEEEE",corner_radius=0)
    body_frame.grid(row=1,column=0,sticky="nswe")

    body_frame.columnconfigure(0,weight=2)

    align_fram = ctk.CTkFrame(body_frame,fg_color="white")
    align_fram.grid(row=0,column=0,pady=50)

    ctk.CTkLabel(align_fram,text="E-Pharmacies",text_color="black",
                 font=("impact",25)).grid(row=0,column=0,padx=5,pady=10)
    
    #pharmacy 1
    #pharm easy logo image
    image_path1 = path('logo2.png')
    tab.pharm_easy_logo = ctk.CTkImage(light_image=Image.open(image_path1),size=(180,80))

    epharmacy_logo_frame1 = ctk.CTkFrame(align_fram,fg_color="white",corner_radius=20)
    epharmacy_logo_frame1.grid(row=1,column=0,padx=35,pady=10)

    epharmacy1=ctk.CTkButton(epharmacy_logo_frame1,text="",corner_radius=20,
                             image=tab.pharm_easy_logo,fg_color="white",hover_color="#EAEAEA",
                             width=200,height=200,command=lambda:notebook.select(pharm_easy))
    epharmacy1.pack()

 

    #pharmacy 2
    #medicap logo image
    image_path2 = path('medicap.png')
    tab.medicap_logo = ctk.CTkImage(light_image=Image.open(image_path2),size=(180,80))
    
    epharmacy_logo_frame2 = ctk.CTkFrame(align_fram,fg_color="white",corner_radius=20,)
    epharmacy_logo_frame2.grid(row=1,column=1,padx=35,pady=10)

    epharmacy2=ctk.CTkButton(epharmacy_logo_frame2,text="",command=lambda:notebook.select(medicap),
                             image=tab.medicap_logo,hover_color="#EAEAEA",
                             fg_color="white",
                             width=200,height=200)
    epharmacy2.pack()

 

    #pharmacy 3
    #pearl vsion
    image_path3 = path('fit2.png')
    tab.pearlvision = ctk.CTkImage(light_image=Image.open(image_path3),size=(190,130))
    epharmacy_logo_frame3 = ctk.CTkFrame(align_fram,fg_color="white")
    epharmacy_logo_frame3.grid(row=1,column=2,padx=35,pady=10)

    epharmacy3=ctk.CTkButton(epharmacy_logo_frame3,text="",image=tab.pearlvision,fg_color="white",hover_color="#EAEAEA",
                             width=200,height=200,command = lambda:notebook.select(fitness_store))
    epharmacy3.pack()

   

    #pharmacy 4
    #baby care logo image
    image_path4 = path('babycare.png')
    tab.babycare = ctk.CTkImage(light_image=Image.open(image_path4),size=(150,140))
    epharmacy_logo_frame4 = ctk.CTkFrame(align_fram,fg_color="white")
    epharmacy_logo_frame4.grid(row=2,column=0,padx=35,pady=10)

    epharmacy4=ctk.CTkButton(epharmacy_logo_frame4,text="BABY CARE",image=tab.babycare,hover_color="#EAEAEA",
                             width=200,height=200,compound="top",fg_color="white",
                             font=("calibri",23,"bold"),text_color="#0b7992",command=lambda:notebook.select(baby_care))
    epharmacy4.pack()

    #pharmacy 5
    #Skin care logo image
    image_path4 = path('skin_care2.png')
    tab.babycare = ctk.CTkImage(light_image=Image.open(image_path4),size=(180,180))
    epharmacy_logo_frame5 = ctk.CTkFrame(align_fram,fg_color="white")
    epharmacy_logo_frame5.grid(row=2,column=1,padx=35,pady=10)

    epharmacy5=ctk.CTkButton(epharmacy_logo_frame5,text="",image=tab.babycare,hover_color="#EAEAEA",
                             width=200,height=200,fg_color="white",
                             font=("calibri",20,"bold"),text_color="#0b7992",command=lambda:notebook.select(skincare))
    epharmacy5.pack()

    
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
    ctk.CTkButton(temp_footer,text="",image=tab.home_logo,width=0,fg_color = "#3B1E54",
                  command=lambda: notebook.select(home)).grid(row=0,column=0,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.mycart_logo,fg_color = "#3B1E54",
                  command=select_cart).grid(row=0,column=1,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.myorders_logo,command=lambda:notebook.select(my_orders),
                  fg_color = "#3B1E54").grid(row=0,column=3,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.shop_logo,fg_color = "#3B1E54").grid(row=0,column=2,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.offers_logo,fg_color = "#3B1E54",command=lambda:notebook.select(offers)).grid(row=0,column=4,padx=30)
    


        






    

















