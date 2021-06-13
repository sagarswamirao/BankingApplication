
# coding: utf-8

# In[ ]:


from time import sleep
import re
import random
from getpass import getpass
from IPython.display import clear_output
import json


def dec(func):
    def inner(*args,**kwargs):
        print("*"*100)
        r=func(*args,**kwargs)
        print("*"*100)
        return r
    return inner


def loading():
    print("loading",end='')
    sleep(0.7)
    for i in range(4):
        print(".",end='')
        sleep(0.7)
    print('.')

@dec
def password():
    
    
    pas=getpass(prompt="Password must contain atleast one uppercase character, one lowercase chracter, one digit and special symbols\nInput pass: ")
    loading()
    validate(pas)
    sleep(1)
    return pas


def validate(pas):
    
    specialChars=re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    upperChar=re.compile('[A-Z]')
    lowerChar=re.compile('[a-z]')
    digits=re.compile('[0-9]')
    count=0
    
    if upperChar.search(pas)!=None:
        count+=1

    if lowerChar.search(pas)!=None:
        count+=1
    if digits.search(pas)!=None:
        count+=1
    if specialChars.search(pas)!=None:
        count+=1

    if count>3:
        print('Passwords strength: Strong')
        sleep(0.5)
        print("Password set successfully")
    elif count == 3:
        print('Password strength: Intermediate')
        sleep(0.5)
        print("Enter password again")
        
        password()
    else:
        print('Password strength: Weak')
        sleep(0.5)
        print("Enter password again")
        
        password()
        
    return None
@dec
def deposit(): 
    
    
    print("Deposit a starting balance\nMinimum amount should be Rs.1500")
    amt=int(input("Enter the amount to be deposited: "))
    
    if amt>=1500:
        print(f"Amount {amt} successfully added to your account")
    else:
        print("Insufficient amount")
    
    return amt
        
@dec
def i1():
    
    acc_no=input("Enter account no. to which you want to deposit money: ")
    
    if acc_no in keys:
        amt=int(input(f"Hello {d[acc_no][0]}\nEnter amt to be deposited: "))
        d[acc_no][5]+=amt
        loading()
        print("Money added successfully")
    else:
        print("No such account exist")
    sleep(2)
@dec
def i2():
    
  
    acc_no=input("enter your acc nuber: ")

    if acc_no in keys:
        print(f"Hello {d[acc_no][0]}!")
        
        id=input("enter your id: ")
        pas=getpass(prompt="enter your password: ")
        loading()
        if id==d[acc_no][7][0] and pas==d[acc_no][7][1]:
            amt=int(input("enter amt to be withdrawed: "))
            if amt<=d[acc_no][5]:
                d[acc_no][5]-=amt
                loading()
                print("withdrawal successful!")
            else:
                print("You have insufficient balance")        
        else:
            print("Invalid id or pass\nPlease try again")
    else:
        print("No such account exist")
    sleep(2)

@dec
def i3():
    
    acc_no=input("enter your acc number: ")
    if acc_no in keys:
        id=input("enter your id: ")
        pas=getpass(prompt="enter your password: ")
    
        if id==d[acc_no][7][0] and pas==d[acc_no][7][1]:
            confirm=input("Are you sure you want to paermanently delete your account\nPress 'y' for yes and 'n' for no-->").strip().lower()
            if confirm=='y':
                del(d[acc_no])
                keys.remove(acc_no)
                loading()
                print("account successfully closed")
            else:
                print("Account not deleted")
        else:
            print("invalid user id or pass.Try again")
    else:
        print("No such account exist")
    
    sleep(2)
@dec
def i4():
    
    
    
    acc_no=str(int(keys[-1])+1)
    print(f"Account Number: {acc_no}")

    name=input("Enter your name: ").strip().title()
    
    age=int(input("Enter your age: "))
    
    dob=input("Enter your date of birth dd/mm/yyyy")
    
    mob=int(input("Enter your mobile number: "))
    
    adhar=int(input("Enter your adhar number: "))
    
    add=input("Enter your address: ").strip()

    id=input("Enter your id: ").strip().lower()
    
    print("Set a password for your account")
    pas=password()
    
    amt=deposit()
    if amt>=1500:
        d.update({acc_no:[name,mob,age,dob,add,amt,adhar,[id,pas]]})
        keys.append(acc_no)
        loading()
        clear_output()
        
        print("*"*100)
        print("Your account is created successfully!!")
        
        
        print(f"Account No: {acc_no}\nName: {name}\nD.O.B: {dob}\nMobile No: {mob}\nAge: {age}\nAmount: {amt}\nAdhaar No: {adhar}\nAddress: {add}\nID: {id}")
        
    else:
        print("Your account could not be created")
    sleep(2)    
        
    
