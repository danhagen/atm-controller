TOTAL_ACCOUNTS = {
    "1234-5678-9101-1121" : {
        "PIN":"9999",
        "MEMBER_NAME":"Daniel Hagen",
        "ACCOUNTS" : {
            "Savings Account" : 500,
            "Checking Account" : 1234567,
            "Carl's College Fund" : 1
        }
    },
    "1212-3434-5656-7878" : {
        "PIN":"1234",
        "MEMBER_NAME":"Bear Robotics",
        "ACCOUNTS" : {
            "Savings Account" : 100000,
            "Checking Account" : 5000000
        }
    },
    "5555-5555-5555-5555" : {
        "PIN":"5555",
        "MEMBER_NAME":"Donald J. Trump",
        "ACCOUNTS" : {
            "Savings Account" : 0,
            "Checking Account" : -750
        }
    }
}

class ATM:
    def __init__(self):
        self.cardInserted = False

    def card_inserted(self,cardNumber="1234-5678-9101-1121"):
        assert type(cardNumber)==str, "cardNumber should be a str."
        assert len(cardNumber)==19, "cardNumber should be 19 characters long, 16 numbers grouped into 4s with a dash (-) separating them."
        assert cardNumber.replace("-","").isdigit(), "Only numbers should be included (excluding the dashes)."
        self.cardInserted = True
        self.get_card_number(cardNumber=cardNumber)

    def detect_card(self):
        '''
        To be replaced by ATM program that detects when a card is inserted.
        '''
        exitProgram=False
        cardInserted=False
        validResponse = False
        while validResponse == False:
            cardInserted = input("Insert your card? (Y/N/[Exit]): ")
            if cardInserted.capitalize() not in ["Y","N","Exit",""]:
                validResponse = False
                print("\n" + "*"*60)
                print("Please enter your card.")
                print("*"*60 + "\n")
            elif cardInserted.capitalize() in ["Exit",""]:
                exitProgram = True
                break
            else:
                validResponse=True
                cardInserted = (cardInserted=="Y")
        return(cardInserted,exitProgram)

    def card_removed(self):
        self.cardInserted = False

        if hasattr(self,"accountInfo") and hasattr(self,"cardNumber"):
            TOTAL_ACCOUNTS[self.cardNumber]["ACCOUNTS"] = self.accountInfo

        if hasattr(self,"cardNumber"):
            delattr(self,"cardNumber")
        if hasattr(self,"accountInfo"):
            delattr(self,"accountInfo")

    def get_card_number(self,cardNumber="1234-5678-9101-1121"):
        '''
        Presumably, this function would recieve an account number from the ATM machine after reading the magnetic strip or chip. For this example, we will assume that this value is given.
        '''
        self.cardNumber = cardNumber

    def input_pin(self):
        validResponse=False
        exitProgram=False
        while validResponse == False:
            self.PIN = input("Enter your PIN: ")
            if len(self.PIN)==4 and self.PIN.isdigit():
                validResponse = True
            elif self.PIN.capitalize()=="Exit":
                exitProgram = True
                self.card_removed()
                break
            else:
                print("Invalid PIN. Please enter Again.")
        return(exitProgram)

    def is_pin_correct(self,attempts):
        '''
        This would be where the bank API would confirm whether or not the PIN is correct for the card number.
        '''
        # return(authorization_from_bank_API(PIN,cardNumber))
        assert hasattr(self,"cardNumber"), "Error, card number must be retrieved first. Make sure the card is inserted."
        assert self.cardInserted==True, "Error, card is not inserted. Please insert card first."

        if self.cardNumber not in TOTAL_ACCOUNTS:
            print("Not a valid account number...\nHave a nice day!")
        elif TOTAL_ACCOUNTS[self.cardNumber]["PIN"]==self.PIN:
            print("\n" + "*"*60)
            print("Welcome " + TOTAL_ACCOUNTS[self.cardNumber]["MEMBER_NAME"] + "!")
            print("\n" + "*"*60)
            self.accountInfo = TOTAL_ACCOUNTS[self.cardNumber]["ACCOUNTS"]
            return(True)
        else:
            print("\n" + "*"*60)
            if attempts<3:
                print("Incorrect PIN. Please Try Again.")
            else:
                print("Incorrect PIN.\nExceeded Maximum Attempts")
            print("\n" + "*"*60)
            return(False)

    def choose_an_account(self):
        accountNames = list(self.accountInfo.keys())
        validChoices = [str(i+1) for i in range(len(accountNames))]
        validResponse=False
        exitProgram=False
        selectedAccount=None
        while validResponse == False:
            print("*"*60 + "\n")
            print("Available Accounts:\n")
            print("*"*60)
            for i in range(len(accountNames)):
                print(str(i+1) + " - " + accountNames[i])
            print("[Exit] ")
            print("*"*60 + "\n")
            accountChoice = input("Enter Choice: ")
            print("\n")

            if accountChoice.capitalize() in validChoices:
                selectedAccount = accountNames[int(accountChoice)-1]
                validResponse=True
            elif accountChoice.capitalize()=="Exit":
                exitProgram = True
                self.card_removed()
                break
            else:
                print("Invalid Choice. Please enter Again.\n")
        return(selectedAccount,exitProgram)

    def choose_an_action(self,selectedAccount):
        validResponse=False
        menuChoice=None
        exitProgram=False
        backToMainMenu=False
        while validResponse == False:
            print("*"*60 + "\n")
            print(
                "Available Actions for "
                + selectedAccount
                + ":\n"
            )
            print("*"*60)
            print("1 - Check Balance")
            print("2 - Make Deposit")
            print("3 - Make Withdrawal")
            print("[Menu]")
            print("[Exit] ")
            print("*"*60 + "\n")
            menuChoice = input("Enter Choice: ")
            print("\n")

            if menuChoice.capitalize() in ["1","2","3"]:
                validResponse=True
            elif menuChoice.capitalize()=="Exit":
                exitProgram = True
                yourATM.card_removed()
                break
            elif menuChoice.capitalize()=="Menu":
                backToMainMenu=True
                break
            else:
                print("Invalid Choice. Please enter Again.")
        return(menuChoice,backToMainMenu,exitProgram)

    def check_balance(self,account):
        assert hasattr(self,"accountInfo"), "Error! Account Information has not been returned. Check authorization."
        assert account in self.accountInfo, "This account does not have " + account + "."
        print("*"*60 + "\n")
        print(
            "Available Balance in "
            + account
            + ": $"
            + str(self.accountInfo[account])
            + "\n"
        )
        print("*"*60 + "\n")

    def return_balance(self,account):
        assert hasattr(self,"accountInfo"), "Error! Account Information has not been returned. Check authorization."
        assert account in self.accountInfo, "This account does not have " + account + "."
        return(self.accountInfo[account])

    def input_deposit(self):
        '''
        To be replaced by the ATM program that determines the deposit amount.
        '''
        validResponse=False
        depositAmount = 0
        backToMainMenu = False
        exitProgram = False
        while validResponse == False:
            print("*"*60 + "\n")
            depositAmount = input("How much would you like to deposit: ")
            print("\n" + "*"*60 + "\n")
            if "-" in depositAmount:
                print("Invalid Amount! Only positive values.\n")
                validResponse=False
            elif depositAmount.capitalize()=="Exit":
                exitProgram = True
                yourATM.card_removed()
                break
            elif depositAmount.capitalize()=="Menu":
                backToMainMenu=True
                break
            elif depositAmount.isdigit():
                validResponse=True
        return(depositAmount,backToMainMenu,exitProgram)

    def make_deposit(self,account,amount):
        '''
        Again, this would need to pull the current amount from the account and add whatever was input into the system. For this exercise the amount will be manually added.
        '''
        assert hasattr(self,"accountInfo"), "Error! Account Information has not been returned. Check authorization."
        assert account in self.accountInfo, "This account does not have " + account + "."

        self.accountInfo[account]+=amount

    def input_withdrawal(self,account):
        validResponse=False
        availableBalance = self.return_balance(account)
        withdrawalAmount=0
        backToMainMenu=False
        exitProgram=False
        while validResponse == False:
            print("*"*60 + "\n")
            withdrawalAmount = input(
                "How much would you like to withdraw ($"
                + str(availableBalance)
                + " Available): ")
            print("\n" + "*"*60 + "\n")
            if "-" in withdrawalAmount:
                print("Invalid Amount! Only positive values.\n")
                validResponse=False
            elif withdrawalAmount.capitalize()=="Exit":
                exitProgram = True
                self.card_removed()
                break
            elif withdrawalAmount.capitalize()=="Menu":
                backToMainMenu=True
                break
            elif withdrawalAmount.isdigit():
                if int(withdrawalAmount)<=availableBalance:
                    validResponse=True
                else:
                    print("Insufficient Funds. Please enter a valid amount.\n")
        return(withdrawalAmount,backToMainMenu,exitProgram)

    def make_withdrawal(self,account,amount):
        '''
        Again, this would need to pull the current amount from the account and add whatever was input into the system. For this exercise the amount will be manually added.
        '''
        assert hasattr(self,"accountInfo"), "Error! Account Information has not been returned. Check authorization."
        assert account in self.accountInfo, "This account does not have " + account + "."

        self.accountInfo[account]-=amount

    def return_to_main_menu(self):
        validResponse = False
        exitProgram=False
        stayInMenu=False
        while validResponse == False:
            backToMainMenu = input("Return to Main Menu? ([Y]/N): ")
            print("\n")
            if backToMainMenu.capitalize() not in ["Y","N","Exit",""]:
                validResponse = False
                print("Invalid Response. Please Try Again.\n")
            elif backToMainMenu.capitalize()=="Exit":
                exitProgram = True
                self.card_removed()
                break;
            else:
                if backToMainMenu.capitalize()=="N":
                    stayInMenu=False
                    exitProgram = True
                    yourATM.card_removed()
                    break;

                else:
                    stayInMenu=True
                validResponse=True
        return(stayInMenu,exitProgram)

