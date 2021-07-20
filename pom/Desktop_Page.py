import sys
sys.path.append(r"C:\Users\suren\Desktop\mysoft\python\opym5\framework\data")
sys.path.append(r"C:\Users\suren\Desktop\mysoft\python\opym5\framework")
from data.basefixture import *
from data.excellib import DataRead
from data.selenium_wrapper import SeleniumWrapper
from config import *
from time import sleep
sw = SeleniumWrapper()
loc_read = DataRead()
key,value = loc_read.read_locators(register_file,desktop_locator_page)

class Desktop():
    def __init__(self,d) :
        self.d = d
    
    def MouseTOComputer(self):
        element = key['move_to_computers']
        sw.MouseAction(self.d,element)
        

    def ClickOnDesktop(self):
        element = key["click_on_desktop"]
        sw.Click(self.d,element)
        
    def ClickOnImage(self):
        element = key['click_on_image']
        sw.Click(self.d,element)
        
    def ClickRadio1(self):
        element = key['click_on_radio1']
        sw.Click(self.d,element)
        
    def ClickRadio2(self):
        element = key['click_on_radio2']
        sw.Click(self.d,element)
        
    def ClickRadio3(self):
        element = key['click_on_radio3']
        sw.Click(self.d,element)
        
    def ClickRadio4(self):
        element = key['click_on_radio4']
        sw.Click(self.d,element)
        

    def AddToCart(self):
        element = key['click_on_add_to_cart']
        sw.Click(self.d,element)
        
    def ClickShoppingCart(self):
        element = key['click_on_shoppingcart']
        sw.Click(self.d,element)
    
# ObjDesktop = Desktop(d)
# ObjDesktop.MouseTOComputer()
# ObjDesktop.ClickOnDesktop()
# ObjDesktop.ClickOnImage()
# ObjDesktop.ClickRadio1()
# ObjDesktop.ClickRadio2()
# ObjDesktop.ClickRadio3()
# ObjDesktop.ClickRadio4()
# ObjDesktop.AddToCart()
# ObjDesktop.ClickShoppingCart()

    
