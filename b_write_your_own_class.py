# In-Class Practice: Write your own class from scratch

class CreditCard:
    def __init__(self, account_number, credit_limit):
        self.account_number = account_number
        self.credit_limit = credit_limit
        self.balance = 0

    def get_balance(self):
        return self.balance
    
    def get_credit_limit(self):
        return self.credit_limit
    
    def set_credit_limit(self, limit):
        if limit >=100000:
            print("please don't dream")
        elif limit >= 0:
            self.credit_limit = limit
        else:
            print("Invalid Limit")

    def set_balance(self, new_balance):
        self.balance = new_balance

    def make_purchase (self, purchase_amount):
        if (purchase_amount<0):
            return(print("Invalid Purchase"))
        
        new_balance = self.balance + purchase_amount

        if (new_balance > self.credit_limit):
            return(print("Exceeding the credit limit"))
        
        self.set_balance(new_balance)


    def make_payment (self, payment_amount):
        if payment_amount < 0:
            print("Nice Try !")
        elif payment_amount > self.balance:
            self.set_balance(0)
        else:
            new_balance = self.balance - payment_amount
            self.set_balance(new_balance)
        

# Uncomment all lines to test your class once completed
my_credit_card = CreditCard(123456789, 5000)
assert my_credit_card.account_number == 123456789
assert my_credit_card.get_balance() == 0
assert my_credit_card.get_credit_limit() == 5000

my_credit_card.set_credit_limit(1000)
my_credit_card.set_credit_limit(-1)       # print error
my_credit_card.set_credit_limit(100001)   # print error
assert my_credit_card.get_credit_limit() == 1000

my_credit_card.make_purchase(900)
my_credit_card.make_purchase(-1)          # print error
my_credit_card.make_purchase(200)         # print error
assert my_credit_card.get_balance() == 900

# my_credit_card.make_payment(500)
# assert my_credit_card.get_balance() == 400

# my_credit_card.make_payment(5000)
# assert my_credit_card.get_balance() == 0

# print("All tests passed!")
