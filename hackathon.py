#Banking System mini project 
# syed muhammad umar
# 333709
# sir nasir hussain

# Module -1 (Open a Account)
def OpenNewAccount():
    n1 = input("Enter your First Name")
    n2 = input("Enter your Last Name")
    return{
        "First Name": n1,
        "Last Name" : n2
    }

# Sub Module (This function is used to check if user is exist in the bank dictionary or nor)
def VerifyUser(username):
    for a in userAccounts:
        if username == a:
            print(f" Your Account Name: {a} ")
            return True
        else:
            print("you dont have any bank account")
            return False
        
# Sub Module (Bank of umar)
def bankOfUmar(accountHolderName, Balanced):
    bank = {
    "AccountHolder" : accountHolderName,
    "Balance" : Balanced
    }
    return bank


# Sub Moduel ("take user name" and check and return verified user name)
def inputUserName():
    Q2 = input("Enter your name: ")
    vu = VerifyUser(Q2)
    if vu == True:
        return Q2
    else:
        print("invalid userName or Credentials")




# use while loop for multipe intries and selection
while True:
    print("Enter: Admin/User")
    role = input("Enter your Role Admin/User").upper()
    if role == "Admin".upper():
        print("Admin Login Successfully")
        print("Options: view total deposite/ check total number of accounts... ")
        admin = int(input("1 ==> view total deposite/ 2 ==> check total number of account"))
        # here all admin roles are
        if admin == 1:
            print("here we will print total amount in the bank !!!!")
        elif admin == 2:
            print("here we will print or check total bank accounts in the bank !!!!!")
        else:
            print("Incorrect Selection")   
    elif role == "User".upper():
        print("Options.....")
        
        
        print("Select: 1 => Open New Account /n 2 => Deposit money /n 3 => Withdraw money  /n 4 => Check balance /n 5 =>  Transfer Money /n 6 => Transaction Statement ")
        userQuery = int(input("Enter your Selection"))
        # here all user roles are
        if userQuery == 1:
            print("Enter your personal details to Open new Bank Account")
            # userAccount carry user account data
            userAccounts = OpenNewAccount()
        elif userQuery == 2:
            print("Deposit Money here")
            cz = inputUserName()
            print("OK your Account Exist ")
            deposit = int("Enter Your Amount :")
            bankOfUmar(accountHolderName = cz, balanced = deposit)
            userAccounts["Balanc"] = bankOfUmar()
            
        elif userQuery == 3:
            print("withdraw money")
            print("Enter Your Account name")
            cs = inputUserName()
            widraw = int(input("Enter Amount for widraw"))
            
            
        elif userQuery == 4:
            print("Check Balance")
            
        elif userQuery == 5:
            print("transfer Money")
            
        elif userQuery == 6:
            print("Transactions Statement")
            
