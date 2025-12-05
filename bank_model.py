from sqlalchemy import Column, Integer, String, ForeignKey, Float, create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()



class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(80))
    accounts = relationship('Account', back_populates="customer")
    fk_bank_id = Column(Integer, ForeignKey('bank.id'), index=True, nullable=False)
    bank = relationship('Bank', lazy='select', back_populates='customers')
    #last_id = 0
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        #Customer.last_id += 1
        #self.id = Customer.last_id

    def __repr__(self):
        return f'Cust[{self.id}, {self.first_name}, {self.last_name}]'

class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Float)
    fk_customer_id = Column(Integer, ForeignKey(Customer.id), index=True, nullable=False)
    customer = relationship(Customer, back_populates='accounts')
    type = Column(String(20))
    fk_bank_id = Column(Integer, ForeignKey('bank.id'), index=True, nullable=False)
    bank = relationship('Bank', lazy='select', back_populates='accounts')
    #last_id = 1000
    yearly_interest_rate = 0.02  # TODO - will be used to update the interest rate

    def __init__(self, customer):
        self.customer = customer
        #Account.last_id += 1
        #self.id = Account.last_id
        self.balance = 0

    def deposit(self, amount):
        #TODO - as part of the home assignment please extend this method
        if amount <= 0:
            print('Invalid amount.')
            raise InvalidAmountException(f'Invalid amount: {amount}')
        else:
            self.balance += amount

    def charge(self, amount):
        #TODO - as part of the home assignment please extend this method
        if amount > self.balance:
            print('Insufficient funds.')
            raise InsufficientFundsException(f'Insufficient funds: {amount}')
        else:
            self.balance -= amount

    def __repr__(self):
        return f'Acc[{self.id}, {self.customer.last_name}, {self.balance}]'

class Bank(Base):
    __tablename__ = 'bank'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    customers = relationship(Customer, cascade='all, delete-orphan, delete', lazy='select')
    accounts = relationship(Account, cascade='all, delete-orphan, delete', lazy='select')

    def __init__(self, name):
        self.name = name
        #self.customer_list = []
        #self.account_list = []

    def create_customer(self, first_name, last_name, email):
        c = Customer(first_name, last_name, email)
        c.fk_bank_id = self.id
        #self.customer_list.append(c)
        return c

    def create_account(self, customer):
        a = Account(customer)
        a.fk_bank_id = self.id
        #self.account_list.append(a)
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
        return f'Bank[{self.name}: \n{self.customers}\n{self.accounts}]'

class BankException(Exception):
    pass

class InsufficientFundsException(BankException):
    pass

class InvalidAmountException(BankException):
    pass



class DBSession:
    current_db_session = None

    def engine(self):
        url = 'sqlite:///bank.db'
        return create_engine(url, echo=True)


    def db_session(self):
        """Opens a new database connection if there is none yet for the
        current application context.
        """
        if not DBSession.current_db_session:
            Session = sessionmaker(bind=self.engine(), autocommit=False, autoflush=False)
            current_db_session = Session()
        return current_db_session

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    db_session = DBSession()
    Base.metadata.create_all(bind=db_session.engine())
    pass


if __name__ == '__main__':
    bank = Bank('SGH Bank')

    c1 = bank.create_customer('John', 'Smith')
    a1 = bank.create_account(c1)

    try:
        #a = 500
        #s = 'avcv' + a
        a1.deposit(-500)
        a1.charge(300)
    except InsufficientFundsException as ife:
        print(ife)
    except InvalidAmountException as iae:
        print(iae)
    # except Exception as e:
    #     print(e)

    a2 = bank.create_account(c1)
    print(bank)
    c2 = bank.create_customer('Anne', 'Brown')
    a3 = bank.create_account(c2)
    print('--------------')
    print(bank)

    #TODO:
    # Add deposit and charge method to account - they should have a
    # parameter: amount