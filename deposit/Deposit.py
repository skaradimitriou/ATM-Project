
class Deposit:

    userBalance = 0.0

    def __init__(self):
        print('You chose Deposit option')

    def addAmount(self, amount):
        try:
            newAmount = float(input('Give the amount that you would like to deposit: '))
            amount += newAmount
            self.userBalance = amount
        except:
            print('Your number should be divided using a dot(.) instead of comma (e.g 100.50€)')

    def updateBalance(self):
        print('Your new balance after the Deposit is {0:,.2f}€'.format(self.userBalance))
        return self.userBalance