@dec                
def i5():
    
    acc_no=input("enter your account number: ")
    if acc_no in keys:
        idd=input("Enter your user id: ").strip()
        paswrd=getpass(prompt="Enter your password: ")
        
        if idd==d[acc_no][7][0] and paswrd==d[acc_no][7][1]:
            
            print("1.Private employee\n2.Government employee\n3.Businessman\n4.Student")
            occ=input("Please enter your occupation:")
            sal=int(input("Enter your Salary Per Month/Annual Turnover: "))
            emis=int(input("Enter Sum of your current EMI(s): "))
            loading()
            if emis>=sal/2:
                    print("You are not eligible for loan")
            else:
                if occ=='1':
                
                    if sal>=50000:
                        max=100000
                        print("You are eligible for a maximum loan of Rs.1 lakh")
                        print("Interest rate: 12.5%")
                        amt=int(input("Enter amount of loan: "))
                        

                    elif sal>=20000 and sal<50000:
                        max=50000
                        print(f"You are eligible for a maximum loan of Rs.{max}")
                        print("Interest rate: 12.5%")
                        amt=int(input("Enter amount of loan: "))
                    
                    else:
                        amt=1
                        max=0
                        print("Sorry! You are not eligible for loan")
                          

                elif occ=='2':
                    if sal>=50000:
                        max=500000
                        print("you are eligible for a loan of maximum Rs.5 lakh")
                        print("Interest rate: 10%")
                        amt=int(input("Enter amount of loan: "))
                    
                    elif sal>=20000 and sal<50000:
                        max=100000
                        print("you are eligible for a loan of maximum Rs.100000")
                        print("Interest rate: 10%")
                        amt=int(input("Enter amount of loan: "))
                    else:
                        amt=1
                        max=0
                        print("Sorry! You are not eligible for loan ")
                    
                    
                elif occ=='3':
                    if sal>=1200000:
                        max=500000
                        print("you are eligible for a loan of maximum Rs.500000")
                        print("Interest rate: 13%")
                        amt=int(input("Enter amount of loan: "))
                    
                    
                    elif sal<120000 and sal>=600000:
                        max=200000
                        print("you are eligible for a loan of maximum Rs.200000")
                        print("Interest rate: 13%")
                        amt=int(input("Enter amount of loan: "))
                        
                    else:
                        amt=1
                        max=0
                        print("Sorry! You are not eligible for loan ")
                else:
                    amt=1
                    max=0
                    print("Sorry! You are not eligible for loan ")
                if amt<=max:
                    confrm=input("Are you sure to persue loan?\nPress 'Y' for YES and 'N' to DENY-->").upper().strip()
                    if confrm=='Y':
                        d[acc_no][5]+=amt
                        loading()
                        print("Loan credited successfully")
                    else:
                        print("No loan credited")
                else:
                    print("Requirements not fulfilled.No loan credited")
        
        else:
            print("Invalid username or password.Please try again.")
        
    else:
        print("No such account exist")   
    sleep(2)
        
@dec
def i6():
    
    
    acc_no=input("Enter your account number: ")
    if acc_no in keys:
        
        print(f"Hello {d[acc_no][0]}!")
        print("What you want to update-\n1.Adhar Number\n2.Mobile No\n3.Password\n4.Address")
        choice=int(input('Enter your choice: '))
    
        
        idd=input("Enter your id: ")
        p=getpass(prompt="Enter your password: ")
        loading()

        if p==d[acc_no][7][1] and idd==d[acc_no][7][0]:
            if choice==1:
                adhar=int(input("Enter new adhar no: "))
                d[acc_no][6]=adhar
                print("Account successfully updated!!")
            elif choice==2:
                mob=int(input("Enter new mob no: "))
                d[acc_no][1]=mob
                print("Account successfully updated!!")
            elif choice==3:
                print("Set new password for your account")
                paswrd=password()
                d[acc_no][7][1]=paswrd
                
                print("Account successfully updated!!")
            elif choice==4:
                add=input("enter new address: ")
                d[acc_no][4]=add
                print("Account successfully updated!!")

            else:
                print("Wrong Choice")

        else:
            print("Invalid user id or password")
    else:
        print("No such account exist")
    sleep(2)
        
       

    
@dec
def i8():
    acc_no=input("Enter your account number: ")
    if acc_no in keys:
        idd=input("Enter your user id: ")
        paswrd=getpass(prompt='Enter your password: ')
        
        if idd==d[acc_no][7][0] and paswrd==d[acc_no][7][1]:
            loading()
            
            clear_output()
            print("*"*100)
            print(f"Account Number: {int(acc_no)}\nName: {d[acc_no][0]}\nD.O.B: {d[acc_no][3]}\nMobile No. : {d[acc_no][1]}\nAddress: {d[acc_no][4]}\nCurrent Balance: {d[acc_no][5]}\nAdhar No.: {d[acc_no][6]}\nUser ID: {d[acc_no][7][0]} ")
        else:
            print("Invalid user id or password.")
    else:
        print("No such account exist.")
    sleep(2)
        
        
@dec       
def i7():
    acc_no=input("Enter your account number: ")
    if acc_no in keys:
        idd=input("Enter your user id: ")
        paswrd=getpass(prompt='Enter your password: ')
        
        if idd==d[acc_no][7][0] and paswrd==d[acc_no][7][1]:
            print(f"Current Account Balance : {d[acc_no][5]}")
        else:
            print("Invalid user id or password.")
    else:
        print("No such account exist.")
    sleep(2)

@dec                
def exit():
    fp=open("bank.json","r+")
    fp.seek(0)
    json.dump(d,fp)
    fp.truncate()
    fp.close()

    print("Thank You...")


# In[ ]:


nxt=1


fp=open("bank.json","r")
fp.seek(0)
d=json.load(fp)
fp.close()
keys=list(d)


while nxt==1:
    clear_output()
    print("*"*100)

    print("Welcome!!")

    op=int(input("1.Deposit Money\n2.Withdraw Money\n3.Account Close\n4.New Account\n5.Loan Sanction\n6.Update Personal Info\n7.Balance Enquiry\n8.Account Details\n9.Exit\n"))
    
    if op!=9:
        if op==1:
            i1()
        elif op==2:
            i2()
        elif op==3:
            i3()
        elif op==4:
            i4()
        elif op==5:
            i5()
        elif op==6:
            i6()
        elif op==7:
            i7()
        elif op==8:
            i8()
        nxt=int(input("1.Go to Home Page\n2.Exit: "))
        if nxt==1:
            continue
        else:
            exit()
            break
    else:
        exit()
        break  


# In[ ]:


fp.close()

