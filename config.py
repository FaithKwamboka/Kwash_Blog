import os

class Config:
    '''
    General configuration parent class
    '''
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kwamboka:kwamboka@localhost/blog'
    # SQLALCHEMY_DATABASE_URI ='postgres://lrvenlerclxhff:799f028a5f2d666bcfedcebd5a0abf167f8f1a3df5f837b0a7d9aa14a40f6bf8@ec2-54-165-184-219.compute-1.amazonaws.com:5432/d3elql7m8a7919'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kwamboka:kwamboka@localhost/blog_test'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
        # uri = os.getenv('DATABASE_URL')
        # if uri and uri.startswith('postgres://'):
        #     uri = uri.replace('postgres://', 'postgresql://', 1)
            
        #     SQLALCHEMY_DATABASE_URI=uri
        


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
