import sys
sys.path.append(r'C:\Users\suren\Desktop\mysoft\python\opym5\framework\data')
from data.basefixture import *

class SeleniumWrapper():

    def Enter(self,d,element,value):
        loctype ,locvalue = element
        d.find_element(loctype,locvalue).clear()
        d.find_element(loctype,locvalue).send_keys(value)
    
    def Click(self,d,element):
        loctype ,locvalue = element
        clickelement = d.find_element(loctype,locvalue)
        if clickelement.is_enabled() and clickelement.is_displayed():
            clickelement.click()
    
    def PageMove(self,d,type):
        ac = ActionChains(d)
        if type.upper() == 'DOWN':
            ac.send_keys(Keys.PAGE_DOWN).perform()
        elif type.upper() == 'UP':
            ac.send_keys(Keys.PAGE_UP).perform()
        
    def SelectItem(self,d,element,text):
        loctype,locvalue = element
        s = Select(d.find_element(loctype,locvalue))
        if isinstance(text,str):
            s.select_by_visible_text(text)
        elif isinstance(text,int):
            s.select_by_index(text)
        else:
            s.select_by_value(text)     

    def MouseAction(self,d,element):
        ac = ActionChains(d)
        loctype,locvalue = element
        ele = d.find_element(loctype,locvalue)
        ac.move_to_element(ele).perform()

    def WindowHandle(self,d):
        handle = d.window_handles
        for j in handle[1:]:
            d.switch_to.window(j)
            d.close()
    
    def AlertOperations(self,d,type):
        if type.lower()=='accept':
            d.switch_to.alert.accept()
        elif type.lower() == 'dismiss':
            d.switch_to.alert.dismiss()
        else:
            d.switch_to.alert.send_keys(type)

    
