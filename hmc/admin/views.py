# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, abort
#from flask_login import login_required
from jinja2 import TemplateNotFound
from flask.blueprints import Blueprint

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/')
def index():
    return render_template('admin/index.html')
