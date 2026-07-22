import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from functools import partial
import sqlite3
from CTkSpinbox import *

def all_drugs_tab(tab,notebook,home,epharmacies,cart,path,cart_func,orders,offers,bucket,services):


    mainframe=ctk.CTkFrame(tab,fg_color="#EEEEEE",corner_radius=0)
    mainframe.pack(fill="both",expand=True)

    mainframe.columnconfigure(0,weight=2)
    mainframe.rowconfigure(0,weight=0)
    mainframe.rowconfigure(1,weight=0)
    mainframe.rowconfigure(2,weight=2)

    title_container=ctk.CTkFrame(mainframe,fg_color="#3B1E54",corner_radius=0)
    title_container.grid(column=0,row=0,sticky="ew")

    image_path1 = path('back.png')
    tab.back = ctk.CTkImage(light_image=Image.open(image_path1),size=(44,44))

    ctk.CTkButton(title_container,text="",image = tab.back,hover_color="#3C1E51",fg_color="#3B1E54",width=55,
                  command = lambda:notebook.select(services)).pack(side="left",padx=10)
    ctk.CTkLabel(title_container,text="ALL-Drugs",fg_color="#3B1E54",height=60,font=("impact",35),text_color="white").pack(pady=5)

    all_item_frame=ctk.CTkScrollableFrame(mainframe,fg_color="#DCDCDC",corner_radius=0)
    all_item_frame.grid(row=2,column=0,sticky="nswe")
    all_item_frame.columnconfigure(0,weight=2)

    frame1=ctk.CTkFrame(all_item_frame,fg_color="#DCDCDC")
    frame1.grid(row=0,column=0,padx=10,pady=30)
    

    
    def add_to_cart(item,qty):

       bucket[item.get()]=qty.get()


    

    def insert_to_show(items,type_of_item):
            
        row=1
        column=0
        for name,price in items.items():

            connection = sqlite3.connect("pharmacy.db")
            cursor = connection.cursor()
            
            cursor.execute("SELECT image FROM images WHERE name = ?", (name,))
            binary_data = cursor.fetchone()
            
                        
            binary_data = binary_data[0]
            with open('retrieved_image.jpg', 'wb') as file:
                file.write(binary_data)
            img = Image.open('retrieved_image.jpg')
            img = img.resize((250, 250), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            
                     
            item1 = ctk.CTkFrame(type_of_item,fg_color="white")
            item1.grid(row=row,column=column,padx=30,pady=20)
            item_var1=tk.StringVar(value=name)
            ctk.CTkButton(item1,textvariable=item_var1,width=190,compound="top",image=img,fg_color="white",
                            height=190,text_color="black",border_color="#dd0e44",hover_color="white",border_width=2,font=("roboto",15,"bold")).pack(pady=5,padx=10)
            ctk.CTkLabel(item1,text=f"Rs.{price}.00",text_color="#60044a",font=("roboto",15,"bold")).pack(pady=10)
            qty_frame= ctk.CTkFrame(item1,fg_color="white")
            qty_frame.pack(padx=20)
            ctk.CTkLabel(qty_frame,text="Quantity: ",text_color="#60044a").pack(side="left",padx=5)
            qty_var1=tk.IntVar(value=0)
            spin=CTkSpinbox(qty_frame,start_value=1, min_value=1,max_value=99,font=("roboto",15,"bold"),variable=qty_var1,
                            height=37,fg_color="white",button_color="#EEEEEE",text_color="black",border_color="white",button_corner_radius=8)
            spin.pack(side="left")
            ctk.CTkButton(item1,text="ADD TO CART",command=partial(add_to_cart,item_var1,qty_var1),corner_radius=8,height=35,font=("calibri",15,"bold"),
                            width=150,fg_color="#dd0e44",text_color="white",hover_color="aqua").pack(pady=20)

            column+=1
            if column==3:
                row+=1
                column=0

    all_drugs = {}
    item_frames = [frame1]
    def run_all_drugs():
        i=0

        connection = sqlite3.connect("pharmacy.db")
        cursor = connection.cursor()

        cursor.execute("select name, price from all_items")
        items = cursor.fetchall()
        
        for item in items:
            all_drugs[item[0]]=item[1]

        connection.commit()
        connection.close()
        
        insert_to_show(all_drugs,item_frames[i])
            
                    
    run_all_drugs()

    footer_frame = ctk.CTkFrame(mainframe,fg_color = "#3B1E54",corner_radius=0)
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
                  command=lambda: notebook.select(home)).grid(row=0,column=0,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.mycart_logo,fg_color = "#3B1E54",
                  command=select_cart).grid(row=0,column=1,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.myorders_logo,fg_color = "#3B1E54",
                  command=lambda: notebook.select(orders)).grid(row=0,column=3,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.shop_logo,fg_color = "#3B1E54",
                  command=lambda: notebook.select(epharmacies)).grid(row=0,column=2,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.offers_logo,fg_color = "#3B1E54",
                  command=lambda: notebook.select(offers)).grid(row=0,column=4,padx=30)

    return bucket, run_all_drugs









