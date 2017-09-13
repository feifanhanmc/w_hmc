# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, g, request, session, flash, redirect, url_for
from hmc.models import User
from hmc.database import db

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
        
        if User.query.filter_by(username=username).count():
            flash('Username already exist')
            return redirect(url_for('home.reg'))
        else:
            u = User(username=username, password_md5=password_md5, nickname=nickname)
            db.session.add(u)
            db.session.commit()
            session['logged_in'] = True
            session['nickname'] = nickname
            flash('You were logged in')
            return redirect(url_for('home.index'))
        return redirect(url_for('home.index'))
    else:
        return render_template('home/reg.html')

@home_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_md5 = request.form['password_md5']
        u = User.query.filter_by(username=username, password_md5=password_md5).first()
        if u:
            session['logged_in'] = True
            session['nickname'] = u.nickname
            flash('You were logged in')
            return redirect(url_for('home.index'))
        else:
            flash('Login failed')
            return redirect(url_for('home.login'))
    else:
        return render_template('home/login.html')

@home_bp.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('nickname', None)
    return redirect(url_for('home.index'))

@home_bp.route('/test')
def test():
    return 'test'

@home_bp.route('/test2')
def test2():
    return 'test2'