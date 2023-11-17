#Program Name   : functions
#Purpose        : Module for functions
#Author         : Jayden Yong
#Created        : 13/11/2023

def productInput(itemList):
    code =     input("Please enter product code >> ")

    for i in range(len(itemList)):
        if code == itemList[i][0]:
            qty  = int(input("Please enter quantity     >> "))

            if qty > itemList[i][3]:
                print("Insufficient stock")
                input()
            
            else:
                itemList[i][3] -= qty
                print("Product successfully added to cart")
                input()
        
        

    