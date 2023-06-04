
class Bank:
    def __init__(self):
        initial_bankdeposit = float(input("If you have a deposit before please digit:"))
        deposit = float(input("Digit a value for deposit(a decimal is also valid): "))
        print( "Bank profit without initial deposit")
        if initial_bankdeposit <= 0:
            print("The deposit will be exclude to make the operation")
        else:
            print()
        total_deposit = initial_bankdeposit + deposit
        percentage_value = float(input("Digit a percentage without decimal houses (a valor between 101 and 0):"))
        cDI_formule = percentage_value/100
        month = int(input("How many months you wanna leave your money before take it:"))
        cDI_mensal_profit = total_deposit   * cDI_formule
        month_profit = cDI_mensal_profit + total_deposit 
        print(month_profit)



Bank()

        


