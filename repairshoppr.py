#Hello, Main goal for this project is simple. Create a inegration with Google Sheets that will automaticly 
#Open a bucket when a service is checked out. If bucket is already chosen then an error flag will pop up. 
#TODO Fix Line Numbers

#Begin Test Enviroment
from tkinter import *
from tkinter import ttk
from sheets import *
from tkinter import messagebox

def checkbucket():
    selction = bucket.get()
    buckets = openbuckets()
    if selction in buckets:
        closebucket(selction)
    else:
        messagebox.showerror(title = "Oops!", message = "Bucket is not open! Please Select another!")




root = Tk()                                                 #Lines 8-10 create a GUI to replicate Repairshoppr to the lowest form, in order to make an effective mock up
root.title("RepairShoppr [Mock-Up]")
root.geometry("600x400")

tabControl = ttk.Notebook(root)                             #Lines 12-15 create a tab that will mimic the first step of check in, in order to show the problem of putting more than one service in a bucket
tab = ttk.Frame(tabControl)
tabControl.add(tab, text = "Check-In")
tabControl.pack(expand = 1, fill = "both")

tab1 = ttk.Frame(tabControl)                                #Lines 17-19 create the  Check-out process, same thought process in order to remove human error on forgetting to de-select bucket
tabControl.add(tab1, text = "Check-Out")
tabControl.pack(expand = 1, fill = "both")

ticket = Label(tab, text = "Ticket Name").grid(row = 0, sticky = W)                                     #Lines 21-45 create the mock interface with some entries, not all are included since they are not nessesary for demonstration purposes
ticketr = Entry(tab, width = 50).grid(row = 1, sticky = W)

servicetype = Label(tab, text = "Ticket Issue").grid(row =2, sticky = W)
issue = StringVar()
issuetype = OptionMenu(tab, issue, "Basic Diagnostic","Streamlined Service","Simplified Service","Complete Cleanup","Hard Drive Check","Prepaid").grid(row = 3, sticky = W)

space =  Label(tab).grid(column = 1)

tech = Label(tab, text = "Technician").grid(row = 4, sticky = W)
technician = StringVar()
selectedtech  = OptionMenu(tab, technician, "Ben","Boris","Leo","Oscar","Zach").grid(row = 5, sticky = W)

pickup = Label(tab, text = "Authorized Pick Up").grid(row = 0, column = 2, sticky =  W)
authorized =  Entry(tab, width = 50).grid(row = 1, column = 2, sticky = W)

choice = IntVar()
bucketSelect = Label(tab, text = "Bucket").grid(row = 2, column = 2, sticky = W)
bucket = Entry(tab, width = 50)
bucket.grid(row = 3, column = 2, sticky = W)

datarelated = Label(tab, text = "Data Related Service").grid(row = 4, column =  2, sticky = W)
related = StringVar()
datadeath = OptionMenu(tab, related, "Yes","No").grid(row = 5, column = 2, sticky = W)

complete = Button(tab, text = "Continue to Intake Signiture --->", command = checkbucket).grid(row = 6, column = 2, sticky = W)
stop = Button(tab, text = "Quit", command = root.quit).grid(row  =  7, column = 2, sticky = W)


root.mainloop()