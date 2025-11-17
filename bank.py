class Customer:
    last_id = 0

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return f'Customer[{self.id}, {self.firstname}, {self.lastname}]'

class Account:
    last_id = 1000
    yearly_interest_rate = 0.02  #TODO - will be used to update the interest rate

    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.id = Account.last_id
        self._balance = 0.0

    def deposit(self, amount):
        #TODO - as part of the home assignment please extend this method
        if amount <= 0:
            raise InvalidAmountException('Cannot deposit less or equal to 0')
            #print('Cannot deposit less or equal to 0')
        else:
            self._balance = self._balance + amount

    def charge(self, amount):
        #TODO - as part of the home assignment please extend this method
        self._balance = self._balance - amount

    def __repr__(self):
        return f'Account[{self.id}, {self.customer.lastname}, {self._balance}]'


class Bank:
    def __init__(self, name):
        self.name = name
        self.customer_list = []
        self.account_list = []

    def create_customer(self, firstname, lastname):
        c = Customer(firstname, lastname)
        self.customer_list.append(c)
        return c

    def create_account(self, customer):
        a = Account(customer)
        self.account_list.append(a)
        return a

    def transfer_money(self, from_account_id, to_account_id, amount):
        # TODO - as part of the home assignment please implement this method - as names suggest the input parameters are
        # ids of the accounts to transfer money from and to and amount to transfer. You may need a helper method to find
        # those accounts based on their ids.
        pass

    def run_daily_interest_updater(self):
        # TODO - as part of the home assignment please implement this method
        pass

    def __repr__(self):
        return f'Bank[{self.customer_list}, {self.account_list}]'

class BankException(Exception):
    pass

class InsufficientFundsException(BankException):
    pass

class InvalidAmountException(BankException):
    pass



bank = Bank('SGH Bank')
c1 = bank.create_customer('John', 'Smith')
a1 = bank.create_account(c1)

try:
    a = 'gsgsg' + 344
    a1.deposit(-500)
    print(bank)
    a1.charge(200)
    print(bank)
except InvalidAmountException as be:
    print(be)
    print('handled by InvAmount')
except BankException as be:
    print(be)
except Exception as be:
    print(be)
    print('handled by exception')

print('continuing execution')

