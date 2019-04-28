from flask import render_template, redirect,url_for,flash,abort,request
from ..models import User
from .forms import RegistrationForm,LoginForm
from . import auth
from .. import db,bcrypt
from flask_login  import login_user, logout_user, login_required 

@auth.route('/register', methods = ["GET","POST"])