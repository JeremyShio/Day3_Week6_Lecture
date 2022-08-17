from flask import render_template, redirect, url_for

from app import app

from app.forms import RegisterForm

from app.models import Address


@app.route('/')
def index():
    # return render_template('index.html')
    return render_template('index.html')


@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        phone_number = form.phone_number.data
        address = form.address.data
        new_address = Address(name = name, phone_number = phone_number, address = address)
        print(new_address)
        return redirect(url_for('index.html'))
        
    return render_template('register.html', form = form)