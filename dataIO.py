#Program Name   : dataIO
#Purpose        : Module for data input and output
#Author         : Jayden Yong
#Created        : 13/11/2023

#Importing modules
import os

#Directory path reroute
os.chdir("X:\Programming Concepts and Design\PCD Assignment\PCD-Assignment")

#Function to prepare data list from file
def openfile(name,mode):
    f = open(name+".txt",mode)                      #Open's data file
    rec = f.readlines()                             #Reads data file and store each line as a list item
    f.close()                                       #Close's data file

    itemList = []                                   #Initialise item list

    for i in range(len(rec)):                       #Loop for each line in record
        item = rec[i].strip("\n").split("|")        #Strip's newline character and split's each line into a list
        itemList.append(item)                       #Append's each item with its details into item list
    
    return itemList                                 #Gives back a ready to use item list

#Function to save data list into file
def savefile(name,mode,itemList):
    write = ""
    for i in range(len(itemList)):
        write += "|".join(itemList[i])+"\n"
    f = open(name+".txt",mode)
    f.write(write)
    f.close()
