
# class bank

class Bank:
    # initializing the constractor
    def __init__(self,balance,bank_user):
        self._balance = balance
        self.bank_user = bank_user


    def user_withdraw(self ,amount):

        if amount > self._balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew R{amount}. New balance: R{self._balance:.2f}")

    def user_deposite(self,dp_amout):
        
        if dp_amout > 0 :
            self._balance +=dp_amout

            print(f'Deposited: R{dp_amout:.2f}, New Balance: R{self._balance:.2f}')
        else:
            print(f'{self.bank_user} deposite must be above 0')


    def show_balance(self):

        return f'Balance: R{self._balance:.2f}'


user_name = input('Username: ')

bank = Bank(balance=0 ,bank_user=user_name)

while True:
    print('-----------------------------------------------------------')
    bank_decision = input('1.Withdraw, 2.Deposite 3.Balance: ').lower()
    print('-----------------------------------------------------------')
    print()
    if bank_decision == '1':

        withdraw_amount = int(input('Witdraw amount: '))
        bank.user_withdraw(withdraw_amount)
    elif bank_decision == '2':

        deposit_amount = int(input('Deposite: '))
        bank.user_deposite(deposit_amount)
    elif bank_decision =='3':

        print(bank.show_balance())
        print()
    else:
        print(f'{bank.bank_user},you entered wrong choice')
        break


    exit_program = input('Exit ?(y/n): ').lower()
    if exit_program == 'y':
        exit()