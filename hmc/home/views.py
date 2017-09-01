# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, abort, g, request, session, flash, redirect, url_for
from flask.blueprints import Blueprint
from jinja2 import TemplateNotFound


#from flask_login import login_required
home_bp = Blueprint('home', __name__)

@home_bp.route('/')
@home_bp.route('/index')
def index():
    return render_template('home/index.html')

@home_bp.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        username = request.form['username']
        password_md5 = request.form['password_md5']
        nickname = request.form['nickname']
        print username
        print password_md5
        print nickname
#         session['logged_in'] = True
        flash('You were logged in')
        return redirect(url_for('home.index'))
    else:
        return render_template('home/reg.html')

@home_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_md5 = request.form['password_md5']
        print username
        print password_md5
#         session['logged_in'] = True
        flash('You were logged in')
        return redirect(url_for('home.index'))
    else:
        return render_template('home/login.html')
