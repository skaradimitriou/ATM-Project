class InstructionsHelper:

    # This is the Helper Class. This is the class that contains every console
    # init message for the user and helps him navigate

    def printWelcomeMessage(self):
        print()
        print('--- Welcome to the ATM Project --')
        print('How can we help you with today?')

    def printInstructions(self):
            print('1. Check Balance')
            print('2. Deposit')
            print('3. Withdrawal')
            print('4. Exit')

    def printExitMessage(self):
       print('You have been logged out successfully')
