from flask import render_template, redirect,url_for,flash,abort,request
from ..models import User
from .forms import RegistrationForm,LoginForm
from . import auth
from .. import db,bcrypt
from flask_login  import login_user, logout_user, login_required, current_user

@auth.route('/register', methods = ["GET","POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email=form.email.data, password = hashed_password)

        user.save_user()
        flash(f"Account Created for {form.username.data}!","success")
        
        return redirect(url_for("auth.login"))
    return render_template('auth/register.html', form = form)


@auth.route('/login', methods = ["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            
            return redirect(url_for('main.index'))
        else:
            flash("Login Unsuccessful.Check Email and Password")
        
        
    
    return render_template('auth/login.html', form = form)

@auth.route('/logout')
def logout():
    logout_user()
    
    return redirect(url_for('main.index'))