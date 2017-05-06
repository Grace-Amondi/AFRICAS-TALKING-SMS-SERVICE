from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


from config import config


bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

    # attach routes and custom pages here
    
    from ussd import ussd as ussd_blueprint
    app.register_blueprint(ussd_blueprint, url_prefix='/ussd')

    return app