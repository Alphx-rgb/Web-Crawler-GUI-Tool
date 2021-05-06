#PROJECT
import tldextract
from bs4 import BeautifulSoup
import os
import requests
import Selenium 
import email_address
import dynamic_websites
import sys
from termcolor import cprint
import man_page
import subdomain_suffix_finder
from tkinter import messagebox
#import gui
#####################################################################################################################################################################
c=""

def WCSC_start(url,depth,ss,keywords_subdomains,i,l,h):
    keywords_of_ss=ss.split(",")
    def start(url): 
        global c  #To make folder "ext.domain" and change current working directory to this folder
        ext=tldextract.extract(url)
        try:
            os.mkdir(ext.domain)
            os.chdir(ext.domain)
        except:
            os.chdir(ext.domain)
        c=ext.domain
    def folder_making(sr):
            try:
                os.mkdir(f".\{sr}")
                os.chdir(f".\{sr}")
            except:
                os.chdir(f".\{sr}")
    def creating_saving_files(lst,strng):
        folder_making(strng)
        f=open(f"{strng}_{l}.txt","a")
        for element in lst:
            if(element == None):
                continue
            elif("http" in element or "https" in element):
                f.write(element + "\n")
            else:
                f.write(url+element + "\n")
        f.close()
        os.chdir(".\..")
    def saving_files(lst,strng):
        os.chdir(f".\{strng}")
        f=open(f"{strng}_{l}.txt","a")
        #print(lst)
        for element in lst:
            #print(element)
            if(element == None):
                continue
            elif("http" in str(element) or "https" in str(element)):
                f.write(element + "\n")
            else:
                f.write(url+element + "\n")
        f.close()
        os.chdir(".\..")


    def link(lst,tag,attribute,file_name,url):  
        
        global c
        #global url

        a=list()
        a=[] 
        if(lst != [] and lst != None and tag != "img"):
            for element in lst:
                try:
                    client1=requests.get(element)
                    soup1=BeautifulSoup(client1.text)
                    links = soup1.findAll(tag)
                    for link in links:
                        if(link.get(attribute) not in a):
                            a.append(link.get(attribute))
                            if(tag=="a"):
                                strngs.append(link.string)
                except:
                    continue
            if(l):
                saving_files(a,file_name)
            if( keywords_of_ss != "" and keywords_of_ss != None):
                Selenium.urll(url,a,strngs,c,keywords_of_ss)
            return(a)               
        elif(l==1):
            links = soup.findAll(tag) 
            lst=[]      #to convert none type to empty list
            for link in links:
                if(link.get(attribute) not in lst):
                    lst.append(link.get(attribute))
                    if(tag=="a"):
                        strngs.append(link.string)
            if(tag=="a" and lst != None and lst != []  and keywords_of_ss != "" and keywords_of_ss != None):
                Selenium.urll(url,lst,strngs,c,keywords_of_ss)
            if(l):
                creating_saving_files(lst,file_name)
            return(lst)
    print(i,l,h)
    start(url)
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","Accept-Encoding": "gzip, deflate"}
    client=requests.get(url,headers=burp0_headers)
    soup=BeautifulSoup(client.text)
    lst=list()
    lst1=list()
    strngs=list() #to store "link.string" to name screenshots
    l=0
    if(h):
        cprint("Collecting Headers.....","yellow",attrs=["bold","blink"])
        try:
            os.mkdir(".\Headers")
            os.chdir(".\Headers")
        except:
            os.chdir(".\Headers")
        with open("Headers.txt","w") as f:
            f.write(str(client.headers))
        f.close()
        os.chdir(".\..")   

    try:
        os.mkdir(".\Screen-Shots")
    except:
        pass
    cprint("Getting links,images and screenshots of the given website....Please Wait","yellow",attrs=["reverse","blink"])
    while(depth!=l):
        l+=1
        lst=link(lst,"a","href","links",url)
        if(i):
            lst1=link(lst1,"img","src","images",url)





    cprint("Collecting Emails (if any) available on the website","yellow")
    email_address.mails(url)
    #print(os.getcwd()) #C:\Users\HP\Desktop\Alphx-Project\project-23thmarch\Web-Crawler-main\stackoverflow
    cprint("#######################","red")
    if(lst==[]):
        for z in range(1,depth+1):
            lst=dynamic_websites.get(url,lst,depth,"a","href",c,"links",z,l,keywords_of_ss)
            if(i):
                lst1=dynamic_websites.get(url,lst1,1,"img","src",c,"images",z,i,keywords_of_ss)
        
    print("Finished")
    messagebox.showinfo(title="Process",message="Process Cmpleted")
    
