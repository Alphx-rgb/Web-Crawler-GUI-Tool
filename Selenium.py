'''Selenium'''
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import itertools
from time import sleep
import keyboard
from termcolor import cprint
k=1                                  
def urll(website,urls,strng,c,keywords_of_ss):
    global k
    
    urlss=[]
    strngss=[]
    driver=webdriver.Chrome(executable_path=r"D:\Dhanbad\chromedriver.exe")
    for element in keywords_of_ss:
        for element2,name in zip(urls,strng):
            try:
                if(element in element2):
                    urlss.append(element2)
                    strngss.append(name)
            except:
                pass

    for Url,name  in zip(urlss,strngss): #use itertools.izip()
        if(name!=None):
            cprint(k,"green",end="")
            print(".",end="")
            cprint(name.replace("\n","").strip(),"cyan",end="")
            print(".....")
        else:
            name = (((Url.strip()).split("."))[0]).replace("/"," ")
            cprint(k,"green",end="")
            print(".",end="")
            cprint(name,"cyan",end="")
            print(".....")
        if(keyboard.is_pressed('q')):
            break
        try:
            if("http" in Url or "https" in Url or ".com" in Url):
                driver.get(Url)
            elif("/" in Url):
                driver.get(website + Url)
            else:
                driver.get(website + "/" + Url)
            driver.maximize_window()
            sleep(2)
            if("." not in name):
                driver.save_screenshot(os.getcwd() + "\\Screen-Shots\\" + (name.replace("\n","").strip()).replace("/"," ") + str(k) +"_ss.png")
            else:
                driver.save_screenshot(os.getcwd()+"\\Screen-Shots\\" + ((name.split("."))[1]).strip() + "_" + str(k) +"_ss.png")
            print("Next...")
        except:
            pass
            
        k+=1
    driver.close()
 
