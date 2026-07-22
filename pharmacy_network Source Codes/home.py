import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk


move_x = 1
logo_y = 1
logo_image_x = 0.25 
logo_text_x = 0.25


btn2_x = 1
btn3_x = 1

button_get_start_x = 0.25
button_get_start_y = 0.5

def home_tab(tab,sign,home,login,notebook,path,lobby):


        mainframe = ctk.CTkFrame(tab,fg_color = "white")
        mainframe.pack(fill="both",expand = True)

        mainframe.columnconfigure(0,weight = 3)
        mainframe.columnconfigure(1,weight = 1)
        mainframe.rowconfigure(0,weigh=1)

        image_path1 = path('doctor2.png')
        tab.my_image = ctk.CTkImage(light_image=Image.open(image_path1),size=(280,400))

        image_path2 = path('medical-check.png')
        tab.my_logo = ctk.CTkImage(light_image=Image.open(image_path2),size=(200,200))

        image_path3 = path('start-up.png')
        tab.get_start = ctk.CTkImage(light_image=Image.open(image_path3),size=(38,38))
        

        
        
        
        def move_frame1():
            global move_x
            move_x-=0.01
            move_frame.place(relx=move_x,rely=0.11)
            if move_x>0:
                frame2.after(3,move_frame1)

            else:
                move_btn_2()

        def move_logo():
                global logo_y
                logo_y-=0.01
                log_frame.place(relx = 0.1,rely=logo_y)
                if logo_y>0.1:
                        frame1.after(6,move_logo)
                else:
                        move_logo_and_text()

        def move_logo_and_text():
            global logo_image_x
            logo_image_x+=0.005
            log_label.place(relx=logo_image_x,rely=0.1)
            if logo_image_x<0.47:
                log_frame.after(10,move_logo_and_text)

            else:
                movegetstart()
                
            global logo_text_x
            logo_text_x-=0.005
            log_text.place(relx=logo_text_x,rely=0.4)
            if logo_image_x<0.05:
                log_frame.after(10,move_logo_and_text)

            global button_get_start_x
            button_get_start_x-=0.005
            button_get_start.place(relx=button_get_start_x,rely=button_get_start_y)
            if logo_image_x<0.045:
                log_frame.after(10,move_logo_and_text)
            
            
            
            

        def move_btn_2():
            global btn2_x
            btn2_x-=0.01
            btn_frame.place(relx=btn2_x,rely=0.65)
            if btn2_x>0.2:
                frame2.after(3,move_btn_2)
            else:
                move_btn_3()

            
        def move_btn_3():
            global btn3_x
            btn3_x-=0.01
            btn_frame2.place(relx=btn3_x,rely=0.78)
            if btn3_x>0.2:
                frame2.after(3,move_btn_3)

        def movegetstart():
            global button_get_start_y
            button_get_start_y+=0.0054
            button_get_start.place(relx=0.09,rely=button_get_start_y)
            if button_get_start_y<0.80:
                log_frame.after(7,movegetstart)
                
                

        

        frame1=ctk.CTkFrame(mainframe,fg_color = "#dbfffd")
        frame1.grid(row=0,column=0,sticky = "nswe")

        frame2=ctk.CTkFrame(mainframe,fg_color = "#016177",corner_radius=0)
        frame2.grid(row=0,column=1,sticky = "nswe")


        move_frame = ctk.CTkFrame(frame2,fg_color = "#016177",width=300,height=350)
        move_frame.place(relx=move_x,rely=0.1)


        ctk.CTkLabel(move_frame,text="",image = tab.my_logo,font=("impact",35),
                     text_color="white").grid(row=0,column=0,padx=10,pady=10)

        ctk.CTkLabel(move_frame,text="Access a wide range of health products\n and services\nfrom the comfort of yor home",
                     font=("calibri",20,"bold"),
                     text_color="white").grid(row=1,column=0,padx=10,pady=10)




        btn_frame = ctk.CTkFrame(frame2,fg_color="#016177")
        btn_frame.place(relx=btn2_x,rely=0.7)

        ctk.CTkLabel(btn_frame,text = "Already a member of our network?",text_color="white",font=("calibri",15),fg_color="#016177").grid(row=0,column=0,sticky="w")
        ctk.CTkButton(btn_frame,text = "Log in",border_color = "#00a0aa",border_width=2,command = lambda: notebook.select(login),
                      font = ("calibri",20,"bold"),fg_color="white",text_color="black",
                      width=220,height=40).grid(row=1,column=0,sticky="w")

        btn_frame2 = ctk.CTkFrame(frame2,fg_color="#016177")
        btn_frame2.place(relx=btn3_x,rely=0.82)

        ctk.CTkLabel(btn_frame2,text = "Join Our Network",text_color="white",font=("calibri",15)).grid(row=0,column=0,sticky="w")
        ctk.CTkButton(btn_frame2,text = "Sign up",font = ("calibri",20,"bold"),fg_color="white",command = lambda: notebook.select(sign),
                      text_color="black",
                      width=220,height=40,border_color = "#00a0aa",border_width=2).grid(row=1,column=0,sticky="w")

        log_frame = ctk.CTkFrame(frame1,fg_color = "#dbfffd",width=600,height = 400)
        log_frame.place(relx = 0.05,rely=logo_y)

        button_get_start = ctk.CTkButton(log_frame,text = "GET START",fg_color="#DB0A41",text_color="white",corner_radius = 10,
                                width=170,height=55,border_color = "white",command = lambda:notebook.select(lobby),
                                         border_width=2,font = ("calibri",18,"bold"),image = tab.get_start,compound="right")
        button_get_start.place(relx=button_get_start_x,rely=button_get_start_y)

        log_text = ctk.CTkLabel(log_frame,text = "STEP INTO WORLD\nOF\nWELLNESS",text_color = "#016177",
                                 font = ("impact",35))
        log_text.place(relx=logo_text_x,rely=0.3)

        log_label = ctk.CTkLabel(log_frame,text = "",image = tab.my_image,
                                 font = ("impact",50))
        log_label.place(relx=logo_image_x,rely=0.1)




            


        
        move_frame1()
        move_logo()


        
        
        
        
        
        
        
        

        
