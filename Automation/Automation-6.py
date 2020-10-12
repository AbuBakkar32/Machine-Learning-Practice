from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import openpyxl
from Automation import XLUtils

driver = webdriver.Chrome('G:/Machine Learning Practice/Automation/driver/chromedriver.exe')
driver.maximize_window()

path = 'data.xlsx'
row = XLUtils.getRowCount(path, 'empsheet')
col = XLUtils.getColumnCount(path, 'empsheet')
print(row, col)

for r in range(1, row+1):
    for c in range(1, col+1):
        data = XLUtils.readData(path, 'empsheet', r, c)
        print(data, end='                              ')
    print('')



