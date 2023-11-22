import datetime
import os


def create_diary():
    name = input("Enter the name of the diary: ") 
    cwd = os.getcwd() 
    path = cwd + "/" + name 
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the diary failed")
    else:
        print("Successfully created the diary")
def open_diary():
    os.chdir(os.getcwd())     
    name = input("Name of the diary:  ") 
    cwd = os.getcwd() 
    path = cwd + "/" + name 
    os.chdir(path)
    entries = os.listdir() 
    print("Entries: " + str(len(entries)))
    for entry in entries:
        print(entry) 

def add_content():
    title = input("What's the title of your entry?  ")
    author=input("What's the name of the author?  ")
    content = input("Please write your content ")
    filename = title.replace(" ","") + ".txt"
    entry = open(filename, "a")
    entry.write(author + "\n")
    entry.write(title + "\n")
    entry.write(str(datetime.datetime.now()) + "\n")
    
    count = 0
    prev_index = 0
    for i in range(0, len(content) - 1):
        if content[i] == " ":
            entry.write(content[prev_index:i])
            count += 1
            prev_index = i
        if count == 10:
            count = 0
            entry.write("\n")
            
    entry.close()
def delete_entry():
    title = input("What's the title of the entry?  ")
    filename = title.replace(" ","") + ".txt"
    os.remove(filename)

choice=0
while choice!="6":
    print("What would you like to do?: ")
    print("1: Create a diary")
    print("2: Open a diary")
    print("3: Create an entry")
    print("5: Delete an entry")
    print("6: Exit")
    choice = input("Your choice:  ")
    if choice == "1" :
        create_diary()
    elif choice == "2" :
        open_diary()
    elif choice == "3":
        add_content()
    elif choice == "4":
        delete_entry()
    
     

