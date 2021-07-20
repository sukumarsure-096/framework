import sys
sys.path.append(r'C:\Users\suren\Desktop\mysoft\python\opym5\framework')
sys.path.append(r'C:\Users\suren\Desktop\mysoft\python\opym5\framework\data')
from config import *
from data.selenium_wrapper import SeleniumWrapper
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
d = webdriver.Chrome(executable_path=path)
d.get('http://demowebshop.tricentis.com')
d.implicitly_wait(60)
d.maximize_window()
from time import sleep
sw = SeleniumWrapper()

def efg():
    
    # MOUSE MOVE TO COMPUTERS
    
        
    sw.MouseAction(d,("xpath",'//a[contains(text(),"Computers")]'))
    # CLICK ON DESKTOP
    sw.Click(d,("xpath","//a[contains(text(),'Desktops')]"))
    # CLICK ON ITEM 
    # sw.Click(d,("xpath","(//img[@title='Show details for Build your own cheap computer'])[2]"))
    d.find_element_by_link_text('Simple Computer').click()
    # click on radio buttton
    sw.Click(d,('xpath',"(//ul[@class='option-list'])[1]/li[1]"))
    # click on radio buttton
    sw.Click(d,('xpath','(//ul[@class="option-list"])[2]/li[3]'))
    # click on radio buttton
    sw.Click(d,('xpath','(//ul[@class="option-list"])[3]/li[2]'))
    # click on radio buttton
    sw.Click(d,('xpath','(//ul[@class="option-list"])[4]/li[2]'))
    # CLEAR QUANTITY
    d.find_element_by_id('addtocart_72_EnteredQuantity').clear()
    # ENTER NEW QUANTITY
    sw.Enter(d,("id",'addtocart_72_EnteredQuantity'),'2')
    # click on add to cart
    sw.Click(d,('id','add-to-cart-button-72'))
    # CLICK ON SHOPPING CART
    # sw.Click(d,('By.LINK_TEXT','Shopping cart'))
    d.find_element_by_link_text("Shopping cart").click()
    # SELECT COUNTRY
    sw.SelectItem(d,('id','CountryId'),'American Samoa')
    #SELECT STATA
    sw.SelectItem(d,('id','StateProvinceId'),'Other (Non US)')
    # CLEAR ZIPCODE
    d.find_element_by_id('ZipPostalCode').clear()
    # ENTER ZIPCODE
    sw.Enter(d,('id',"ZipPostalCode"),'560031')
    # CLICK ON TERM AND SERVICES
    sw.Click(d,("id",'termsofservice'))
    # click on checkout
    sw.Click(d,('id','checkout'))
    # CLICK ON BILLING ADDRESS
    d.quit()
efg()
    
