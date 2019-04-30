from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet,configure_uploads,IMAGES

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)
bcrypt = Bcrypt()
# mail = Mail()

db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    
    # initializing flask extensions
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    bcrypt.init_app(app)
    # mail.init_app(app)
    
    # Creating app configurations
    app.config.from_object(config_options[config_name])
    
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    
    # configure UploadSet
    configure_uploads(app,photos)
    
    from .requests import configure_request
    configure_request(app)
    
    return app
