import datetime as dt

diary={}
def add_entry():
    #adds an entry to the dictionary
    text=input("Write whatever you like here: ")
    date=dt.datetime.now()
    date_str=str(date)
    diary[date_str]=text

def view_entries():
    #displays all entries in chronological order
    sorted_diary = dict(sorted(diary.items()))
    for i in sorted_diary:
        print("Date: "+i)
        print(diary[i])
        print("------------------------------------------------")

def delete_entry():
    #deletes an entry
    date=input("Please enter the date and time of the entry you want to delete: ")
    if (date in diary):
        diary.pop(date)
        print("Entry was succesfully deleted")
    else:
        print("There is no entry with this date and time")
def search_entries():
    #searches for entries based on specific keywords
    keywords=input("Please enter any keywords seperated by space: ").split()
     
    sorted_diary = dict(sorted(diary.items()))
    print("Results:")
    d=0
    for i in sorted_diary:
        count=0
        for j in keywords:
            if (j in diary[i]):
                count+=1
        if count==len(keywords):
            d+=1
            print("Date: "+i)
            print(diary[i])
            print("------------------------------------------------")
    if d==0:
        print("No results were found")

if __name__ == "__main__":
    print("To add an entry press 1")
    print("To delete an entry press 2")
    print("To view existing entries press 3")
    print("To search for entries using keywords press 4")
    print("To exit press any other symbol")
    print()
    choice=input("Please enter a number: ")
    while (True):
        if (choice=='1'):
            add_entry()
        elif (choice=='2'):
            delete_entry()
        elif (choice=='3'):
            view_entries()
        elif (choice=='4'):
            search_entries()
        else:
            print("Good Bye!")
            break
        print("To add an entry press 1")
        print("To delete an entry press 2")
        print("To view existing entries press 3")
        print("To search for entries using keywords press 4")
        print("To exit press any other symbol")
        print()
        choice=input("Please enter a number: ")
    
