import requests
from tkinter import *
from bs4 import BeautifulSoup
import os
from tkinter import Entry


global urln
urln=""


def imagedownload(parsedhtml1, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    try:
        images = parsedhtml.find_all('img')
        for image in images:
            name = image['alt']
            link = image['src']
            with open(name.replace(' ', '-').replace('/', "")+'.jpeg', 'wb') as f:
                im = requests.get(link)
                f.write(im.content)
                mainlabel.configure(text='Writing: '+name)
                mainlabel.update()
    except:
        mainlabel.configure(text='Downloaded available images')
        mainlabel.update()


def tags(parsedhtml1):
    # print("List of all the h1, h2, h3 :")
    # for heading in parsedhtml.find_all(["h1", "h2", "h3"]):
    #    headlab = Label(frame,text=heading.name + ' ' + heading.text.strip())
    #    headlab.pack()
    mainlabel.configure(text="GETTING HEADINGS FROM THE FILE")
    mainlabel.update()
    for heading in parsedhtml.find_all(["h1","h2","h3"]):
        with open(fname+"(headings).txt", "a") as headfile:
            headfile.write(heading.name + ' ' + heading.text.strip()+"\n")
    mainlabel.configure(text="Headings Fetched sucessfully ")
    mainlabel.update()
   

def links(parsedhtml1):
    mainlabel.configure(text="Getting LINKS from the page")
    mainlabel.update()
    for a_href in parsedhtml.find_all("a", href=True):
        with open(fname+"(links).txt", "a") as linkfile:
            linkfile.write(a_href["href"]+"\n")
    mainlabel.configure(text="LINKS added to file sucesfully")
    mainlabel.update()
    # with open(fname+".txt", "w") as outfile:
        # for link in parsedhtml1.find_all('a'):
        #     a =(link.get('href'))
        #     # outfile.write(a.content)

        #     print((a))


    #    linklab= Label(frame, text=link.get('href'))
    #    linklab.pack()
    # outfile.close()
def geturl():
    try:
        mainlabel.configure(text="Fetching Resources From URL")
        mainlabel.update()
        urln = linkk.get()
        material = requests.get(urln)
        global parsedhtml
        parsedhtml = BeautifulSoup(material.content, 'html.parser')
        global fname
        fname = folder.get()
        mainlabel.configure(text="Fetched resources")
        mainlabel.update()
    except:
     mainlabel.configure(text="Please check your internet connection")
     mainlabel.update()

    



# gui
root = Tk()
# root.geometry("655x333")
frame = Frame(root, borderwidth=6, bg="grey", relief="sunken",width=400,height=200)
frame.pack_propagate(0)
frame.pack(side=LEFT, anchor="nw")


# input("paste url")  # the website to be scrapedlinkk = Entry(frame, borderwidth=5,)

linkk = Entry(frame, width=50,borderwidth=5)
linkk.insert(0, "Paste your url here.")
linkk.pack()


folder = Entry(frame, width=50,borderwidth=5)
folder.insert(0, "Enter the name of the destination file") # input("insertfolder name")
folder.pack()

urlb=Button(frame,text="search",command=geturl)
urlb.pack()



b1 = Button(frame, foreground='red',
            text="Download images", command=lambda:imagedownload(parsedhtml, fname))
b1.pack(side="left", padx=25)
b2 = Button(frame, foreground='red', text="Get headings",
            command=lambda: tags(parsedhtml))
b2.pack(side="left", padx=25)
b3 = Button(frame, foreground='red', text="Get links",
            command=lambda: links(parsedhtml))
b3.pack(side="left", padx=25)
display= StringVar()
display.set("")
mainlabel=Label(frame,text="",bg="grey")
mainlabel.place(x=100,y=150)
root.mainloop()
