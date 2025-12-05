from sqlalchemy import and_, or_

from bank_model import Bank, Customer, Account, init_db, DBSession

db = DBSession().db_session()


def add_data():
    init_db()
    b = Bank('My First Bank')

    db.add(b)
    db.commit()
    c1 = b.create_customer('John', 'Brown', 'john@brown.com')
    c2 = b.create_customer('Anna', 'Smith', 'anne@smith.com')
    db.add(c1)
    db.add(c2)
    #
    a1 = b.create_account(c1)
    a2 = b.create_account(c1)
    #
    db.add(a1)
    db.add(a2)
    db.commit()

    print(b)


def get_customers():
    customers = db.query(Customer).filter(or_(Customer.last_name=='Smith', Customer.first_name.startswith('Jo'))).all()
    for c in customers:
        print(c)
        print(c.accounts)


if __name__ == '__main__':
    #add_data()
    get_customers()