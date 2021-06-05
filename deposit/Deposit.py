class Deposit:

    userBalance = 0

    def __init__(self):
        print('You chose Deposit option')

    def addAmount(self, amount):
        newAmount = float(input('Give the amount that you would like to deposit: '))
        amount += newAmount
        self.userBalance = amount
        return amount

    def updateBalance(self):
        print('Your new balance after the Deposit is {0}€'.format(self.userBalance))
        return self.userBalance