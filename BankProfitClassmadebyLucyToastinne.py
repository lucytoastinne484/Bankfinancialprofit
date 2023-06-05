# BankProfitClassmadebyLucyToastinne.py

class Bank():
	def __init__(self):
		print()

		# Ask if the user already has money on its bank account
		initial_bank_deposit = int(input("If you have made a deposit before please type it (can be zero):\n"))

		print()

		# Ask for a second deposit
		second_deposit = 0

		while second_deposit == 0:
			second_deposit = int(input("Type a value for a second deposit (a decimal is also valid):\n"))

		if initial_bank_deposit <= 0:
			print()
			print("The deposit will be zero to make the operation.")

		total_deposit = initial_bank_deposit + second_deposit

		print()

		# Define the percentage value to calculate the profit
		percentage_value = 101

		# Limit the percentage value between 0 and 100
		while percentage_value not in range(0, 100 + 1):
			percentage_value = int(input("Type a percentage without decimal houses (a value between 100 and 0):\n"))

		# Define the CDI formula
		cdi_formula = percentage_value / 100

		print()

		# Ask for how many months the money stays on the bank account
		months = int(input("How many months your money is going to stay in the bank before withdrawing it:\n"))

		# Calculate the monthly format (total deposit multiplied by the CDI formula)
		cdi_monthly_profit = int(total_deposit * cdi_formula)

		# Add the profit to the total money
		total_profit_per_month = int(cdi_monthly_profit + total_deposit)

		# Show money on the bank
		print()
		print("Money on bank:")
		print(self.Format_Number(total_deposit))
		print()

		# Show the CDI monthly profit
		print("CDI monthly profit:")
		print(self.Format_Number(cdi_monthly_profit))
		print()

		# Show the total profit on one month
		print("Total profit (on one month):")
		print(self.Format_Number(total_profit_per_month))

		# If the months are not zero, show the profit in the number of months
		if months not in [0, 1]:
			print()
			print("Profit in {} months".format(months) + ":")
			print(self.Format_Number(months * total_profit_per_month))

	def Format_Number(self, number):
		return "{:,}".format(number).replace(",", ".")

Bank()