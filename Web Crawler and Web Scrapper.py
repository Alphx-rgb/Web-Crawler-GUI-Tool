#PROJECT
import tldextract
from bs4 import BeautifulSoup
import os
import requests
import threading
import Selenium 
import email_address
####################################################################################################################################
c=""
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
    for element in lst:
        if(element == None):
            continue
        elif("http" in str(element) or "https" in str(element)):
            f.write(element + "\n")
        else:
            f.write(url+element + "\n")
    f.close()
    os.chdir(".\..")


def link(lst,tag,attribute,file_name):  
    global c
    global url
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
                        #if(tag=="a"):
                            #strngs.append(link.string)
            except:
                continue
        saving_files(a,file_name)
        #Selenium.urll(url,a,strngs,c)
        return(a)               
    elif(l==1):
        links = soup.findAll(tag) 
        lst=[]      #to convert none type to empty list
        for link in links:
            if(link.get(attribute) not in lst):
                lst.append(link.get(attribute))
                if(tag=="a"):
                    strngs.append(link.string)
        if(tag=="a"):
            Selenium.urll(url,lst,strngs,c)
        creating_saving_files(lst,file_name)
        return(lst)
    else:
        print("No %s found"%(file_name))



url=input("Enter the url(in form like http://www.google.com):")
depth=int(input("Enter Depth:"))
start(url)
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
client=requests.get(url,headers=burp0_headers)
soup=BeautifulSoup(client.text)
lst=list()
lst1=list()
strngs=list() #to store "link.string" to name screenshots
l=0

print("Collecting Headers.....")
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

print("Getting links,images and screenshots of the given website....Please Wait")

while(depth!=l):
    l+=1
    lst=link(lst,"a","href","links")
    lst1=link(lst1,"img","src","images")


print("Collecting Emails (if any) available on the website:")
email_address.mails(url)
print(os.getcwd())

