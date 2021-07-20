import sys

from openpyxl import workbook
sys.path.append(r'C:\Users\suren\Desktop\mysoft\python\opym5\framework')
from config import *
from xlrd import *
import openpyxl

class DataRead():

    #   READ LOCATORS
    # def read_locators(self,filename,sheet_name):
    #     workbook = open_workbook(filename)
    #     sheetname = workbook.sheet_by_name(sheet_name)
    #     row = sheetname.get_rows()
    #     head = next(row)
    #     d = {j[0].value : (sheetname.row_values(index,start_colx=1))  for index,j in enumerate(row,start=1)}
    #     return d ,d.keys()

    def read_locators(self,filename,sheet_name):
        workbook = openpyxl.load_workbook(filename)
        sheetname = workbook.get_sheet_by_name(sheet_name)
        rows= sheetname.rows
        headers = next(rows)
        d = { j[0].value : (j[1].value , j[2].value) for j in rows }
        return d,d.keys

    #   READ DATA
    # def read_data(self,filename,sheet_name):
    #     workbook = open_workbook(filename)
    #     sheetname = workbook.sheet_by_name(sheet_name)
    #     row = sheetname.get_rows()
    #     head = next(row)
    #     headers = [j.value for j in head]
    #     headers = ','.join(headers)
    #     d = [sheetname.row_values(index)  for index,j in enumerate(row,start=1)]
    #     return headers,d

    def read_data(self,filename,sheet_name):
        workbook = openpyxl.load_workbook(filename)
        sheetname = workbook.get_sheet_by_name(sheet_name)
        l = [j for j in sheetname.values]
        headers = ','.join(l.pop(0))
        return headers , l