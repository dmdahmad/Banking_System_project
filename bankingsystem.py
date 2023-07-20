# Banking system

customerNames = ['ahmad', 'alisha', 'murphy', 'mahesh']
customerPincodes = ['6996', '8989', '7858', '5254']
customerBalances = [100000, 52000, 200000, 300000]
deposition = 0
withdrawal = 0
balance = 0
counter_1 = 1
counter_2 = 4
i = 0


while True:
    print('*'*44)
    print('-'*10,'Welcome to Indian Bank','-'*10)
    print('*'*44)
    print(' '*7,"1. Open a new account")
    print(' '*7,"2. Withdraw money")
    print(' '*7,"3. Deposit")
    print(' '*7,"4. Check customers & balance")
    print(' '*7,"5. Exit/Quit")
    print('*'*44)
    
    choicenumber = input("Select your choice number from the above : ")
    
    if choicenumber =="1":
        print("Choice number 1 is selected by the customer")
        NOC = eval(input("Number of Customers : "))

        i = i + NOC
        if i > 4:
            print("\n")
            print("Customer registration exceed reached")
            i = i - NOC
        else:
            while counter_1 <= i:
                name = input("Enter the name : ")
                customerNames.append(name)
                pin = str(input("Enter the pin number : "))
                customerPincodes.append(pin)
                balance = 0
                deposition = eval(input("Please input a value to deposition : "))
                balance = balance + deposition
                customerBalances.append(balance)
                print("\nName : ", end=" ")
                print(customerNames[counter_2])
                print("Pin : ", end=" ")
                print(customerPincodes[counter_2])
                print("Balance", end=" ")
                print(customerBalances[counter_2], end= " ")
                print("-/Rs")
                counter_1 = counter_1 + 1
                counter_2 = counter_2 + 1
                print("\nYour name is added")
                print("Your pin is added to customer system")
                print("Your balance is added to customer system")
                print("-----New account created successfully-----")
                print("\n")
                print("Your name is available on the customer list now : ")                     
                print(customerNames)
                print("\n")
                print("Note! please remember the name and pin number")
                print("-"*46)                
        mainmenu = input("Please press enter key to go back to main menu or exit : ")
        print("\n")
    elif choicenumber == "2":
        j = 0
        print("Choice 2 is selected by the customer")
        while j<1:
            k=-1
            name = input("Enter the name : ")
            pin = input("Enter the pin : ")
            while k < len(customerNames) - 1:
                k = k+1
                if name == customerNames[k]:
                    if pin == customerPincodes[k]:
                        j = j+1
                        print("Your current balance : ", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/Rs\n")
                        balance = (customerBalances[k])
                        withdrawal = eval(input("Enter the withdraw amount : "))
                        if withdrawal > balance:
                            deposition = eval(input("Please deposit a higher value because your balance mentioned is not enough : "))
                            balance = balance + deposition
                            print("Your current balance : ", end=" ")
                            print(balance, end=" ")
                            print("-/Rs\n")
                            balance = balance  - withdrawal
                            print('\n')
                            print("-----Withdraw successfully-----")
                            customerBalances[k] = balance
                            print("Your new balance : ", end=" ")
                            print("-/Rs\n\n")
                        else:
                            balance = balance - withdrawal
                            print("\n")
                            print("-----Wihdraw successfully-----")
                            customerBalances[k] = balance
                            print("Your new balance : ", balance, end=" ")
                            print("-/Rs\n\n")
            if j < 1:
                print("Your name and pin does not match\n")
                break
        mainmenu = input("Please press enter key to go back to main menu or exit : ")
        print("\n")
    elif choicenumber == "3":
        print("Choice number 3 is selected by the customer")
        n = 0
        while n<1:
            k = -1
            name = input("Enter the name : ")
            pin = input("Enter the pin : ")
            while k < len(customerNames) -1:
                k = k+1
                if name == customerNames[k]:
                    if pin == customerPincodes[k]:
                        n = n + 1
                        print("Your current balance : ", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/Rs")
                        balance = (customerBalances[k])
                        deposition = eval(input("Enter the value to deposit the amount : "))
                        balance = balance + deposition
                        customerBalances[k] = balance
                        print("\n")
                        print("-----Deposit successfully-----")
                        print("Your new balance : ", balance, end=" ")
                        print("-/Rs\n\n")
            if n < 1:
                print("Your name and pin does not match\n")
                break
        mainmenu = input("Please press enter key to go back to main menu or exit : ")
        print("\n")
    elif choicenumber == "4":
        print("Choice number 4 is selected by the customer")
        k = 0
        print("Customer name list and balances mentioned below : ")
        print("\n")
        while k <= len(customerNames) -1:
            print("--> CUSTOMER - ", customerNames[k])
            print("-->  BALANCE - ", customerBalances[k], end=" ")
            print("-/Rs")
            print("\n")
            k = k + 1
        mainmenu = input("Please press enter key to go back to main menu or exit : ")
        print("\n")
    
    elif choicenumber == "5":
        print("Choice number 5 is selected by the customer")
        print("Thank you using our banking system")
        print("\n")
        print("~"*10,"Come again","~"*11)
        print("~"*12,"See you","~"*12)
        break
    else:
        print("invalid option selected")
        print("please try again")
        mainmenu = input("please press enter key to go back to main menu or exit : ")
        print("\n")


