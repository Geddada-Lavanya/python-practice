from implement import *
class Main(credit,debit):
    def pay_method(self,pay_type):
        pay_type.pay_method()
obj=Main()
c=credit()
d=debit()
obj.pay_method(d)
obj.pay_method(c)

# -------------------------or-----------------------------------

# from implement import *
# def pay_method(pay_type):
#     pay_type.pay_method()
# c=credit()
# d=debit()
# pay_method(d)
# pay_method(c)