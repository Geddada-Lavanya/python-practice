class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,withdraw_amt):
        if withdraw_amt <= self.__balance:
            self.__balance-=withdraw_amt
            print("amount withdraw {}".format(withdraw_amt))
        else:
            print("Insufficient funds")
    def get(self):
        return self.__balance
obj=BankAccount(123,2000)
obj.deposit(1000)
print(obj.get())
obj.withdraw(500)
print(obj.get())