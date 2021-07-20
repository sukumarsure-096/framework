from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from config import *
import pytest

class dinit():
    
    @pytest.fixture(autouse=True,scope= 'class')
    def Init(self,request):
        if browser.upper() == 'CHROME':
            d = webdriver.Chrome(executable_path=path)
        elif browser.lower() == 'chrome':
            d = webdriver.Chrome(executable_path=path)
        else:
            d = webdriver.Chrome(executable_path=path)
        request.cls.d = d
        d.maximize_window()
        d.implicitly_wait(60)
        d.get(url)

        yield

        d.quit()

