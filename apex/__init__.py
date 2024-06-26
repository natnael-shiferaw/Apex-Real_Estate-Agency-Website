from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from apex.config import Config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'agents.login'
login_manager.login_message_category = 'info'
mail = Mail()

def create_app(config_class=Config):

  app = Flask(__name__)
  app.config.from_object(Config)

  db.init_app(app)
  bcrypt.init_app(app)
  login_manager.init_app(app)
  mail.init_app(app)

  from apex.main.routes import main
  from apex.agents.routes import agents
  from apex.api.routes import api

  app.register_blueprint(main)
  app.register_blueprint(agents)
  app.register_blueprint(api)

  # Create database
  with app.app_context():
      db.create_all()

  return app

