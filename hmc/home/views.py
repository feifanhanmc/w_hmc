# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, abort, g
from flask.blueprints import Blueprint
#from flask_login import login_required
from jinja2 import TemplateNotFound

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
@home_bp.route('/index')
def index():
    print 'WTF'
    return render_template('home/index.html')
 
@home_bp.route('/test')
def test():
    return 's'
