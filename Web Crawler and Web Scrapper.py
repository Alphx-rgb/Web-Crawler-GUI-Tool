#PROJECT
import tldextract
from bs4 import BeautifulSoup
import os
import requests
import pyttsx3
engine=pyttsx3.init('sapi5')
engine.setProperty("voices",'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
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
    engine.say(f"You have entered {ext.domain} with depth search of {depth} ......")
    engine.runAndWait()
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


def link(lst,tag,attribute,file_name):  
    global c
    global url
    a=list()
    a=[]  
    if(lst != [] or lst == None):
        for element in lst:
            try:
                client1=requests.get(element)
                soup1=BeautifulSoup(client1.text)
                links = soup1.findAll(tag)
                for link in links:
                    a.append(link.get(attribute))
                    #if(tag=="a"):    #uncomment this for getting screenshots of links founded in depth2 search
                        #strngs.append(link.string)
            except:
                continue
        saving_files(a,file_name)
        #Selenium.urll(url,a,strngs,c)  #uncomment this for getting screenshots of links founded in depth2 search
        return(a)               
    else:
        links = soup.findAll(tag) 
        lst=[]      #to convert none type to empty list
        for link in links:
            lst.append(link.get(attribute))
            if(tag=="a"):
                strngs.append(link.string)
        if(tag=="a"):
            Selenium.urll(url,lst,strngs,c)
        creating_saving_files(lst,file_name)
        return(lst)






url=input("Enter the url:")
depth=int(input("Enter Depth:"))
start(url)
client=requests.get(url)
soup=BeautifulSoup(client.text)
lst=list()
lst1=list()
strngs=list() #to store "link.string" to name screenshots
l=0

engine.say("Collecting Headers.....")
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
engine.runAndWait()
try:
    os.mkdir(".\Screen-Shots")
except:
    pass
engine.say("Getting links,images and screenshots of the given website....Please Wait")
print("Getting links,images and screenshots....Please Wait")
engine.runAndWait()
while(depth!=l):
    l+=1
    lst=link(lst,"a","href","links")
    lst1=link(lst1,"img","src","images")
print("Collecting Emails (if any) available on the website:")
engine.say("Collecting Emails")
engine.runAndWait()
email_address.mails(url)

engine.say("Work Completed")
engine.runAndWait()
print("Work Completed....")
