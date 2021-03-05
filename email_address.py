from bs4 import BeautifulSoup 
import requests
import re
url=input("Enter url:")
#pattern=re.compile( r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""")
#pattern=r"\w+.?\w+@\w+.\w+"


def mails(url):
    pattern=re.compile("[a-zA-A0-9\\.\\-+_]+@[ a-zA-A0-9\\.\\-+_]+.[a-zA-A0-9\\.\\-+_]+.[a-zA-A0-9\\.\\-+_]+.[a-zA-A0-9\\.\\-+_]")
    client=requests.get(url)
    matches=re.findall(pattern,client.text)
    f=open("mails.txt","w")
    for match in matches:
        f.write(match + "\n")
mails(url)