class BillPayment:

    userBalance = 0.0

    def __init__(self):
        print('You chose Bill Payment option')

    def payTheBill(self,userBalance):
        billingCompany = input('Type the company that you want to perform the payment: ')
        billingQrCode = input('Type the electronic payment code: ')

        try:
            billingAmount = float(input('Type the bill Amount (e.g 100.50€):'))
        except:
            print('Your number should be divided using a dot(.) instead of comma (e.g 100.50€)')

        if userBalance >= billingAmount:
            userBalance -= billingAmount
            self.userBalance = userBalance

            print('You paid {0}€ to {1}'.format(billingAmount, billingCompany))
            print('')
        else:
            print('The amount that you want to pay is bigger than your bank account balance.')

    def updateBalance(self):
        print('Your new balance after the Deposit is {0:,.2f}€'.format(self.userBalance))
        return self.userBalance