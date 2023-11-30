#WIP
import os

def isFloat(num):
    status =True
    try:
        num=float(num)
    except:
        status =False
    return status

def errormsg():
    print("Under construction")
    
def readFile():  #change1
    f=open("itemM.txt","r")
    rec=f.readlines()
    f.close()
    #format
    recf=[x.strip("\n").split("|") for x in rec]
    return recf  #after reading the record, return the record

def displayMember(mem): #change4

    #for i in range(len(recf)):
    os.system("cls")
    print("-"*50)
    mem=sorted(mem)
    for line in recf:
        print("%s  %s-20s  %8.2f"%(line[0], line[1][:20],float(line[2])))
    print("-"*50)
    
def displayMenuOpt1():
    print("<A>dd   <U>pdate   <D>elete  <S>ave    <Q>uit")

#Membership Tier & Colour (Need Changing)

def chkCard(itm,recf):

    status =False
    for i in range(len(recf)):
        if itm==recf[i][0]:
            status=True
            break
    return status

def crud(opt):
    print("Akan datang")

def crudAdd(opt,recf):
    loop=True
    step=1
    while loop:
        if step==1: #add, update or delete item
            itm=input("Enter Item  <Q>uit >> ")
            if itm=="Q":
                step=99
            elif chkItem(itm,recf):
                print("Item exist, cannot add the same item again")
            else:
                step +=1
            '''
                if opt=="A":
                    print("Item exist")
                else:
                    step +=1
            else:
                if opt=="A":
                    step +=1
                else:
                    print("Item doesn't exist")
            '''
        if step==2:
            itmDsc=input("Enter Member Description <Q>uit >> ")
            if itmDsc=="Q":
                step=99
            else:
                step=step+1

        if step==3:
            price=input("Enter Item Price  <Q>uit  >> ")
            if price=="Q":
                step=99
            elif not isFloat(price):
                print("Invalid price value entered")
            else:
                step=step+1
                
        if step==4: #everything is ok
            recf.append([itm, itmDsc, price])
            step=99

        if step==99:
            loop=False
            
    return recf

#MembershipMenuSystem

#Part1

import uuid

class MembershipSystem:
    def __init__(self):
        self.members={}

    def add_member(self, name):
        member_id=str(uuid.uuid4())[:8]
        self.members[member_id]= name
        return member_id
    def update_member(self,member_id, new_name):
        if member_id in self.members:
            self.members[member_id] = new_name
            return True
        else:
            return False
    def delete_member(self, member_id):
        if member_id in self.members:
            del self.members[member_id]
            return True
        else:
            return False

    def get_member_name(self, member_id):
        return self.members.get(member_id, "Member not found")

membership_system = MembershipSystem()

#Part2

def opt1():
    #print("under construction")
    loop=True
    #change2
    rec=readFile()
    while loop:
        displayMember(mem) #change3
        displayMenuOpt1()
        opt=input("Option >> ").upper()
        if opt=="Q":
            loop=False
            os.system("cls")
            choose()
        elif opt=="A":
            while True:
            memName=input("Enter Member Name           >>")
            memTier=input("Enter Membership Tier (B/S/G/P) >>")
            if memTier == "B":
                memTier = "Bronze"
            elif memTier == "S":
                memTier = "Silver"
            elif memTier == "G":
                memTier = "Gold"
            elif memTier == "P":
                memTier = "Platinum"
            else:
                print("Invalid Membership Tier")
            #rec=crudAdd(opt,rec)
        elif opt=="U":
            data.saveFile("MemberLst", "w", mem)
            print("Member list updated successfully.")
            #crud(opt)
        elif opt=="D":
            memID=input("Enter Member Registered ID >>")
            def deleteMem(memID, mem):
                updatedMem = [item for item in mem if item[0] != memID]
                if len(updatedMem) == len(mem):
                    print(f"Member ID {memID} is invalid.")
                else:
                    data.saveFile("MemberLst", "w", updatedMem)
                    print(f"Member ID {memID} is successfully deleted.")
                return updatedMem
            mem=deleteMem(memID, mem)
            #crud(opt)
        elif opt=="S":
            errormsg()
        else:
            print("Invalid option")
if __name__=="__main__":
    opt1()

#Q to ask Friday
#Option 1 : Generate Randomize Unique ID
#Option 2 : Using Email/Number(preferably email) to substitute
#point system to up tier
#B:5% | S:10% | G:15% | P:20%
