import random

#Global Variables- uniqid of customer & customer inforamtion as list(custinfolist) in dictionary(custdict)
custdict={}
custinfolist=[]

#Function - Display balance amount of customer
def display(uniqid): 
    cust_info=file_read()
    for k in cust_info:
        if (uniqid)==k:
            balvalue=cust_info[uniqid][4]
            print("\n Amount balance:" +str(balvalue))

#Function - Deposit amount(into dictionary & then write to file) only if 5000<=amount>=50000
def deposit(uniqid): 
    amount=int(input("Enter amount to be Deposited: ")) 
    cust_info=file_read()
    bal=cust_info[uniqid][4]
    for k in cust_info:
        if (uniqid)==k:
            if amount in range(5000,50001):
               cust_info[uniqid][4]=(cust_info[uniqid][4] + amount)
               print("\n Amount Deposited:")
               custdict=cust_info
               break
        else:
            print("Deposit should be between 5000 and 50000")
    file_write(custdict)    

#Function - Withdraw amount(into dictionary & then write to file) only if min balance is 10000
def withdraw(uniqid): 
    amount = int(input("Enter amount to be Withdrawn: ")) 
    cust_info=file_read()
    for k in cust_info:
        if (uniqid)==k:
           amount_avail=cust_info[uniqid][4]
           amount_avail1=cust_info[uniqid][4] - 10000
           if (amount_avail1>=amount):
              cust_info[uniqid][4]= (cust_info[uniqid][4] - amount)
              print("\n You Withdrew:", amount)
              custdict=cust_info
              break
           else: 
              print("\n Insufficient balance  ")
    file_write(custdict) 
#Function - To generate unique id for every customer     
def checkuniqexists():
    uid=random.randint(100,200)
    if uid not in custdict:
      return uid
    else:
      return (random.randint(100,200))
    
#Function - Writing dictionary into file
def file_write(cust):
    f=open("accdetails.txt",'w+')
    f.write('%s\r\n'%(cust))
    f.close()
    
#Function - Reading dictionary from file
def file_read():
    f=open("accdetails.txt",'r')
    c=eval(f.read())
    f.close()
    return c

#Function- Account Registration for the first time
def acc_reg(name,email,pwd,phno):
    key=checkuniqexists()
    balance=10000
    custinfolist.append(name)
    custinfolist.append(email)
    custinfolist.append(pwd)
    custinfolist.append(phno)
    custinfolist.append(balance)
    custdict[key]=custinfolist
    file_write(custdict)
    return key

#Function- Login into Account
def login():
    continueoperation='Y'
    while continueoperation in ('Y','y'):
        if (choice==1):
            print("Enter name:")
            name=input()
            print("Enter email id:")
            email=input()
            print("Enter Password:")
            pwd=input()
            print("Enter phone no:")
            phno=input()
            key=acc_reg(name,email,pwd,phno)
            print("Your unique id:"+str(key))
            return input("Do you wish to continue Y/N:")
        elif (choice==2):
            key=int(input("Enter your unique id:"))
            pwd=input("Enter your password:")
            custfile=file_read()
            if (pwd in custfile[key]):
                    print("Login Successful")
                    print("1.Display balance 2.Deposit cash 3.Withdraw Cash 4.logout\n")
                    user_input=int(input())
                    if (user_input ==1):
                        display(key)
                        break
                    elif(user_input ==2):
                        deposit(key)
                        break
                    elif(user_input==3):
                        withdraw(key)
                        break
                    elif(user_input==4):
                        exit()                   
            else:
                    print("Login failed, Please enter correct password")
    return input("Do you wish to continue Y/N: ")

print("Customer operations:")
print("1.Register 2.login")
choice=int(input())
value=login()




























    
