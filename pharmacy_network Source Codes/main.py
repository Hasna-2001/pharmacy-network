import os
import sys
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk	
from login import login_tab
from signin import signin_tab
from home import home_tab
from pharmacient_form import pharmacient_form
from doctor_form import doctor_form
from lobby import lobby
from epharmacies import epharmacy
from pharmacy_1 import pharm_easy   
from cart import picked_items
from new_item_add_form import add_new_items
from pharmacy_2 import medicap
from cart_sign_in import cart_login_tab
from shippingform import shipping_form
from payment import payment_task
from recipt import upload_recipt
from nearby_pharmacy import nearby_stores
from doctors import Doctors
from my_orders import my_oreder
from donate_us import donate
from feedback import reviwe
from our_services import services
from offers import show_offer
from username_pswrd import create_username
from add_pharmacy_form import add_pharmacy_frm
from username_pswrd2 import create_username2
from username_pswrd3 import create_username3
from donate_payment import payment_task_donate
from fitness import fitness_store
from admin_panel_page import admin_pannel
from admin_add_pharmacy import admin_pharmacy_frm
from admin_doctors_form import admin_doctor_form
from add_offers import add_offers_form
from baby_care import baby_care_store
from skin_care import skincare_shop
from all_drugs import all_drugs_tab
from remove_pharmacy import remove_pharmacy_tab
from remove_doctors import remove_doc


