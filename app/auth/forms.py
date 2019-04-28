from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField
from wtforms.validators import Required,Email,EqualTo
from .. models import User

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        
        if user:
            raise ValidationError("A User with that username exists! ")
        
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        
        if user:
            raise ValidationError("That Email is taken!")
    
    
class LoginForm(FlaskForm):
    email = StringField('Enter Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
    
