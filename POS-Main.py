#Program Name   : POS-Main
#Purpose        : Main program for POS system
#Author         : Jayden Yong
#Created        : 13/11/2023

#Importing modules
import os
import dataIO as io
import functions as fn

#SALES module design
def salesDisplay(itemList):
    os.system("cls")    #Clears screen

    print("-"*60)
    print("Welcome to Retail Store")
    print("-"*60)
    print("Product Code     Product Description          Price(RM)")
    print("-"*60)

    for i in range(len(itemList)):
        print(f"{itemList[i][0]:<3}{itemList[i][1]:<30}{float(itemList[i][2]):>8.2f}")

    print("-"*60)
    print("<S>hop now     <Q>uit")
    print("-"*60)

def main():

    #may add choice for item master and sales module

    loop = True
    while loop:
        itemList = io.openfile("product-list","r")
        salesDisplay(itemList)
        opt = input("What do you wish to do? >> ").upper()

        if opt == "S":
            print("-"*60)
            
