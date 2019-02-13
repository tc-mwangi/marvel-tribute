import os

class Config:
    MARVEL_API_BASE_URL='https://gateway.marvel.com:443/v1/public/{}?apikey={}&hash={}'
    MARVEL_API_KEY = os.environ.get('MARVEL_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_TRACK_MODIFICATIONS=False
    UPLOADED_PHOTOS_DEST='app/static/images/avatars'

    # email configurations
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    SUBJECT_PREFIX='Marvel-Tribune'
    SENDER_EMAIL='saber.dangermouse@gmail.com'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URL=os.environ.get('DATABASE_URL')
    pass


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://saberdanger:cartoonroyalty@localhost/marvel_app_test'
    

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://saberdanger:cartoonroyalty@localhost/marvel_app'
    DEBUG =True


config_options={
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}

