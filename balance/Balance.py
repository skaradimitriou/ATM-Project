# This is the balance class

class Balance:

    def __init__(self):
        print('You chose Check Balance')

    def printBalanceInfo(self, balance):
        print('Your account balance is: {0:,.2f}€.'.format(balance))
