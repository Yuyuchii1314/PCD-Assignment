import dataIO as io
import os

def membershipDisplay(member):
    os.system("cls")
    print("-"*60)
    for i in range(len(member)):
        print("%-11s  %-30s  %7s" %(member[i][0], member[i][1],member[i][2]))
    print("-"*60)

def memberships():
    loop=True
    member=data.openfile("membershiptier","r")
    while loop:
        membershipDisplay(member)
        opt=input("<A>dd   <E>dit   <D>elete   <Q>uit>>")
        if opt == "A":
            while True:
                tiercode = input("Enter New Membership Tier   <Q>uit >> ")
                while loop:
                    if opt== "Q":
                        loop=False
                        os.system("cls")
                        memberships()
                        tierdsc = input("Enter New Membership Description   <Q>uit >>")
                        while loop:
                            if opt== "Q":
                                loop=False
                                os.system("cls")
                                memberships()
                    else:
                        tierpercent = input("Enter New Discount Percentange   <Q>uit  >> ")
                        while loop:
                            if opt== "Q":
                                loop=False
                                os.system("cls")
                                memberships()
                    member.append([tiercode, tierdsc, tierpercent])
                    data.savefile("membershiptier", "w", member)
                    memberships()
        elif opt == "E":
            for i in range(len(mem)):
                if mem[i][0] == memCode:
                    print("---Current Details---")
                    print(f"Member's Phone No.: {mem[i][0]}")
                    print(f"Member's Name: {mem[i][1]}")
                    updName = input("Enter Updated Name (Press Enter to maintain current info): ")
                    if updName!="":
                        mem[i][1] = updName
                    data.saveFile("membershiptier", "w", member)
                    print("Member information updated successfully.")
        elif opt == "D":
            memNo=input("Enter Membership Tier to delete   <Q>uit >>")
            def deleteMem(memNo, mem):
                updatedMem = [item for item in member if item[0] != memNo]
                data.saveFile("membershiptier", "w", member)
        elif opt == "Q":
            loop=False
            os.system("cls")
            menu()

memberships()
