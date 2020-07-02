from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.uix.dropdown import DropDown 
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
import json, glob
from datetime import datetime
from pathlib import Path
import random

Builder.load_file('design.kv')


class LoginScreen(Screen):
    def sign_up(self):  
        self.manager.transition.direction = 'right'
        self.manager.current = "sign_up_screen"
    
    def login(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        uname = uname.strip()
        pword = pword.strip()
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = 'login_screeen_success'
        else:
            anim = Animation(color = (0.6, 0.7, 0.1, 1))
            anim.start(self.ids.login_wrong)
            self.ids.login_wrong.text = "Wrong username or password!"

class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        if uname == "" or pword == "":
            print("Please enter proper username and password. Blank is not allowed")
        else:
            uname = uname.strip()
            pword = pword.strip()
            users[uname] = {'username': uname, 'password': pword,
            'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        
            with open("users.json", 'w') as file:
                json.dump(users, file)
            
            self.manager.current = "sign_up_screen_success"

class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

class LoginScreenSuccess(Screen):
    
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"
    
    def add_medicines(self):
        self.manager.transition.direction = "right"
        self.manager.current = "add_medicines"
    
    def add_member_to_medicines(self):
        self.manager.transition.direction = "right"
        self.manager.current = "add_member_to_medicines"
    
    def view_member_medicines(self):
        self.manager.transition.direction = "right"
        self.manager.current = "view_member_medicines"

class AddMedicines(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"
    
    def back(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screeen_success"
    
    def add_medicine(self,med_name,med_weight, med_type): 
        print("med_name", med_name)      
        with open("medicines.json") as file:
            medicines = json.load(file)
            print(medicines, "medicies")
        medicines[med_name] = {'medicine_name': med_name, 'medicine_weight': med_weight,
        'med_type':med_type,'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        print ("medicines[med_name]",medicines[med_name])
        with open("medicines.json", 'w') as file:
            json.dump(medicines, file)

class MapMemberMedicines(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"
    
    def back(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screeen_success"
    
    def add_member_to_medicine(self,member_name,member_age):
        with open("member_medicine.json") as file:
            member_medicine = json.load(file)
        member_medicine[member_name] = {'member_name': member_name, 'member_age': member_age,
        'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        print ("member_medicine[member_name]",member_medicine[member_name])
        with open("member_medicine.json", 'w') as file:
            json.dump(member_medicine, file)
    
    def back(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screeen_success"

class ViewMemberMedicines(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"
    def back(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screeen_success"

    def view_member_medicine(self):
        names = []
        member_name = []
        patient_name = []
        patient_age = []
        with open("member_medicine.json") as file:
            member_medicine = json.load(file)
            for members in member_medicine.items():
                member_name.append(members[0])
                print (member_name, "members")
                for k,v in members[1].items():
                    if k == "member_name":
                        patient_name.append(v)
                    elif k == "member_age":
                        patient_age.append(v)
                
        return member_name, patient_name, patient_age
    
    def get_member_name(self):
        names = []
        member_name = []
        with open("member_medicine.json") as file:
            member_medicine = json.load(file)
            for members in member_medicine.items():
                member_name.append(members[0])
                print (member_name, "members")
        return members

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()