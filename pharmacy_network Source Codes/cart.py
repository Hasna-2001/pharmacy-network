import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from functools import partial
from tkinter import messagebox
import sqlite3



def picked_items(tab,signin,signup,notebook,home,epharmacies,bucket,bucket2,refresh_total,checkout_page,path,
                 bucket3,bucket4,offers,orders,bucket5,bucket7,bucket8,state,required_login):

    #main frame in lobby
    pharm_easy = ctk.CTkFrame(tab,fg_color = "#EEEEEE")
    pharm_easy.pack(fill="both", expand=True)

    pharm_easy.columnconfigure(0,weight=2)
    pharm_easy.rowconfigure(0,weight=0)
    pharm_easy.rowconfigure(1,weight=3)
    pharm_easy.rowconfigure(2,weight=0)
    #nave bar frame
    navbar = ctk.CTkFrame(pharm_easy,fg_color = "#3B1E54",corner_radius=0)
    navbar.grid(row=0,column=0,sticky="nswe")
    
    navbar.columnconfigure(0,weight=0)
    navbar.columnconfigure(1,weight=2)

    ctk.CTkLabel(navbar,text="YOUR PICKS",font=("impact",25),
                 text_color="white").grid(row=0,column=0,sticky="w",padx=15,pady=10)

    
    
    def sohw(a):
        del bucket[a]
        show_items()
        
    for name,price in bucket2.items():
        bucket[name]=price

    for name,price in bucket3.items():
            bucket[name]=price

    for name,price in bucket4.items():
            bucket[name]=price

    for name,price in bucket5.items():
            bucket[name]=price

    for name,price in bucket7.items():
            bucket[name]=price

    for name,price in bucket8.items():
            bucket[name]=price
    
    total_var=tk.IntVar()

    def show_items():

        row=2
        column=0
        total=0

        connection = sqlite3.connect("pharmacy.db")
        cursor = connection.cursor()

        temp_frame2 = ctk.CTkScrollableFrame(body_frame,fg_color = "#DCDCDC")
        temp_frame2.grid(row=1,column=0,sticky="nswe")
        for selected_item,qty in bucket.items():
            
            cursor.execute("select price from all_items where name = ?",(selected_item,))
            price = cursor.fetchone()
            price = int(price[0])

            cursor.execute("select image from images where name = ?",(selected_item,))
            binary_data = cursor.fetchone()
            
            binary_data = binary_data[0]
            with open('retrieved_image.jpg', 'wb') as file:
                file.write(binary_data)
            img = Image.open('retrieved_image.jpg')
            img = img.resize((200, 200), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
                        
            picked_frame = ctk.CTkFrame(temp_frame2,fg_color="white")
            picked_frame.grid(row=row,column=column,padx=20,pady=30)

            ctk.CTkLabel(picked_frame,image=img,corner_radius = 10,text="").grid(row=0,column=0,rowspan=4,padx=5)      
            ctk.CTkLabel(picked_frame,text=f"{selected_item} x {qty}",font=("roboto",15,"bold"),
                            text_color="black").grid(row=0,column=1,pady=10,padx=15,columnspan=2,sticky="w")
            
            ctk.CTkLabel(picked_frame,text=f"Price:         Rs.{price}.00",font=("roboto",15,"bold"),
                            text_color="black").grid(row=1,column=1,pady=10,padx=15,columnspan=2,sticky="w")
            
            ctk.CTkLabel(picked_frame,text="Total :",font=("roboto",15,"bold"),
                            text_color="black").grid(row=2,column=1,pady=10,padx=15,sticky="w")
            
            ctk.CTkLabel(picked_frame,text=f"Rs.{qty*price}.00",font=("roboto",15,"bold"),
                            text_color="black").grid(row=2,column=2,pady=10,padx=20,sticky="w")
            
            ctk.CTkButton(picked_frame,text="Remove Item",height=35,command=partial(sohw,selected_item),
                            font=("impact",17)).grid(row=3,column=1,columnspan=2,pady=10,sticky="w",padx=10)
            column+=1
            if column==2:
                row+=1
                column=0
        
        for selected_item,qty in bucket.items():
            cursor.execute("select price from all_items where name = ?",(selected_item,))
            price = cursor.fetchone()
            total+=int(price[0])*qty
    
        total_var.set(total)
        sybtotal_label = ctk.CTkLabel(checkout_frame,text =f"Your Sub Total:   Rs.{total}.00",font=("roboto",18,"bold"),text_color="black")
        sybtotal_label.grid(row=0,column=0,sticky="e",padx=10)
        
        

    def go_to_checkout():
        if bucket == {}:
            messagebox.showwarning(title="WARNING", message="Your Cart is empty!")

        elif state.get() == "Logedin":
            notebook.select(checkout_page)
            refresh_total()
            
        else:
            notebook.select(required_login)
                    
                

    #body frame 
    body_frame = ctk.CTkFrame(pharm_easy,fg_color = "#DCDCDC",corner_radius=0)
    body_frame.grid(row=1,column=0,sticky="nswe")
    body_frame.columnconfigure(0,weight=2)
    body_frame.rowconfigure(1,weight=2)

    checkout_frame = ctk.CTkFrame(body_frame,fg_color="#DCDCDC",corner_radius=0)
    checkout_frame.grid(row=2,column=0,pady=10,sticky="we")

    checkout_frame.columnconfigure(0,weight=11)
    checkout_frame.columnconfigure(1,weight=1)
    
    ctk.CTkButton(checkout_frame,text="Checkout Now",command=go_to_checkout,width=90
                  ,height=35,font=("impact",18)).grid(row=0,column=1,padx=15,sticky="e")

    
 
    footer_frame = ctk.CTkFrame(pharm_easy,fg_color = "#3B1E54",corner_radius=0)
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

    #Home icon button frame
    ctk.CTkButton(temp_footer,text="",image=tab.home_logo,width=0,fg_color = "#3B1E54",
                  command=lambda: notebook.select(home)).grid(row=0,column=0,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.mycart_logo,fg_color = "#3B1E54").grid(row=0,column=1,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.shop_logo,fg_color = "#3B1E54",
                  command=lambda: notebook.select(epharmacies)).grid(row=0,column=2,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.myorders_logo,fg_color = "#3B1E54",
                  command = lambda: notebook.select(orders)).grid(row=0,column=3,padx=30)
    ctk.CTkButton(temp_footer,text="",width=0,image=tab.offers_logo,fg_color = "#3B1E54",
                  command = lambda: notebook.select(offers)).grid(row=0,column=4,padx=30)
   


    return show_items,total_var
  


















