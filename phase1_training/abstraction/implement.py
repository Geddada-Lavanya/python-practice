from abstract import *
class debit(payment):
    def pay_method(self):
        print("Amount paid through debit card")
class credit(payment):
    def pay_method(self):
        print("Amount paid through credit card")