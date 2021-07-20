import sys

from attr import s
sys.path.append(r'C:\Users\suren\Desktop\mysoft\python\opym5\framework')
from data.selenium_wrapper import *
from data.excellib import DataRead
from config import *
import random
obj = DataRead()
key,value = obj.read_locators(register_file,login_locator_name)

sw = SeleniumWrapper()

class Login():
    def __init__(self,d):
        self.d = d
    
    def click_loginlink(self):
        element =  key['txt_click_login']
        sw.Click(self.d,element)
    
    def enter_mail(self,value):
        element = key['txt_email']
        sw.Enter(self.d,element,value)

    def enter_pwd(self,value):
        element = key['txt_pwd']
        sw.Enter(self.d,element,value)

    def click_login_button(self):
        element = key['txt_login_btn']
        sw.Click(self.d,element)
        if 'Demo Web Shop' == self.d.title:
            pass
        else:
            ran = random.randint(1,100)
            shot = 'C:\\Users\\suren\\Desktop\\mysoft\\python\\opym5\\framework\\scrrenshot'+str(ran)+".png"
            self.d.save_screenshot(shot)

    
    def clickLogout(self):    
        element =  key['txt_logout_btn']
        sw.Click(self.d,element)