class Pharmacy:

    def resource_path(self,relative_path):
   
        try:
            self.base_path = sys._MEIPASS
        except Exception:
            self.base_path = os.path.abspath(".")

        return os.path.join(self.base_path, relative_path)

    def __init__(self,window):
        
        self.window=window
        self.window.geometry("1000x700")
        self.window.title("Pharmacy Network")
        self.window.resizable(False, False)

        self.notebook=ttk.Notebook(self.window)
        self.notebook.pack(fill="both",expand=True)

        self.home_tab=ctk.CTkFrame(self.window)
        self.signin_tab=ctk.CTkFrame(self.window)
        self.login_tab=ctk.CTkFrame(self.window)
        self.pharmaciet_tab=ctk.CTkFrame(self.window)
        self.doctor_tab=ctk.CTkFrame(self.window)
        self.lobby_tab=ctk.CTkFrame(self.window)
        self.epharmacy_tab=ctk.CTkFrame(self.window)
        self.pharm_easy_tab=ctk.CTkFrame(self.window)
        self.cart_tab=ctk.CTkFrame(self.window)
        self.add_new_items=ctk.CTkFrame(self.window)
        self.medi_cap_tab=ctk.CTkFrame(self.window)
        self.cart_signin_tab=ctk.CTkFrame(self.window)
        self.shipping_form_tab=ctk.CTkFrame(self.window)
        self.payment_tab=ctk.CTkFrame(self.window)
        self.upload_recipt_tab=ctk.CTkFrame(self.window)
        self.neraby_pharmacy_tab=ctk.CTkFrame(self.window)
        self.doctors_tab=ctk.CTkFrame(self.window)
        self.orders_tab=ctk.CTkFrame(self.window)
        self.donate_tab=ctk.CTkFrame(self.window)
        self.feed_back_tab=ctk.CTkFrame(self.window)
        self.services_tab=ctk.CTkFrame(self.window)
        self.offers_tab=ctk.CTkFrame(self.window)
        self.username_tab=ctk.CTkFrame(self.window)
        self.alldrugs_tab=ctk.CTkFrame(self.window)
        self.images_tab=ctk.CTkFrame(self.window)
        self.add_pharmacy_form_tab=ctk.CTkFrame(self.window)
        self.username_tab2=ctk.CTkFrame(self.window)
        self.username_tab3=ctk.CTkFrame(self.window)
        self.doante_pay=ctk.CTkFrame(self.window)
        self.fitness_store_tab=ctk.CTkFrame(self.window)
        self.admin_tab=ctk.CTkFrame(self.window)
        self.admin_addpharmacy_form=ctk.CTkFrame(self.window)
        self.admin_doctor_form=ctk.CTkFrame(self.window)
        self.add_offers=ctk.CTkFrame(self.window)
        self.baby_care_tab=ctk.CTkFrame(self.window)
        self.skin_care_tab=ctk.CTkFrame(self.window)
        self.remove_pharmacy_tab=ctk.CTkFrame(self.window)
        self.remove_doctors_tab=ctk.CTkFrame(self.window)
        self.remove_pharmeasy_tab=ctk.CTkFrame(self.window)
        
        
        
        self.notebook.add(self.home_tab,text="Home")
        self.notebook.add(self.signin_tab,text="Sign in")
        self.notebook.add(self.login_tab,text="Log in")
        self.notebook.add(self.pharmaciet_tab,text="pharmacient")
        self.notebook.add(self.doctor_tab,text="doctor")
        self.notebook.add(self.lobby_tab,text="lobby")
        self.notebook.add(self.epharmacy_tab,text="epharmacy")
        self.notebook.add(self.pharm_easy_tab,text="Pharm Easy")
        self.notebook.add(self.cart_tab,text="My Cart")
        self.notebook.add(self.add_new_items,text="new items add form")
        self.notebook.add(self.medi_cap_tab,text="medicap")
        self.notebook.add(self.cart_signin_tab,text="cart signin")
        self.notebook.add(self.shipping_form_tab,text="Shipping form")
        self.notebook.add(self.payment_tab,text="payment")
        self.notebook.add(self.upload_recipt_tab,text="upload recipt")
        self.notebook.add(self.neraby_pharmacy_tab,text="nearby_pharamacy")
        self.notebook.add(self.doctors_tab,text="doctors")
        self.notebook.add(self.orders_tab,text="orders")
        self.notebook.add(self.donate_tab,text="Donate")
        self.notebook.add(self.feed_back_tab,text="feedback")
        self.notebook.add(self.services_tab,text="services")
        self.notebook.add(self.offers_tab,text="offers")
        self.notebook.add(self.username_tab,text="user name")
        self.notebook.add(self.alldrugs_tab,text="all drugs")
        self.notebook.add(self.add_pharmacy_form_tab,text="join now pharmacy")
        self.notebook.add(self.username_tab2,text="user name2")
        self.notebook.add(self.username_tab3,text="user name3")
        self.notebook.add(self.doante_pay,text="doante pay")
        self.notebook.add(self.fitness_store_tab,text="fitness store")
        self.notebook.add(self.admin_tab,text="admin")
        self.notebook.add(self.admin_addpharmacy_form,text="admin add_pharmacy")
        self.notebook.add(self.admin_doctor_form,text="admin doctor_form")
        self.notebook.add(self.add_offers,text="add offers form")
        self.notebook.add(self.baby_care_tab,text="baby care")
        self.notebook.add(self.skin_care_tab,text="Skin care")
        self.notebook.add(self.remove_pharmacy_tab,text="Remove_pharmacy")
        self.notebook.add(self.remove_doctors_tab,text="Remove_doctors")
                
        style = ttk.Style()
        style.layout("TNotebook.Tab",[])

    def main(self):

        def run_cart():
            func_show_item()

        def refresh_total():
            total_refresh()

        def my_order_run():
            my_order_func()

        def refresh_remove_pharmacy():
            remove_refresh()

        def refresh_remove_doc():
            remove_doc_refresh()


        
        user_table,sales_table = admin_pannel(self.admin_tab,self.notebook,self.resource_path,self.home_tab,self.add_new_items,self.admin_addpharmacy_form,
                                              self.admin_doctor_form,self.add_offers,self.login_tab,self.remove_doctors_tab,self.remove_pharmacy_tab)
        
        #log in tab 
        state = login_tab(self.login_tab,self.signin_tab,self.lobby_tab,self.notebook,self.resource_path,self.admin_tab)

        #sign in tab
        user_details=signin_tab(self.signin_tab,self.login_tab,self.home_tab,self.notebook,self.resource_path,self.pharmaciet_tab,self.doctor_tab,self.username_tab3)

        #home_tab
        home_tab(self.home_tab,self.signin_tab,self.home_tab,self.login_tab,self.notebook,self.resource_path,self.lobby_tab)

        pharmacient_details = pharmacient_form(self.pharmaciet_tab,self.login_tab,self.home_tab,self.notebook,self.resource_path,self.signin_tab,self.doctor_tab,self.add_pharmacy_form_tab)

        restart_doctors = Doctors(self.doctors_tab,self.notebook,self.resource_path,self.lobby_tab,self.cart_tab,self.epharmacy_tab,run_cart,self.orders_tab,self.offers_tab,self.services_tab)
        
        details = doctor_form(self.doctor_tab,self.login_tab,self.home_tab,self.notebook,self.resource_path,self.signin_tab,self.pharmaciet_tab,self.username_tab)
    

        epharmacy(self.epharmacy_tab,self.login_tab,self.signin_tab,self.notebook,self.lobby_tab,
                  self.pharm_easy_tab,self.resource_path,self.medi_cap_tab,self.cart_tab,run_cart,self.offers_tab,self.orders_tab,self.fitness_store_tab,self.baby_care_tab,self.skin_care_tab)

         
        bucket_pharmeasy,restart_pharmeasy=pharm_easy(self.pharm_easy_tab,self.login_tab,self.signin_tab,self.notebook,
                                                      self.lobby_tab,self.epharmacy_tab,self.cart_tab,self.resource_path,run_cart,
                                                      self.orders_tab,self.offers_tab)

        
        bucket_medicap,restart_medicap=medicap(self.medi_cap_tab,self.notebook,self.lobby_tab,self.epharmacy_tab,self.cart_tab,self.resource_path,bucket_pharmeasy,
                                               run_cart,self.orders_tab,self.offers_tab,self.signin_tab)

        bucket_fitness,restart_fitness=fitness_store(self.fitness_store_tab,self.notebook,self.lobby_tab,self.epharmacy_tab,self.cart_tab,self.resource_path,bucket_pharmeasy,run_cart,self.orders_tab,self.offers_tab,
                                                            self.signin_tab)
        
        bucket_skin_care,restart_skin_care=skincare_shop(self.skin_care_tab,self.notebook,self.lobby_tab,self.epharmacy_tab,self.cart_tab,self.resource_path,bucket_pharmeasy,run_cart,self.orders_tab,self.offers_tab,
                                                            self.signin_tab)
        
        bucket_baby_care,restart_baby_care=baby_care_store(self.baby_care_tab,self.notebook,self.lobby_tab,self.epharmacy_tab,self.cart_tab,self.resource_path,bucket_pharmeasy,run_cart,self.orders_tab,self.offers_tab,
                                                            self.signin_tab)
        
        all_drugs_bucket,restart_alldrugs=all_drugs_tab(self.alldrugs_tab,self.notebook,self.lobby_tab,self.epharmacy_tab,self.cart_tab,self.resource_path,
                      run_cart,self.orders_tab,self.offers_tab,bucket_pharmeasy,self.services_tab)

        offer_bucket,restart_bucket=show_offer(self.offers_tab,self.notebook,self.lobby_tab,self.epharmacy_tab,self.cart_tab,self.resource_path,run_cart,self.orders_tab,bucket_pharmeasy)
        
        func_show_item,total=picked_items(self.cart_tab,self.login_tab,self.signin_tab,self.notebook,self.lobby_tab,
                                          self.epharmacy_tab,bucket_pharmeasy,bucket_medicap,refresh_total,
                                          self.shipping_form_tab,self.resource_path,offer_bucket,all_drugs_bucket,self.offers_tab,
                                          self.orders_tab,bucket_fitness,bucket_baby_care,bucket_skin_care,state,self.cart_signin_tab)

        lobby(self.lobby_tab,self.notebook,self.epharmacy_tab,self.resource_path,self.cart_tab,
              self.orders_tab,self.services_tab,self.offers_tab,bucket_pharmeasy,self.fitness_store_tab,self.medi_cap_tab,self.pharm_easy_tab,self.skin_care_tab,func_show_item,self.login_tab)


        add_new_items(self.add_new_items,self.lobby_tab,self.notebook,self.resource_path,self.admin_tab,self.pharm_easy_tab,self.fitness_store_tab,
                      self.medi_cap_tab,self.baby_care_tab,self.skin_care_tab,restart_pharmeasy,restart_medicap,restart_fitness,restart_baby_care,restart_skin_care,restart_alldrugs)
        
        cart_login_tab(self.cart_signin_tab,self.signin_tab,self.notebook,self.resource_path,state,self.cart_tab,self.shipping_form_tab,refresh_total)

        total_refresh,checkouted_items=shipping_form(self.shipping_form_tab,self.notebook,self.resource_path,self.cart_tab,total,self.payment_tab,self.lobby_tab)
        
        payment_task(self.payment_tab,self.shipping_form_tab,self.lobby_tab,self.notebook,self.resource_path,my_order_run,self.orders_tab,checkouted_items,sales_table)

        upload_recipt(self.upload_recipt_tab,self.services_tab,self.notebook,self.resource_path,self.services_tab)

        restart_nearby= nearby_stores(self.neraby_pharmacy_tab,self.notebook,self.resource_path,self.lobby_tab,self.cart_tab,self.epharmacy_tab,run_cart,self.orders_tab,
                                      self.offers_tab,self.services_tab)

        my_order_func=my_oreder(self.orders_tab,self.notebook,self.resource_path,self.lobby_tab,self.cart_tab,checkouted_items,self.epharmacy_tab,self.offers_tab)

        donate(self.donate_tab,self.notebook,self.resource_path,self.lobby_tab,self.cart_tab,self.epharmacy_tab,run_cart,self.doante_pay,self.orders_tab,self.offers_tab,self.services_tab)        

        reviwe(self.feed_back_tab,self.notebook,self.resource_path,self.lobby_tab,run_cart,self.cart_tab,self.orders_tab,self.epharmacy_tab,self.offers_tab,self.services_tab)

        services(self.services_tab,self.notebook,self.resource_path,self.upload_recipt_tab,self.neraby_pharmacy_tab,self.doctors_tab,
                 self.orders_tab,self.donate_tab,self.feed_back_tab,self.lobby_tab,self.alldrugs_tab)

        create_username(self.username_tab,self.doctors_tab,self.doctor_tab,self.notebook,restart_doctors,details,user_table,refresh_remove_doc,state)

        details_place = add_pharmacy_frm(self.add_pharmacy_form_tab,self.home_tab,self.notebook,self.resource_path,self.pharmaciet_tab,self.username_tab2)
               
        create_username2(self.username_tab2,self.neraby_pharmacy_tab,self.pharmaciet_tab,self.notebook,restart_nearby,details_place,pharmacient_details,user_table,refresh_remove_pharmacy,state)

        create_username3(self.username_tab3,self.lobby_tab,self.signin_tab,self.notebook,user_details,user_table,state)

        payment_task_donate(self.doante_pay,self.lobby_tab,self.notebook,self.resource_path,self.donate_tab)

        admin_pharmacy_frm(self.admin_addpharmacy_form,self.notebook,self.resource_path,restart_nearby,self.neraby_pharmacy_tab,self.admin_tab,refresh_remove_pharmacy)

        admin_doctor_form(self.admin_doctor_form,self.notebook,self.resource_path,restart_doctors,self.doctors_tab,self.admin_tab,refresh_remove_doc,user_table)

        add_offers_form(self.add_offers,self.notebook,self.resource_path,restart_bucket,self.offers_tab,self.admin_tab)

        remove_refresh = remove_pharmacy_tab(self.remove_pharmacy_tab,self.notebook,self.resource_path,self.admin_tab,restart_nearby)

        remove_doc_refresh = remove_doc(self.remove_doctors_tab,self.notebook,self.resource_path,self.admin_tab,restart_doctors,user_table)

        
        
if __name__ == "__main__":
    window=ctk.CTk()
    app=Pharmacy(window)
    app.main()

    
    app.window.mainloop()
