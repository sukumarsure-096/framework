import sys
sys.path.append(r'C:\Users\suren\Desktop\mysoft\python\opym5\framework\data')
sys.path.append(r'C:\Users\suren\Desktop\mysoft\python\opym5\framework\pom')
sys.path.append(r'C:\Users\suren\Desktop\mysoft\python\opym5\framework')
from config import *
from data.basefixture import *
from data.excellib import DataRead
from pom.Desktop_Page import Desktop
from pom.Login_page import Login
from pom.Billing_Page import BillingPage
import pytest
dr = DataRead()

headers,value = dr.read_data(testdata_file,e2e_tc_page)

class TestE2E(dinit):

    @pytest.mark.parametrize(headers,value)
    def test_e2e(self,testcase,email,password,countrycode,statecode,zipcode):
        ObjLogin = Login(self.d)
        ObjLogin.click_loginlink()
        ObjLogin.enter_mail(email)
        ObjLogin.enter_pwd(password)
        ObjLogin.click_login_button()
        
        ObjDesktop = Desktop(self.d)
        ObjDesktop.MouseTOComputer()
        ObjDesktop.ClickOnDesktop()
        ObjDesktop.ClickOnImage()
        ObjDesktop.ClickRadio1()
        ObjDesktop.ClickRadio2()
        ObjDesktop.ClickRadio3()
        ObjDesktop.ClickRadio4()
        ObjDesktop.AddToCart()
        ObjDesktop.ClickShoppingCart()

        ObjBilling = BillingPage(self.d)
        ObjBilling.SelectCountry(countrycode)
        ObjBilling.SelectState(statecode)
        ObjBilling.EnterZipcode(zipcode)
        ObjBilling.TermAndservices()
        ObjBilling.Billing()
        ObjBilling.ShippingAddress()
        ObjBilling.ShippingMethod()
        ObjBilling.PaymentMethod()
        ObjBilling.PaymentInfo()

        ObjLogin.clickLogout()



