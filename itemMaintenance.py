#Program Name: Item Maintenance
#Purpose: To maintain the item database (product-list.txt)

#Importing modules
import os
import dataIO as io

def line():
    print("-"*60)  

itemList = io.openfile("product-list","r")   #Opens product-list.txt and stores it as a list

#Function to add item
def add():
    loop = True
    while loop:
        code  = input("Enter Item Code        >> ")
        if any(item[0] == code for item in itemList):
            print("Item code already exists. Please re-enter item code.")
        else:
            break

    desc  = input("Enter Item Description >> ")
    price = input("Enter Item Price (RM)  >> ")
    stock = "0"

    itemList.append([code,desc,price,stock])    #Appends new item into item list

    io.savefile("product-list","w",itemList)    #Saves item list into product-list.txt

def modify():
    item   = input("Enter Item Code To Modify   >> ")
    targetDD = {"C":0,"D":1,"P":2}
    
    loop = True
    while loop:
        for x in range(len(itemList)):
            if itemList[x][0] == item:
                line()
                print("<C>ode     <D>escription     <P>rice")
                line()
                target = input("What do you wish to modify? >> ").upper()
                new    = input("Enter new value             >> ")
                itemList[x][targetDD[target]] = new
                io.savefile("product-list","w",itemList)
                loop = False
                return

        print("Item code not found.")
        item = input("Please re-enter item code >> ")
        loop = True

#Function to delete item
def delete():
    while True:
        code = input("Enter Item Code To Delete >> ")

        for i in range(len(itemList)):
            if itemList[i][0] == code:
                del itemList[i]
                io.savefile("product-list","w",itemList)
                return
        
        print("Item code not found. Please re-enter item code.")


def invalid():
    print("Invalid input. Please try again.")
    input("Press any key to continue.")

fnList = ["",add,modify,delete,invalid]

#Main menu design
def maintenance():
    loop = True
    while loop:
        os.system("cls")    #Clears main menu

        line()
        print(f"{'Item Master Maintenance':^60s}")
        line()

        for i in range(len(itemList)):
            print(f"{i+1:^5d}{itemList[i][0]:5s}{itemList[i][1]:40s}{float(itemList[i][2]):8.2f}")   #Prints item list in a table format

        line()
        print("<A>dd     <M>odify     <D>elete     <Q>uit")
        line()

        opt = input("What do you wish to do? >> ").upper()

        if opt == "Q":
            loop = False
        else:
            idx = (opt == "A")*1 + (opt == "M")*2 + (opt == "D")*3 + (opt not in "AMQD")*4
            fnList[idx]()  #Calls function from function list