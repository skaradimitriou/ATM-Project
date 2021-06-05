class Withdrawal():

    userBalance = 0

    def __init__(self):
        print('You chose Withdrawal option')

    def getAmount(self, userBalance):
        print('')
        try:
            withdrawalAmount = float(input('What is the amount that you would like to withdraw?'))

            if userBalance >= withdrawalAmount:
                userBalance -= withdrawalAmount
                self.userBalance = userBalance
                print('Your account balance after this action is {0:,.2f}€'.format(self.userBalance))
            else:
                print('Your account balance is not enough to make this action.')
        except:
            print('Your number should be divided using a dot(.) instead of comma (e.g 100.50€)')


    def updateBalance(self):
        return self.userBalance