import os
import datetime

def run_command(command): #definning a function
       return(os.system(command))
def show_date() :
     return datetime.datetime.today()      
#run_command("date") #calling a function
#run_command("df -h")
today = show_date()
print(today)
