import random
from account import Account, db
from faker import Faker


def fake_account_number():
	account_number = random.randint(100000, 999999)
	while Account.query.filter_by(account_number=account_number).first() !=None:
		account_number = random.randint(100000, 999999)

	return account_number

def fake_pin():
	return random.randint(100, 999)

def fake_balance():
	return random.randint(0, 1000)

def fake_account():
	return Account(
		account_number=fake_account_number(), 
		pin=fake_pin(),
		balance=fake_balance()
	)

def generate_accounts(max_n):
	db.session.query().filter_by()
	for n in range(max_n):
		account = fake_account()
		db.session.add(account)

	db.session.commit()

# generate_accounts(1000)

def add_fake_names():
	fake = Faker()
	accounts = Account.query.all()
	for account in accounts:
		account.name = fake.name()

	db.session.commit()

# add_fake_names()

def add_fake_cc():
	fake = Faker()
	for account in Account.query.all():
		account.cc = fake.credit_card_number()
		account.ccexp = fake.credit_card_expire(start='now', end='+10y',date_format="%m/%y")
		account.cvv = fake.credit_card_security_code()

	db.session.commit()

add_fake_cc()
