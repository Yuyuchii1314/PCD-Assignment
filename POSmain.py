#Program Name   : POS-Main
#Purpose        : Main program for POS system

#Importing modules
import os
import dataIO as io
import itemMaintenance as im

#Main menu design
def menu():
    os.system("cls")    #Clears screen

    print("-"*60)
    print("Electrical Appliances Shop")
    print("-"*60)
    print("<1> Item Maintenance")
    print("<2> Stock/Inventory Management")
    print("<3> Membership Maintenance")
    print("<4> Sales")
    print("<5> Reports")
    print("<Q> Quit")
    print("-"*60)

#Main program
def main():
    loop = True
    while loop:
        menu()
        opt = input("What do you wish to do? >> ")

        if opt == "1":
            im.maintenance()
        elif opt == "2":
            print("coming soon")
            input("")
        elif opt == "3":
            print("coming soon")
            input("")
        elif opt == "4":
            print("coming soon")
            input("")
        elif opt == "5":
            print("coming soon")
            input("")
        elif opt == "Q" or opt == "q":
            loop = False
        else:
            print("Invalid input. Please try again.")
            input("")

main()
            
