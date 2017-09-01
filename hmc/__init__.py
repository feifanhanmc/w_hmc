# -*- coding: utf-8 -*-
from flask import Flask

from hmc.admin.views import admin_bp
from hmc.home.views import home_bp

from database import db
# from hmc.admin import models
from hmc.home import models


def create_app():
    #Create app and load configurations
    app = Flask(__name__, instance_relative_config=True)
    
    # Create modules(一定要在config之前注册蓝图)
    app.register_blueprint(home_bp, url_prefix='')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    #config    
    # app.config.from_object('config')
    app.config.from_pyfile('config.py')

    # Create database
    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    return app
