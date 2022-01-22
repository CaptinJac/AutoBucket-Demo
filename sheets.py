#Hello, This is the logic of the Sheets Interpretor, All logic if possible will be fit in to avoide any downtime with the code.
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('usr_secret.json', scope)
client = gspread.authorize(creds)

desktops = client.open('Mock Bucket List').sheet1
laptops = client.open('Mock Bucket List').get_worksheet(1)

def getallbuckets():
    y = 1 
    x = 1
    desktopbuckets = []
    laptopbuckets = []

    for z in range(len(desktops.row_values(1)) + 1):
        desktopbuckets.append({'bucket' : desktops.cell(x, y).value, 'available' : desktops.cell(x , y + 1).value})
        desktopbuckets.append({'bucket' : desktops.cell(x, y + 2).value,  'available' : desktops.cell(x, y + 3).value})
        x = x + 1
    
    x = 1
    y = 1   
    
    for z in range(len(laptops.row_values(1)) + 1):
        laptopbuckets.append({'bucket' : laptops.cell(x, y).value, 'available' : laptops.cell(x, y + 1).value})
        laptopbuckets.append({'bucket' : laptops.cell(x, y + 2).value, 'available' : laptops.cell(x, y + 3).value})
        x = x + 1

    return(sorted(desktopbuckets, key = lambda i: i['bucket']), sorted(laptopbuckets, key = lambda i:i['bucket']))

def openbuckets():
    buckets = getallbuckets()
    open = []
    for dict in buckets:
        for index in range(len(dict)):
            for key in dict[index]:
                if key == "available":
                    if dict[index].get(key) == "FALSE":
                        open.append(dict[index]['bucket'])
    return (open) 

def closedbuckets():
    buckets = getallbuckets()
    closed = []
    for dict in buckets:
        for index in range(len(dict)):
            for key in dict[index]:
                if key == "available":
                    if dict[index].get(key) == "TRUE":
                        open.append(dict[index]['bucket'])
    return (closed) 

def closebucket(input):
    x = 0
    if input in desktops.col_values(1):
        x = desktops.col_values(1).index(input) + 1
        desktops.update_cell(x, 2, "TRUE")
    elif input in desktops.col_values(3):
        x = desktops.col_values(3).index(input) + 1
        desktops.update_cell(x , 4, "TRUE")
    elif input in laptops.col_values(1):
        x = laptops.col_values(1).index(input) + 1
        laptops.update_cell(x, 2, "TRUE")
    elif input in laptops.col_values(3):
        x = laptops.col_values(3).index(input) + 1
        laptops.update_cell(x, 4, "TRUE")
   

    
def checker(input):
    buckets = openbuckets()
    if input not in buckets:
        return(False)

