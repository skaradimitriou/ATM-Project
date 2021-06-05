# trying to implement an ATM Project
from balance.Balance import Balance
from deposit.Deposit import Deposit
from withdrawal.Withdrawal import Withdrawal

userBalance = 5000

def printInstructions():
    print('--- Welcome to the ATM Project --')
    print()
    print('How can we help you with today?')
    print('1. Check Balance')
    print('2. Deposit')
    print('3. Withdrawal')


printInstructions()
userChoice = int(input('Give your option: '))

if userChoice == 1:
    balance = Balance()
    balance.printBalanceInfo(userBalance)
elif userChoice == 2:
    deposit = Deposit()
    deposit.addAmount(userBalance)
    userBalance = deposit.updateBalance()
elif userChoice == 3:
    withdrawal = Withdrawal()
    withdrawal.getAmount(userBalance)
    userBalance = withdrawal.updateBalance()
else:
    print('You entered an error input choice.')
    # userInput = int(input('Can we help you with something else?'))
    # printInstructions()
    # userChoice = int(input('Give your option: '))