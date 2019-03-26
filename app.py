from flask import Flask, render_template, request, url_for, session, redirect
from account import Account, app


@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		account_number = request.form['account-number']
		pin = request.form['pin']

		account = Account.query.filter_by(account_number=account_number).first()
		if account.pin == int(pin):
			return redirect( url_for('menu', account_number=account_number) )

	return render_template('index.html')


@app.route('/menu/<int:account_number>/')
def menu(account_number):
	account = Account.query.filter_by(account_number=account_number).first()
	return render_template('menu.html', balance=account.balance)