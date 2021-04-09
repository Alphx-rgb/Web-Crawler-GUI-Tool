'''Selenium'''
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import itertools
from time import sleep
import keyboard
k=1                                  
def urll(website,urls,strng,c):
    global k
    
    driver=webdriver.Chrome(executable_path=r"D:\Dhanbad\chromedriver.exe")
    
    for Url,name  in zip(urls,strng): #use itertools.izip()
        if(name!=None):
            print(k,".",name + ".....")
        else:
            name = Url
            print(k,".",name , ".....")
        if(keyboard.is_pressed('q')):
            break
        if("http" in Url or "https" in Url or ".com" in Url):
            driver.get(Url)
        elif("/" in Url):
            driver.get(website + Url)
        else:
            driver.get(website + "/" + Url)
        driver.maximize_window()
        sleep(2)
        if("." not in name):
            driver.save_screenshot(os.getcwd() + "\\Screen-Shots\\" + name + str(k) +"_ss.png")
        else:
            driver.save_screenshot(os.getcwd()+"\\Screen-Shots\\" + (name.split("."))[1] + "_" + str(k) +"_ss.png")
        print("Next...")
        k+=1
    driver.close()
            
