import sys
sys.path.append(r'C:\Users\suren\Desktop\mysoft\python\opym5\framework\data')
sys.path.append(r'C:\Users\suren\Desktop\mysoft\python\opym5\framework')
from data.excellib import DataRead
from data.basefixture import *
from data.selenium_wrapper import SeleniumWrapper
from config import *
from time import sleep 
sw = SeleniumWrapper()
dr = DataRead()
key ,value =  dr.read_locators(register_file,billing_locator_page)

class BillingPage():
    def __init__(self,d) :
        self.d = d

    def SelectCountry(self,value):
        element = key['select_country']
        sw.SelectItem(self.d,element,value)
        sleep(3)
    def SelectState(self,value):
        element = key['select_state']
        sw.SelectItem(self.d,element,value)
        sleep(3)
    def EnterZipcode(self,value):
        element = key['zipcode']
        sw.Enter(self.d,element,value)
        sleep(3)
    def TermAndservices(self):
        element = key['term_service']
        sw.Click(self.d,element)
        sleep(3)
        element = key['checkout'] #click on check out page
        sw.Click(self.d,element)
        sleep(3)
    def Billing(self):
        element = key['billing_Adress_click']
        sw.Click(self.d,element)
        sleep(3)
    def ShippingAddress(self):
        element = key['Shipping_Adress_click']
        sw.Click(self.d,element)
        sleep(3)
    def ShippingMethod(self):
        element = key['Shipping_method_ground']
        sw.Click(self.d,element)
        sleep(3)
        element = key['Shipping_method_contine_click']
        sw.Click(self.d,element)

    def PaymentMethod(self):
        element = key['pay_mode']
        sw.Click(self.d,element)
        sleep(3)
        element = key['pay_continue']
        sw.Click(self.d,element)

    def PaymentInfo(self):
        element = key['pay_info_continue']
        sw.Click(self.d,element)

        element = key['pay_confirm']
        sw.Click(self.d,element)
        sleep(3)
        element = key['pay_confirm_continue']
        sw.Click(self.d,element)

        element = key['click_on_add_to_cart']
        sw.Click(self.d,element)
        sleep(3)



        
        