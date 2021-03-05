from bs4 import BeautifulSoup 
import requests
import re

def mails(url):
    pattern=re.compile("[a-zA-A0-9\\.\\-+_]+@[ a-zA-A0-9\\.\\-+_]+.[a-zA-A0-9\\.\\-+_]+.[a-zA-A0-9\\.\\-+_]+.[a-zA-A0-9\\.\\-+_]")
    client=requests.get(url)
    matches=re.findall(pattern,client.text)
    f=open("mails.txt","w")
    for match in matches:
        f.write(match + "\n")
