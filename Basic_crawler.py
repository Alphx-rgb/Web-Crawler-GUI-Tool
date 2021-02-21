import tldextract
from bs4 import BeautifulSoup
import os
import requests
import pyttsx3
from urllib.parse import urljoin, urlparse  
engine=pyttsx3.init('sapi5')
engine.setProperty("voices",'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')


def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme) #urlparse() function parses a URL into six components, we just need to see if the netloc (domain name) and scheme (protocol) are there.

def headers_links_images(url):
    client=requests.get(url)
    soup = BeautifulSoup(client.text)

    def folder_making(sr):
        try:
            os.mkdir(f".\{sr}")
            os.chdir(f".\{sr}")
        except:
            os.chdir(f".\{sr}")
    def viewing_files(sr):
        ans=input(f"Want to view {sr}?")
        if(ans=='y' or ans == "yes" or ans=="Y" or ans == "Yes"):
            with open(f"{sr}.txt","r") as f:
                lst=(f.read()).split("https")
                for link in lst:
                    print("https" + link)




####################### COLLECTING LINKS ###########################
    print("Collecting links ....")
    engine.say("Collecting links ....")
    engine.runAndWait()
    folder_making("href_links")
    #print(os.getcwd())
    f=open("links.txt","w")
    links = soup.findAll("a")
    for link in links:
        if(link.string != None):
            if(("http" in link.get("href")) or "htps" in link.get("href")): 
                sr = str(link.get("href")) + "\t" + (link.string) +"\t"
                f.write(sr + "\n")
            else:
                sr= url + str(link.get("href")) + "\t" + (link.string) +"\t"
                f.write(sr + "\n")
        else:
            if(("http" in link.get("href")) or "htps" in link.get("href")):
                sr = str(link.get("href"))
                f.write(sr)
            else:
                sr = url +  str(link.get("href"))
                f.write(sr)
    f.close()
    viewing_files("links")
    os.chdir(".\..")
#######################      HEADERS  ###########################
    print("Collecting Headers ....")
    engine.say("Collecting Headers ....")
    engine.runAndWait()
    folder_making("Headers")
    f=open("Headers.txt","w")
    f.write(str(client.headers))
    f.close()
    viewing_files("Headers")
    os.chdir(".\..")
####################### COLLECTING IMAGES LINKS ###########################
    print("Collecting images...")
    engine.say("Collecting images .....")
    engine.runAndWait()
    folder_making("Images")
    f=open("images.txt","w")
    images= soup.findAll("img")
    for image in images:
        if(image.get("src") != None):
            f.write(image.get("src"))
        if(image.get("srcset" != None)):
            f.write(image.get("Srcset"))
    f.close()
    viewing_files("images")    
    os.chdir(".\..")
#################### Source-Code ##########################
   #print(client.text)
    #f=open("source_code.txt","w")
    #f.write(str(client.text))
    #f.close()
#################### ATTRIBUTES ##########################

def search(sr,url):
    client=requests.get(url)
    try:
        rsearches= soup.findAll("sr")
        for rsearch in rsearches:
            print(rsearch + '\n')
    except:
        print("Not found")
        engine.say("Not found, try again...")
        engine.runAndWait()










url=input("Enter the url:")
if(is_valid(url)):
    ext=tldextract.extract(url)
    engine.say(f"You have entered:{ext.domain}.{ext.suffix}")
    engine.runAndWait()
    headers_links_images(url)
    engine.say("Want to enter any attribute to search for in the source code ....")
    engine.runAndWait()
    if(input("y/n:") == "y"):
        atb=input("Enter attribute:")  #atb ==> attribute
        search(atb,url)
    else:
        print("Thank you")
        engine.say("Thank You")
        engine.runAndWait()



else:
    print("Invalid url")
    engine.say("Try again....")
    engine.runAndWait()


