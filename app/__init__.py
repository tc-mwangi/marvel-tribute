from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail
# from flask_simplemde import SimpleMDE

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

# simple = SimpleMDE()

bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos', IMAGES)
mail = Mail()

# application factory
def create_app(config_name):

    # initialize app
    app = Flask(__name__)

    #create app configurations
    app.config.from_object(config_options[config_name])
    # config_options[config_name].init_app(app)

    # initialize extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    # simple.init_app(app)

    #register blueprints
    # from .main import main as main_blueprint
    # app.register_bluepirnt(main_blueprint)

    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint, url_prefix = '/auth')

    # # settings configurations
    # from .requests import configure_request
    # configure_request(app)

    # configure UploadSet
    configure_uploads(app, photos)

    return app
