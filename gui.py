'''#For GUI
from tkinter import *
import tkinter.colorchooser
import tkinter as tk
import tkinter.scrolledtext
root=Tk()
root.title("Codemy.com- Simple Button Animation")
root.geometry("400x300")
#tkinter.colorchooser.askcolor()
text_area=tk.scrolledtext.ScrolledText(root,width=40,height=10,font = ("Times New Roman",15))
text_area.grid(column = 2 , row= 2, pady = 10, padx = 10)
text_area.insert(tk.INSERT,
"""\
This is a scrolledtext widget to make tkinter text read only.
Hi
Geeks !!!
Geeks !!!
Geeks !!! 
Geeks !!!
Geeks !!!
Geeks !!!
Geeks !!!
""")


def expand():
    pass
#Creating a button animation
my_button=Button(root,text="Click Me!",command=expand,font=("Helvetica",24),fg="red")
my_button.pack()

canvas=tk.Canvas(root,width=300,height=300)
canvas.create_window(150,150,window=my_button)
root.mainloop()'''

'''
from tkinter import *
  
root = Tk()
root.geometry("300x300")
root.title(" Q&A ")
  
def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    if(INPUT == "120"):
        Output.insert(END, 'Correct')
    else:
        Output.insert(END, "Wrong answer")
      
l = Label(text = "What is 24 * 5 ? ")
inputtxt = Text(root, height = 10,
                width = 25,
                bg = "light yellow")
  
Output = Text(root, height = 5, 
              width = 25, 
              bg = "light cyan")
  
Display = Button(root, height = 2,
                 width = 20, 
                 text ="Show",
                 command = lambda:Take_input())
  
l.pack()
inputtxt.pack()
Display.pack()
Output.pack()
  
mainloop()'''

import tkinter as tk
import WCSC
import man_page
from tkinter import messagebox

def take_input():
    URL=output_url.get("1.0","end-1c")
    depth=int(depth_output.get("1.0","end-1c"))
    print("input=",URL)
    ss=ss_output.get("1.0","end-1c")
    print("keywords for ss",ss)
    keywords_subdomains=subdomains_output.get("1.0","end-1c")
    print("Keywords of subdomains",keywords_subdomains)
    i=images_check.get()
    l=links_check.get()
    h=header_check.get()
    print("i=",i,"l=",l,"h=",h)
    WCSC.WCSC_start(URL,depth,ss,keywords_subdomains,int(i),int(l),int(h))






root = tk.Tk()
root.iconbitmap("logo_icon.ico")
root.title("WCSC")
root.maxsize(500,500)
root.geometry("500x500")
url_label = tk.Label(root,text="URl of website:",width=25,height=1,font=("Itim"))
ss_label=tk.Label(root,text="Keywords for the screenshots:",width=25,font=("Itim"))
subdomains_label = tk.Label(root,text="Keywords for subdomains",width=25,height=1,font=("Itim"))
depth_label = tk.Label(root,text="Depth:",width=25,height=1,font=("Itim"))

depth_output=tk.Text(root,height=1,width=37,bg="light cyan",font=("Itim"))
output_url = tk.Text(root,height=1,width=37,bg="light cyan",font=("Itim"))
ss_output=tk.Text(root,height=1,width=37,bg="light cyan")
subdomains_output=tk.Text(root,height=1,width=37,bg="light cyan")
button=tk.Button(root,height=1,width=10,text="Go!",command=lambda:take_input())
button_help=tk.Button(root,height=1,width=10,text="Help",command=lambda:man_page.man_page_start())
#check_button:images,header,links,
images_check = tk.IntVar() 
links_check = tk.IntVar() 
header_check = tk.IntVar() 

Button1 = tk.Checkbutton(root, text = "images", 
                      variable = images_check,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10)
Button2 = tk.Checkbutton(root, text = "links", 
                      variable = links_check,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10)
Button3 = tk.Checkbutton(root, text = "header", 
                      variable = header_check,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10)
 
canvas=tk.Canvas(root,width=400,height=300)
img=tk.PhotoImage(file=r"C:\Users\HP\Desktop\WSCS\Web-Crawler-main\logo.png")
canvas.create_image(250,250,image=img)

canvas.place(x=0,y=-150)
url_label.place(x=0,y=240)
output_url.place(x=230,y=240)
depth_label.place(x=0,y=260)
depth_output.place(x=230,y=260)
ss_label.place(x=0,y=280)
ss_output.place(x=230,y=280)
subdomains_label.place(x=0,y=300)
subdomains_output.place(x=230,y=300)

button.place(x=100,y=400)
button_help.place(x=300,y=400)
Button1.place(x=50,y=340)
Button2.place(x=180,y=340)
Button3.place(x=310,y=340)


root.mainloop()

    
#To add: loading widget
