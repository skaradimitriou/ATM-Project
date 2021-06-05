from balance.Balance import Balance
from deposit.Deposit import Deposit
from helper.InstructionsHelper import InstructionsHelper
from withdrawal.Withdrawal import Withdrawal

userBalance = 5000.0

helper = InstructionsHelper()
helper.printWelcomeMessage()

def printExitMessage():
    print('You have been logged out successfully')

while True:
    helper.printInstructions()
    userChoice = int(input('Give your option: '))

    if userChoice == 4:
        printExitMessage()
        break
    elif userChoice == 1:
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