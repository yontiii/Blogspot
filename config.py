import os

class Config:
    
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:john123@localhost/blog'
  SECRET_KEY = os.environ.get('SECRET_KEY')
  UPLOADED_PHOTOS_DEST = 'app/static/photos'
  
 
  
  
class ProdConfig(Config):
    
    pass

class DevConfig(Config):

    DEBUG = True
   
   
config_options = {
    'development':DevConfig,
    'production':ProdConfig
} 