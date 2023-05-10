"""
        Create banking application

           1) Open account
                -> name
                -> opening balance

           2) Deposite amount

           3) Withdraw amount

           4) Balance

           Enter your choice : 1

Using : while loop , Conditional , Class and Object

"""

class Bank:
	def __init__(self):
		self.total_amount = 0
		self.name = ''

	def welcome(self):
		self.name = input('Please Enter your name : ')

	def print_current_balance(self):
		print('Your Current balance : {}'.format(self.total_amount))

	def deposit(self):
		self.total_amount += float(input('Hello {}, please enter amount to deposit : '.format(self.name)))
		self.print_current_balance()

	def withdraw(self):
		amount_to_withdraw = float(input('Enter amount to withdraw : '))

		if amount_to_withdraw > self.total_amount:
			print('Insufficient Balance !!')
		else:
			self.total_amount -= amount_to_withdraw

		self.print_current_balance()


if __name__=="__main__":
	bank = Bank()
	bank.welcome()

	while True:
		choice = int(input("Enter your choice : "))
		if choice == 1:
			bank.print_current_balance()
		elif choice == 2:
			bank.deposit()
		elif choice == 3:
			bank.withdraw()
            
		else:
			print('Please enter a valid input.')

