import dataIO as io
import os

def membershipDisplay(member):
    os.system("cls")
    print("-"*60)
    for i in range(len(member)):
        print("%-11s  %-30s  %7s" %(member[i][0], member[i][1],member[i][2]))
    print("-"*60)

def memberships():
    loop = True 
    member = data.openfile("membershiptier", "r")
    while loop:
        membershipDisplay(member)
        opt=input("<A>dd   <E>dit   <D>elete   <Q>uit>>")
        if opt == "A":
            while True:
                tiercode = input("Enter New Membership Tier <Q>uit >> ")
                if tier == "Q":
                    loop = False
                    os.system("cls")
                    memberships()
                tierdsc = input("Enter New Membership Description <Q>uit >> ")
                if tier == "Q":
                    loop = False
                    os.system("cls")
                    memberships()
                tierpercent = input("Enter New Discount Percentage <Q>uit >> ")
                if tier == "Q":
                    loop = False
                    os.system("cls")
                    memberships()
                member.append([tiercode, tierdsc, tierpercent])
                data.savefile("membershiptier", "w", member)
                break
        elif opt == "E":
            tier = input("Enter Membership Tier <Q>uit >> ")
            if tier == "Q":
                    loop = False
                    os.system("cls")
                    memberships()
            for i in range(len(member)):
                if member[i][0] == tier:
                    print("Which Membership Tier to Edit?")
                    editChoice = input("<T>ier   <D>escription   <P>ercentage >> ")
                    if editChoice == "T":
                        newtier = input("Input new tier >> ")
                        member[i][0] = newtier
                    elif editChoice == "D":
                        newdsc = input("Input new description >> ")
                        member[i][1] = newdsc
                    elif editChoice == "P":
                        newpercent = input("Input new percentage >> ")
                        member[i][2] = newpercent
                    data.savefile("membershiptier", "w", member)
                break
        elif opt == "D":
            memTier = input("Which Membership Tier to Delete? ")
            updatedMem = [item for item in member if item[0] != memTier]
            member = updatedMem
            data.savefile("membershiptier" ,"w", updatedMem)
        elif opt == "Q":
            loop=False
            os.system("cls")
            menu()

memberships()
