'''Selenium'''
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


                                  
def urll(url,strng):
    if(strng==""):
        return 0
    driver=webdriver.Chrome(executable_path=r"D:\Dhanbad\chromedriver.exe")
    print(url)
    driver.get(url)
    driver.maximize_window()
    driver.get_screenshot_as_file(r"C:\\Users\\HP\\Desktop\\Project_code\\projectt\\Screen-Shots\\" + strng +".png")
    driver.close()