if __name__ == "__main__":
    exitProgram = False
    yourATM = ATM()
    # Start Loop that can be Exited with 'Exit' command.
    while exitProgram == False:
        '''
        Insert card or EXIT.
        This will be replaced by the ATMs ability to detect when a card is inserted.
        '''
        cardInserted,exitProgram = yourATM.detect_card()

        pinAttempts = 1 # Number of attempts for PIN (3 Max.)
        if cardInserted==True:
            yourATM.card_inserted() # card is recognized by machine
            yourATM.get_card_number() # card/account number returned via magnetic strip or chip

            auth = False
            while auth==False:
                '''
                Input Pin or EXIT.
                To be replaced by the ATM's internal touchscreen input.
                '''
                exitProgram = yourATM.input_pin() # input pin or EXIT
                if exitProgram==True:
                    break

                auth = yourATM.is_pin_correct(pinAttempts) # check if PIN matches the one provided by the Bank API. Returns True or False, not the correct PIN.

                if auth==False:
                    pinAttempts+=1
                if pinAttempts>3:
                    yourATM.card_removed() # remove card from ATM
                    exitProgram = True
                    break;

            if auth==True:
                # list of account names and their corresponding touchscreen number assignments.
                accountNames = list(yourATM.accountInfo.keys())
                validChoices = [str(i+1) for i in range(len(accountNames))]

                # Loop to stay in menu until customer wishes to EXIT or leave the MENU.
                stayInMenu = True
                backToMainMenu = False
                while stayInMenu == True:
                    '''
                    Choose and Account or EXIT.
                    To be replaced by touchscreen input.
                    '''
                    selectedAccount,exitProgram = yourATM.choose_an_account()
                    if exitProgram==True:
                        break

                    '''
                    Choose and Action or choose to EXIT or return to MENU.
                    '''
                    menuChoice,backToMainMenu,exitProgam = \
                        yourATM.choose_an_action(selectedAccount)
                    if exitProgram==True:
                        break

                    if menuChoice == "1":
                        """
                        Prints the account balance on command line. To be replaced by a print statement to touchscreen.
                        """
                        yourATM.check_balance(selectedAccount)

                    elif menuChoice == "2":
                        """
                        Input deposit amount or choose to EXIT or return to MENU. This will be replaced by the interal check and cash deposit software that determine the correct deposit amount.
                        """
                        depositAmount,backToMainMenu,exitProgram = \
                            yourATM.input_deposit()

                        if exitProgram==True:
                            break
                        elif backToMainMenu==False:
                            # deposit the money to the correct account.
                            yourATM.make_deposit(
                                selectedAccount,
                                int(depositAmount)
                            )
                            yourATM.check_balance(selectedAccount)

                    elif menuChoice == "3":
                        """
                        Input withdrawal amount or choose to EXIT or return to MENU. This checks to ensure that the amount does not exceed the account balance.
                        """
                        withdrawalAmount,backToMainMenu,exitProgram = \
                            yourATM.input_withdrawal(selectedAccount)

                        if exitProgram==True:
                            break
                        elif backToMainMenu==False:
                            # withdraw the money to the correct account.
                            yourATM.make_withdrawal(
                                selectedAccount,
                                int(withdrawalAmount)
                            )
                            yourATM.check_balance(selectedAccount)

                    if exitProgram==True:
                        break
                    elif backToMainMenu==False:
                        """
                        Determine if the user wished to return to the main menu or exit the ATM portal.
                        """
                        stayInMenu,exitProgram = yourATM.return_to_main_menu()
                        if exitProgram==True:
                            break
