'''Selenium'''
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import itertools
from time import sleep

                                  
def urll(website,urls,strng,c):
    driver=webdriver.Chrome(executable_path=r"D:\Dhanbad\chromedriver.exe")
    
    for Url,name  in zip(urls,strng): #use itertools.izip()
        try:
            print("in try, yipeeeeee",c,name,Url)
            if("http" in Url or "https" in Url or ".com" in Url):
                driver.get(Url)
            elif("/" in Url):
                driver.get(website + Url)
            else:
                driver.get(website + "/" + Url)
            driver.maximize_window()
            sleep(2)
            driver.get_screenshot_as_file(r"C:\\Users\\HP\\Desktop\\Alphx project\\asdas\\" + c + "\\Screen-Shots\\" + name +".png")
        except:
            continue
    driver.close()
            


