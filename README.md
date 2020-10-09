<p align=center>
    <img src="https://www.pinclipart.com/picdir/big/390-3905072_atm-png-graphic-design-clipart.png">
</p>
</br>
<h1 align="center"> ATM Controller</h1>
<h2 align="center">A simple controller for a hypothetical ATM machine.</h2>
<h3 align="center">Written by Daniel A. Hagen on 10/07/2020</h3>

<p align="center">
    <a href="https://travis-ci.com/danhagen/atm-controller">
        <img src="https://travis-ci.com/danhagen/atm-controller.svg?branch=main" alt="Build Status"
    </a>
    <a href="https://www.python.org/dev/peps/pep-0008/">
        <img src="https://img.shields.io/badge/code%20style-pep8-green.svg" alt="PEP8">
    </a>
    <a href="https://coveralls.io/github/danhagen/atm-controller?branch=master&service=github">
        <img src="https://coveralls.io/repos/github/danhagen/atm-controller/badge.svg?branch=master&service=github" alt="Coverage Status">
    </a>
</p>

### Installation from GitHub
```
git clone https://github.com/danhagen/atm-controller.git && cd atm-controller
pip install -r requirements.txt
pip install .
```

### Working the ATM
In order to run the ATM, simply navigate to the repository folder via the command-line, as described above, and type in the following code:

```
python3 atm.py
```

This will begin a series of prompts, that will be replaced by specific ATM input/output sources when implemented, that will guide the user to the "Bank Account" information.

To do this, one must first "Insert your Card" by simply entering `Y` in the command prompt. This will then ask the user to input their PIN (which in this example case is `9999`).

```
Insert your card? (Y/N/[Exit]): Y
Enter your PIN: 9999
```

The "inserted" card automatically signals the program to find the account number that corresponds to it, and then uses the PIN to authenticate the user. This will be replaced by the Bank API that will safely relay whether or not a PIN was accepted. Currently, a local `TOTAL_ACCOUNTS` `dict` variable contains all of the sensitive information, so that will be the first to go! If the user fails to enter the proper PIN 3 times, the program will exit automatically.

```
Insert your card? (Y/N/[Exit]): Y
Enter your PIN: 9996

************************************************************
Incorrect PIN. Please Try Again.

************************************************************
Enter your PIN: 9997

************************************************************
Incorrect PIN. Please Try Again.

************************************************************
Enter your PIN: 9998

************************************************************
Incorrect PIN.
Exceeded Maximum Attempts

************************************************************
```

When the right PIN is entered, the user is greeted and presented with a Menu screen to choose from. (Note that invalid account numbers and invalid PINs are rejected with warnings; i.e., too short, invalid characters, etc.)

```
Insert your card? (Y/N/[Exit]): Y
Enter your PIN: 9999

************************************************************
Welcome Daniel Hagen!

************************************************************
************************************************************

Available Accounts:

************************************************************
1 - Savings Account
2 - Checking Account
3 - Carl's College Fund
[Exit]
************************************************************
```

Navigating to these subaccounts, you are again presented with a menu.

```
Available Accounts:

************************************************************
1 - Savings Account
2 - Checking Account
3 - Carl's College Fund
[Exit]
************************************************************

Enter Choice: 3


************************************************************

Available Actions for Carl's College Fund:

************************************************************
1 - Check Balance
2 - Make Deposit
3 - Make Withdrawal
[Menu]
[Exit]
************************************************************

Enter Choice:
```
Note that at any time, the user can go back to the Menu by entering `Menu` or can exit the ATM by entering `Exit`.

The user can then check the account's balance, make a deposit, or withdraw from the account.

Let's see how much I have squirreled away for Carl so far...

```
************************************************************

Available Actions for Carl's College Fund:

************************************************************
1 - Check Balance
2 - Make Deposit
3 - Make Withdrawal
[Menu]
[Exit]
************************************************************

Enter Choice: 1


************************************************************

Available Balance in Carl's College Fund: $1

************************************************************

Return to Main Menu? ([Y]/N):
```

<b>Ouch!</b> Sorry, Carl... We will need to bump that up! To do this, I will navigate back to the Menu by entering `Y` and then make a deposit in his College Fund.

```
************************************************************

Available Actions for Carl's College Fund:

************************************************************
1 - Check Balance
2 - Make Deposit
3 - Make Withdrawal
[Menu]
[Exit]
************************************************************

Enter Choice: 2


************************************************************

How much would you like to deposit: 3000

************************************************************

************************************************************

Available Balance in Carl's College Fund: $3001

************************************************************

Return to Main Menu? ([Y]/N):
```

There! That's more like it. Note that the account balance is automatically presented whenever the account is modified (i.e., deposits or withdrawals are made).

Speaking of withdrawals, they are just as simple. Just navigate to the menu, choose the account, and input the desired amount you wish to withdraw. The program will not let you withdraw more than you have in the account, and will display the balance next to the prompt for convenience.

```
************************************************************

Available Actions for Savings Account:

************************************************************
1 - Check Balance
2 - Make Deposit
3 - Make Withdrawal
[Menu]
[Exit]
************************************************************

Enter Choice: 3


************************************************************

How much would you like to withdraw ($500 Available): 300

************************************************************

************************************************************

Available Balance in Savings Account: $200

************************************************************

Return to Main Menu? ([Y]/N):
```

To Exit, either select `N` from the `Return to Main Menu` prompt, or type `Exit` at any time. Lastly, any time an account is altered, when the user exits the program, their account information is updated in the (for now local) `TOTAL_ACCOUNTS` `dict`.
