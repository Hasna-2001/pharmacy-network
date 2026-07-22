import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from functools import partial
import sqlite3
from tkinter import messagebox 



def my_oreder(tab,notebook,path,home,cart,checkouted_items,epharmacies,offers):

    #main frame in lobby
    pharm_easy = ctk.CTkFrame(tab,fg_color = "#EAEAEA")
    pharm_easy.pack(fill="both", expand=True)

    pharm_easy.columnconfigure(0,weight=2)
    pharm_easy.rowconfigure(0,weight=0)
    pharm_easy.rowconfigure(1,weight=0)
    pharm_easy.rowconfigure(2,weight=3)
    pharm_easy.rowconfigure(3,weight=0)
    
    #nave bar frame
    nav=ctk.CTkFrame(pharm_easy,fg_color="#3B1E54",corner_radius=0)
    nav.grid(row=0,column=0,sticky="we")
    nav.columnconfigure(0,weight=2)

    ctk.CTkLabel(nav,text="MY ORDERS",
                 font=("impact",35),text_color="white").grid(row=0,column=0,pady=5)    #profile icon button 
    

    #body frame 
    body_frame = ctk.CTkScrollableFrame(pharm_easy,fg_color = "#EAEAEA")
    body_frame.grid(row=2,column=0,sticky="nswe")
    #body_frame.columnconfigure(0,weight=2)
    body_frame.rowconfigure(1,weight=2)

    def clear():
        answer=messagebox.askokcancel(title="Conformation",message="Are You Sure?")
        if answer:
            connection = sqlite3.connect("pharmacy.db")
            cursor = connection.cursor()  
            cursor.execute("delete from new_orders")
            connection.commit()
            connection.close()
            my_order_list()

        else:
            pass
        

    ctk.CTkButton(pharm_easy,text="Clear All",command=clear,text_color="black",height=35,
                  fg_color="white",border_width=2,border_color="red",
                  font=("roboto",17,"bold")).grid(row=1,column=0,sticky="e",padx=15,pady=10)
    
    def my_order_list():
        row=0
        column=0
        orders = []
        connection = sqlite3.connect("pharmacy.db")
        cursor = connection.cursor()  
        cursor.execute("select order_id from new_orders")
        items = cursor.fetchall()
        
        for item in items:
            orders.append(item[0])
        
        container_frame = ctk.CTkFrame(body_frame,fg_color="#EAEAEA")
        container_frame.grid(row=0,column=0,sticky="nswe")
        for items in orders:
            items = [(items)]
            cursor.execute("select total,date,status from new_orders where order_id = ?",items)
            all_items = cursor.fetchall()
            bill_frame=ctk.CTkFrame(container_frame,fg_color="aqua")
            bill_frame.grid(row=row,column=column,pady=30,padx=20)
            
            
            ctk.CTkLabel(bill_frame,text="Payment Date:",font=("verdana",15),text_color="black").grid(row=0,column=0,padx=10,pady=5)
            ctk.CTkLabel(bill_frame,text=all_items[0][1],font=("verdana",15),text_color="black").grid(row=0,column=1,padx=10,pady=5)
            ctk.CTkLabel(bill_frame,text="Total:",font=("verdana",15),text_color="black").grid(row=1,column=0,padx=10,pady=5)
            ctk.CTkLabel(bill_frame,text=f"Rs.{all_items[0][0]}.00",font=("verdana",15),text_color="black").grid(row=1,column=1,padx=10,pady=5)
            ctk.CTkLabel(bill_frame,text="Payment Status:",font=("verdana",15),text_color="black").grid(row=2,column=0,padx=10,pady=5)
            ctk.CTkLabel(bill_frame,text=all_items[0][2],font=("verdana",15),text_color="black").grid(row=2,column=1,padx=10,pady=5)

            column+=1
            if column==3:
                row+=1
                column=0

        connection.commit()
        connection.close()
       

        
    






    my_order_list()

    footer_frame = ctk.CTkFrame(pharm_easy,fg_color = "#3B1E54",corner_radius=0)
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

    #Home icon button frame
    ctk.CTkButton(temp_footer,text="",image=tab.home_logo,width=0,fg_color = "#3B1E54",
                  command=lambda: notebook.select(home)).grid(row=0,column=0,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.mycart_logo,fg_color = "#3B1E54",
                  command=lambda:notebook.select(cart)).grid(row=0,column=1,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.shop_logo,fg_color = "#3B1E54",
                  command=lambda: notebook.select(epharmacies)).grid(row=0,column=2,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.myorders_logo,fg_color = "#3B1E54").grid(row=0,column=3,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.offers_logo,fg_color = "#3B1E54",
                  command=lambda:notebook.select(offers)).grid(row=0,column=4,padx=30)


    return my_order_list



















