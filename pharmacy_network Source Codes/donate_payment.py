import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from functools import partial


def payment_task_donate(tab,home,notebook,path,donate):

    main_frame=ctk.CTkFrame(tab,fg_color="#EAEAEA")
    main_frame.pack(fill="both",expand=True)

    main_frame.columnconfigure(0,weight=2)
    main_frame.rowconfigure(0,weight=0)
    main_frame.rowconfigure(1,weight=2)


    nav=ctk.CTkFrame(main_frame,fg_color="#EAEAEA")
    nav.grid(row=0,column=0,sticky="nswe")
    nav.columnconfigure(0,weight=2)
    nav.columnconfigure(1,weight=0)

    ctk.CTkLabel(nav,text="",font=("verdana",25),text_color="black").grid(row=0,column=0)
    ctk.CTkButton(nav,text="Cancel",fg_color="white",border_width=2,command=lambda:notebook.select(donate),
                  text_color="black",font=("verdana",15),hover_color="aqua",
                  border_color="#DB0A41").grid(row=0,column=1,padx=10,pady=10)

    body_frame=ctk.CTkScrollableFrame(main_frame,fg_color="white")
    body_frame.grid(row=1,column=0,sticky="nwse")
    body_frame.columnconfigure(0,weight=2)

    status = ctk.StringVar()
    def credit_card():
        
        image_path1 = path('atm-card.png')
        tab.atm_card = ctk.CTkImage(light_image=Image.open(image_path1),size=(150,150))
        
        credit_card_frame=ctk.CTkFrame(body_frame,fg_color="#EAEAEA")
        credit_card_frame.grid(row=3,column=0,pady=50)

        ctk.CTkLabel(credit_card_frame,text="Pay With Card",font=("impact",25),text_color="black").grid(row=0,column=0,sticky="w",padx=20)
        ctk.CTkLabel(credit_card_frame,text="",image=tab.atm_card,text_color="black").grid(row=0,column=1,pady=30)

        details_frame= ctk.CTkFrame(credit_card_frame,fg_color="white",border_width=1,border_color="#DB0A41")
        details_frame.grid(row=1,column=0,columnspan=2,padx=20,pady=20)

        ctk.CTkLabel(details_frame,text="All Feilds Are Required",font=("verdana",13),text_color="black").grid(row=0,column=0,columnspan=2,pady=10,sticky="w",padx=30)
        ctk.CTkLabel(details_frame,text="Select Card",font=("verdana",15),text_color="black").grid(row=1,column=0,pady=10)

        cards_frame=ctk.CTkFrame(details_frame,fg_color="white")
        cards_frame.grid(row=1,column=1,padx=10,stick="w")
        card_value=tk.StringVar()

        visa =ctk.CTkRadioButton(cards_frame,border_color="#DB0A41",
                                            variable=card_value,font=("verdana",15),
                                            value="Visa",text="Visa",text_color="black")
        visa.pack(side = "left")

        mastercard = ctk.CTkRadioButton(cards_frame,border_color="#DB0A41",font=("verdana",15),
                                            variable=card_value,
                                            value="Mastercard",text="Mastercard",text_color="black")
        mastercard.pack(side = "left")

        card_number_var = tk.IntVar()
        ctk.CTkLabel(details_frame,text="Card Number",font=("verdana",15),text_color="black").grid(row=2,column=0,pady=10)
        ctk.CTkEntry(details_frame,height=35,width=400,textvariable=card_number_var,
                                         corner_radius=5,text_color="black",fg_color="white",
                                         border_color="#DB0A41").grid(row=3,column=0,columnspan=2,padx=30)

        ctk.CTkLabel(details_frame,text="Expiry date",font=("verdana",15),text_color="black").grid(row=4,column=0,pady=10)
        ctk.CTkLabel(details_frame,text="Security Code",font=("verdana",15),text_color="black").grid(row=4,column=1,pady=10)

        expiry_date_var = tk.StringVar()
        ctk.CTkEntry(details_frame,height=35,width=150,textvariable=expiry_date_var,
                                         corner_radius=5,text_color="black",fg_color="white",
                                         border_color="#DB0A41").grid(row=5,column=0,padx=20)

        security_code_var=tk.IntVar()
        ctk.CTkEntry(details_frame,height=35,width=150,textvariable=security_code_var,
                                         corner_radius=5,text_color="black",fg_color="white",
                                         border_color="#DB0A41").grid(row=5,column=1,sticky="e",padx=30)

        holder_name_var=tk.StringVar()
        ctk.CTkLabel(details_frame,text="Name on Card",font=("verdana",15),text_color="black").grid(row=6,column=0,pady=10)
        ctk.CTkEntry(details_frame,height=35,width=400,textvariable=holder_name_var,
                                         corner_radius=5,text_color="black",fg_color="white",
                                         border_color="#DB0A41").grid(row=7,column=0,columnspan=2)

        
        def pay_now_run_sucecss(state):
            status.set("Success")
            notebook.select(home)
            

        def pay_now_run_pending(state):
            status.set(state)
            notebook.select(donate)
            
            
            
        ctk.CTkButton(details_frame,text="Pay Now",width=120,height=40,font=("verdana",15,"bold"),text_color="black",
                          fg_color="yellow",corner_radius=5,command=partial(pay_now_run_sucecss,"Sucess")).grid(row=8,column=1,pady=30)

        ctk.CTkButton(details_frame,text="Cancel",width=120,height=40,font=("verdana",15,"bold"),text_color="black",
                          fg_color="yellow",corner_radius=5,command=partial(pay_now_run_pending,"Pending")).grid(row=8,column=0,pady=30)



    def bank_transfer():

        

        credit_card_frame=ctk.CTkFrame(body_frame,fg_color="#EAEAEA")
        credit_card_frame.grid(row=3,column=0,pady=50)

        ctk.CTkLabel(credit_card_frame,text="This Option NoT Availabale",height=680,width=425,font=("impact",30),text_color="black").grid(row=0,column=0,sticky="w",padx=20)
        ctk.CTkLabel(credit_card_frame,text="",text_color="black").grid(row=0,column=1,pady=30)



    image_path2 = path('bank.png')
    tab.bank = ctk.CTkImage(light_image=Image.open(image_path2),size=(100,100))

    image_path3 = path('credit.png')
    tab.card = ctk.CTkImage(light_image=Image.open(image_path3),size=(100,100))
    

    ctk.CTkLabel(body_frame,text="Select Your Payment Option",font=("impact",30),text_color="black").grid(row=1,column=0,pady=30)
    option_frame=ctk.CTkFrame(body_frame,fg_color="white")
    option_frame.grid(row=2,column=0,columnspan=2)

    ctk.CTkButton(option_frame,image=tab.card,text="credit card",font=("calibri",20,"bold"),text_color="black",compound="top",fg_color="white",
                  width=200,command=credit_card,height=100).grid(row=0,column=0,padx=20,pady=15)
    ctk.CTkButton(option_frame,image=tab.bank,text="Bank Transfer",compound="top",font=("calibri",20,"bold"),text_color="black",fg_color="white",
                  width=200,command=bank_transfer,height=100).grid(row=0,column=1,padx=25,pady=10)

    









    


