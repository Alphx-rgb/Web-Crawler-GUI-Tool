import tldextract
import requests
import os
from termcolor import cprint
#url = input("Enter the url:")
def suffix_subdomain(url):
    ext=tldextract.extract(url)
    #print(ext," exttttttttttttttttt")
    sub_domains=list()
    suffixes=list()
    cprint("Checking Subdomains.....","cyan",attrs=[ 'blink'])
    c=os.getcwd()
    os.chdir("./..")
    for i in range(1):  #change this to number of times you need to scan
        with open(f"subdomains{i}.txt","r") as f:
            for i in range(10): #change this to the number of words you want to scan
                subdomain=f.readline()
                urll = "https://" + subdomain[:-1] + "." +  ext.domain + "." + ext.suffix #[:-1] is because to remove "\n"
                try:
                    client=requests.get(urll)
                    if(client.status_code==200):
                        sub_domains.append(urll)
                        print(urll,"OK")
                    if(300<client.status_code<400):
                        sub_domains.append(client.url)
                        print("redireced link:",end="")
                        for response in (client.history):
                            print(response.url,end="")
                        print()    
                except:
                    pass
        f.close()
    ################saving in a file###############
    try:
        os.mkdir(c+"\\"+"Subdomains_founded")
        os.chdir(c+"\\"+"Subdomains_founded")
    except:
        os.chdir(c+"\\" + "Subdomains_founded")
    
    with open("subdomains.txt","w") as f:
        for item in sub_domains:
            f.write(item + "\n")
    f.close()
    os.chdir(".\..\..")  #back to main directory
    ###################################################
    #######CHECKING SUFFIXES ##################
    cprint("Checkign Suffixes.....","red",attrs=[ 'blink'])
    print(os.getcwd())
    with open("suffixes.txt","r") as f:
        for i in range(10):
                suffix=f.readline()
                urll = "https://" + ext.subdomain + "." + ext.domain + "." + suffix[:-1] #[:-1] is because to remove "\n"
                #print(suffix[:-1])
                #print(urll)
                try:
                    client=requests.get(urll)
                    #print(client.status_code)
                    if(client.status_code==200):
                        suffixes.append(urll)
                        print(urll,"OK")
                except:
                    pass        
    try:
        os.mkdir(c+"\\" + "Suffix_founded")
        os.chdir(c+"\\" + "Suffix_founded")
    except:
        os.chdir(c+"\\" + "suffix_founded")
    with open("links_with_changed_suffix.txt","w") as f:
        for item in suffixes:
            f.write(item + "\n")
    f.close()
    os.chdir(".\..") #back to main directory
    print("Final directory at the end of sd and sf = " +  " " + os.getcwd())
    #############################################################################
    