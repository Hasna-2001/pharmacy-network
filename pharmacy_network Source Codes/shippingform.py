import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import datetime

def shipping_form(tab,notebook,path,cart,total,payment,home):

    main_frame = ctk.CTkFrame(tab,fg_color="grey")
    main_frame.pack(fill="both",expand=True)

    main_frame.columnconfigure(0,weight=2)
    main_frame.rowconfigure(0,weight=0)
    main_frame.rowconfigure(1,weight=2)

    nav=ctk.CTkFrame(main_frame,fg_color="red",corner_radius=0)
    nav.grid(row=0,column=0,sticky="we")

    nav.columnconfigure(0,weight=0)
    nav.columnconfigure(1,weight=2)
    nav.columnconfigure(2,weight=0)


    ctk.CTkLabel(nav,text="Secure Checkout",font=("impact",25),text_color="white").grid(row=0,column=1,padx=20,pady=10)

    body_frame=ctk.CTkFrame(main_frame,fg_color="#EAEAEA",corner_radius=0)
    body_frame.grid(row=1,column=0,sticky="nswe")

    body_frame.columnconfigure(0,weight=2)
    body_frame.columnconfigure(1,weight=1)
    body_frame.rowconfigure(0,weight=0)
    body_frame.rowconfigure(1,weight=2)



    ctk.CTkLabel(body_frame,text="SHIPPING FORM",
                 font=("impact",20),text_color="black").grid(row=0,column=0,padx=20,sticky="w")

    ctk.CTkButton(body_frame,text="EDIT CART",height=35,border_width=2,command=lambda:notebook.select(cart),
                                 corner_radius=5,fg_color="white",border_color="#DB0A41",
                 font=("calibri",15),text_color="black").grid(row=0,column=1,pady=10,sticky="e",padx=20)

    form_frame=ctk.CTkScrollableFrame(body_frame,fg_color="white")
    form_frame.grid(row=1,column=0,sticky="nswe",padx=20)

    form_frame.columnconfigure(0,weight=1)
    form_frame.columnconfigure(1,weight=2)

    ctk.CTkLabel(form_frame,text="Country:",font=("verdana",15),text_color="black").grid(row=0,column=0,padx=20,sticky="e")
    country=["Sri Lanka","India","United states","United Kingdom","Pakistan","Bangaladesh","Nepal"]
    country_value = tk.StringVar(value=country[0])
    select_country=ctk.CTkComboBox(form_frame,height=35,variable=country_value,width=250,
                                 corner_radius=5,text_color="black",fg_color="white",
                                 border_color="#DB0A41",button_color="#DB0A41",dropdown_fg_color="#880066")
    select_country.configure(values=country)
    select_country.grid(row=0,column=1,sticky="w",pady=10,padx=20)

    
    ctk.CTkLabel(form_frame,text="First Name:",font=("verdana",15),text_color="black").grid(row=1,column=0,padx=20,sticky="e")
    fname=ctk.CTkEntry(form_frame,placeholder_text="LAST NAME",height=35,width=250,
                                 corner_radius=5,text_color="black",fg_color="white",
                                 border_color="#DB0A41")
    fname.grid(row=1,column=1,sticky="w",pady=10,padx=20)

    
    ctk.CTkLabel(form_frame,text="Last Name:",font=("verdana",15),text_color="black").grid(row=2,column=0,sticky="e",padx=20)
    lname=ctk.CTkEntry(form_frame,placeholder_text="FIRST NAME",height=35,width=250,
                                 corner_radius=5,text_color="black",fg_color="white",
                                 border_color="#DB0A41")
    lname.grid(row=2,column=1,sticky="w",pady=10,padx=20)


    ctk.CTkLabel(form_frame,text="Company Name:",
                    font=("verdana",15),text_color="black").grid(row=3,column=0,sticky="e",padx=20)
    comapany_name=ctk.CTkEntry(form_frame,placeholder_text="Optional",height=35,width=250,
                                corner_radius=5,text_color="black",fg_color="white",
                                border_color="#DB0A41")
    comapany_name.grid(row=3,column=1,sticky="w",pady=10,padx=20)



    address1_value = tk.StringVar()
    ctk.CTkLabel(form_frame,text="Address 1:",font=("verdana",15),text_color="black").grid(row=4,column=0,sticky="e",padx=20)
    address1=ctk.CTkEntry(form_frame,textvariable=address1_value,height=35,width=250,
                                 corner_radius=5,text_color="black",fg_color="white",
                                 border_color="#DB0A41")
    address1.grid(row=4,column=1,sticky="w",pady=10,padx=20)

    address2_value = tk.StringVar()
    ctk.CTkLabel(form_frame,text="Address 2:",font=("verdana",15),text_color="black").grid(row=5,column=0,sticky="e",padx=20)
    address2=ctk.CTkEntry(form_frame,textvariable=address2_value,height=35,width=250,
                                 corner_radius=5,text_color="black",fg_color="white",
                                 border_color="#DB0A41")
    address2.grid(row=5,column=1,sticky="w",pady=10,padx=20)

    zip_value = tk.StringVar()
    ctk.CTkLabel(form_frame,text="ZIP:",font=("verdana",15),text_color="black").grid(row=6,column=0,sticky="e",padx=20)
    zipcode=ctk.CTkEntry(form_frame,textvariable=zip_value,height=35,width=120,
                                 corner_radius=5,text_color="black",fg_color="white",
                                 border_color="#DB0A41")
    zipcode.grid(row=6,column=1,sticky="w",pady=10,padx=20)

    temp_frame= ctk.CTkFrame(form_frame,fg_color="aqua")
    temp_frame.grid(row=7,column=1,sticky="w",padx=20)

    ctk.CTkLabel(form_frame,text="City:",font=("verdana",15),text_color="black").grid(row=7,column=0,padx=20,sticky="e",pady=10)
    city_value = tk.StringVar()
    city=ctk.CTkEntry(temp_frame,textvariable=city_value,height=35,width=200,
                                 corner_radius=5,text_color="black",fg_color="white",
                                 border_color="#DB0A41")
    city.grid(row=0,column=1)

    phone_value = tk.StringVar()
    ctk.CTkLabel(form_frame,text="Phone:",font=("verdana",15),text_color="black").grid(row=8,column=0,sticky="e",padx=20)
    phone=ctk.CTkEntry(form_frame,textvariable=phone_value,height=35,width=250,
                                 corner_radius=5,text_color="black",fg_color="white",
                                 border_color="#DB0A41")
    phone.grid(row=8,column=1,sticky="w",pady=10,padx=20)

    email_value = tk.StringVar()
    ctk.CTkLabel(form_frame,text="Email:",font=("verdana",15),text_color="black").grid(row=9,column=0,sticky="e",padx=20)
    email=ctk.CTkEntry(form_frame,textvariable=email_value,height=35,width=250,
                                 corner_radius=5,text_color="black",fg_color="white",
                                 border_color="#DB0A41")
    email.grid(row=9,column=1,sticky="w",pady=10,padx=20)


    def save():
        select_country.configure(state="disabled")
        fname.configure(state="disabled")
        lname.configure(state="disabled")
        address1.configure(state="disabled")
        address2.configure(state="disabled")
        zipcode.configure(state="disabled")
        city.configure(state="disabled")
        phone.configure(state="disabled")
        email.configure(state="disabled")
        comapany_name.configure(state="disabled")


    def reset():
        select_country.configure(state="normal")
        fname.configure(state="normal")
        lname.configure(state="normal")
        address1.configure(state="normal")
        address2.configure(state="normal")
        zipcode.configure(state="normal")
        city.configure(state="normal")
        phone.configure(state="normal")
        email.configure(state="normal")
        comapany_name.configure(state="normal")
        

        fname_value.set("First Name")
        lname_value.set("Last Name")
        comapany_name_value.set("Optional")
        address1_value.set("")
        address2_value.set("")
        zip_value.set("")
        city_value.set("")
        phone_value.set("")
        email_value.set("")
        country_value.set(country[0])
            
    checkouted_items = {}
    now= datetime.datetime.now()
    

    def run_order_items():
        checkouted_items[f"{total.get()}.00"]=now.strftime("%Y-%m-%d")
        notebook.select(payment)
    
    
    button_frame=ctk.CTkFrame(form_frame,fg_color="white")
    button_frame.grid(row=10,column=0,columnspan=2)
    ctk.CTkButton(button_frame,text="Save",height=35,fg_color="#880066",command=save,
                  font=("calibri",17,"bold"),
                          border_color="white",corner_radius=50).grid(row=0,column=0,pady=10,padx=10)

    ctk.CTkButton(button_frame,text="Reset",height=35,fg_color="#880066",command=reset,
                  font=("calibri",17,"bold"),
                          border_color="white",corner_radius=50).grid(row=0,column=1,pady=10,padx=10)

    ctk.CTkButton(button_frame,text="Cancel",height=35,fg_color="#880066",font=("calibri",17,"bold"),command=lambda:notebook.select(home),
                          border_color="white",corner_radius=50).grid(row=0,column=2,pady=10,padx=10)

        
    final_total=tk.StringVar()

    bill_frame = ctk.CTkFrame(body_frame,fg_color="#EAEAEA")
    bill_frame.grid(row=1,column=1,sticky="nswe")

    tempframe1=ctk.CTkFrame(bill_frame,fg_color="white")
    tempframe1.pack(fill="both",padx=20)

    tempframe1.columnconfigure(0,weight=1)
    tempframe1.columnconfigure(1,weight=1)

    ctk.CTkLabel(tempframe1,text="Subtotal:",font=("verdana",15),text_color="black").grid(row=0,column=0,sticky="w",padx=30)
    ctk.CTkLabel(tempframe1,text="00.00",textvariable=final_total,font=("verdana",15),text_color="black").grid(row=0,column=1,sticky="e",padx=30)

    ctk.CTkLabel(tempframe1,text="Shipping:",font=("verdana",15),text_color="black").grid(row=1,column=0,sticky="w",padx=30)
    ctk.CTkLabel(tempframe1,text="00.00",font=("verdana",15),text_color="black").grid(row=1,column=1,sticky="e",padx=30)

    ctk.CTkLabel(tempframe1,text="Taxes:",font=("verdana",15),text_color="black").grid(row=2,column=0,sticky="w",padx=30)
    ctk.CTkLabel(tempframe1,text="00.00",font=("verdana",15),text_color="black").grid(row=2,column=1,sticky="e",padx=30)

    ctk.CTkLabel(tempframe1,text="----------------------------------------",font=("verdana",15),text_color="black").grid(row=3,column=0,columnspan=2)
    ctk.CTkLabel(tempframe1,text="Final Total:",font=("verdana",15,"bold"),text_color="black").grid(row=4,column=0,sticky="w",padx=30)
    ctk.CTkLabel(tempframe1,text="00",textvariable=final_total,font=("verdana",15,"bold"),text_color="black").grid(row=4,column=1,sticky="e",padx=30)

    ctk.CTkButton(tempframe1,width=100,height=40,font=("verdana",15,"bold"),text_color="white",
                  fg_color="#880066",corner_radius=5,command=run_order_items,
                  text="PLACE ORDER").grid(row=5,column=0,columnspan=2,pady=30)


    def run():
        final_total.set(f"{total.get()}.00")

    
        

    return run, checkouted_items
        











