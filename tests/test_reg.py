import pytest
import sys
sys.path.append(r'C:\Users\suren\Desktop\mysoft\python\opym5\framework')
sys.path.append(r'C:\Users\suren\Desktop\mysoft\python\opym5\framework\pom')
sys.path.append(r'C:\Users\suren\Desktop\mysoft\python\opym5\framework\utilities')
from data.basefixture import *
from pom.Login_page import Login 
from data.excellib import DataRead
from utilities.customLogger import LogGen
from config import *

dr = DataRead()
headers,data = dr.read_data(testdata_file,login_testcase_name)

class TestLogin(dinit):
    logger = LogGen.loggen()

    @pytest.mark.parametrize(headers,data)
    def test_login(self,testcase,email,pwd,status):
        self.logger.info('********************************')
        r = Login(self.d)
        r.click_loginlink()
        r.enter_mail(email)
        r.enter_pwd(pwd)
        r.click_login_button()
        r.clickLogout()
        
