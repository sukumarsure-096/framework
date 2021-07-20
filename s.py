from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import random
# d = webdriver.Chrome(executable_path=r'C:\Users\suren\Downloads\chromedriver_win32 (1)\chromedriver.exe')
# d.maximize_window()

class CoffeVending():

    def milk(self):
        print('milk is better')
    
    def coffee(self):
        print('coffe is better')
    
class TeaVending():

    def milk(self):
        print('milk is better')
    
    def Tea(self):
        print('Tea is better')
    

c = CoffeVending()

def commoninter(item):
    try:
        item.milk()
        item.coffee()
        item.Tea()
    except Exception:
        print('something is fishy')
    

commoninter(c)
commoninter(TeaVending())











##d = webdriver.Chrome(executable_path=r'C:\Users\suren\Downloads\chromedriver_win32 (1)\chromedriver.exe')
##d.get('file:///C:/Users/suren/Desktop/mysoft/python/opym5/training/chrome/table.html')
##
### l = d.find_element_by_name('selenium')
##l = d.find_element_by_xpath("(//input[@name='download'])[4]")
##l.click()
##print(l.is_selected())
##sleep(5)
##d.quit()

# def locators():
#     wb = xlrd.open_workbook(r'C:\Users\suren\Desktop\mysoft\python\opym5\fw\register.xls')
#     worksheet = wb.sheet_by_name('login_web')
#     row = worksheet.get_rows()
#     head = next(row)
#     d = {j[0].value : (worksheet.row_values(index,start_colx=1))  for index,j in enumerate(row,start=1)}
#     return d ,d.keys()
##print(locators())
# def testdata():
#     l =[]
#     wb = xlrd.open_workbook(r'C:\Users\suren\Desktop\mysoft\python\opym5\fw\Testdata.xls')
#     worksheet = wb.sheet_by_name('Sheet1')
#     row = worksheet.get_rows()
#     head = next(row)
#     for index,j in enumerate(head,start=1):
#         if j[0].value == 'test_shopping':
#             headers = worksheet.row_values(index-1,start_colx = 2)
#             headers = [item for item in headers if item]
#             headers = ','.join(headers)
#             break
#     row = worksheet.get_rows()
#     for index,j in enumerate(row,start=1):
# ##        if j[0].value == 'test_shopping':
#         l.append(tuple(worksheet.row_values(index)))
#     return l,headers
# print(testdata())

# def read_data(testcase):
#     workbook = xlrd.open_workbook(r'C:\Users\suren\Desktop\mysoft\python\opym5\fw\Testdata.xls')
#     worksheet = workbook.sheet_by_name('Sheet1')
#     data = []
#     headers = None
#     rows = worksheet.get_rows()
#     for rowno, row in enumerate(rows):
#         if row[0].value == testcase:
#             headers = worksheet.row_values(rowno - 1, start_colx=2)
#             headers = [item for item in headers if item]
#             headers = ','.join(headers)
#             break

#     rows = worksheet.get_rows()  # Re-initialising iterator

#     for rowno, row in enumerate(rows):
#         if row[0].value == testcase:
#             # Get the row values of the existing row from column-1
#             temp_data = worksheet.row_values(rowno, start_colx=1)
#             temp_data = [item for item in temp_data if item]
#             # Append the list only if the execute column is "Yes"
#             if temp_data[0] == "Yes":
#                 data.append(tuple(temp_data))
#     return [headers, data]
# ##print(read_data('test_login'))
