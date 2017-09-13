# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, g, redirect, url_for, request, session, flash
from functools import wraps
from hmc.models import BDUser, BDRecord
from hmc.database import db
import uuid
import datetime
from sqlalchemy import desc

hmk_bp = Blueprint('hmk', __name__)

@hmk_bp.route('/reg/', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        username = request.form['username']
        password_md5 = request.form['password_md5']
        nickname = request.form['nickname']
        comname = request.form['comname']
        if BDUser.query.filter_by(username=username).count():
            flash('Username already exist')
            return redirect(url_for('hmk.reg'))
        else:
            u = BDUser(username=username, password_md5=password_md5, nickname=nickname, comname=comname)
            db.session.add(u)
            db.session.commit()
            session['logged_in'] = True
            session['username'] = username
            session['nickname'] = nickname
            session['comname'] = comname
            flash('You were logged in')
            return redirect(url_for('hmk.index'))
        return redirect(url_for('hmk.index'))
    else:
        return render_template('hmk/reg.html')
    
@hmk_bp.route('/logout/')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    session.pop('nickname', None)
    session.pop('comname', None)
    return redirect(url_for('hmk.index'))

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
#         if g.user is None:
        if not session.get('logged_in'):
            return redirect(url_for('hmk.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@hmk_bp.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_md5 = request.form['password_md5']
        u = BDUser.query.filter_by(username=username, password_md5=password_md5).first()
        if u:
            session['logged_in'] = True
            session['username'] = username
            session['nickname'] = u.nickname
            session['comname'] = u.comname
            flash('You were logged in')
            return redirect(url_for('hmk.index'))
        else:
            flash('Login failed')
            return redirect(url_for('hmk.login'))
    else:
        return render_template('hmk/login.html')
    
@hmk_bp.route('/')
@hmk_bp.route('/index/')
def index():
    return render_template('hmk/index.html')

@hmk_bp.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        merchant_name = request.form['merchant_name']
        merchant_tel = request.form['merchant_tel']
        visit_purpose = request.form['visit_purpose']
        if visit_purpose == 'wh':
            visit_purpose = '维护'
        elif visit_purpose == 'qy':
            visit_purpose = '签约'
        else:
            visit_purpose = '挖掘需求'
        visit_result = request.form['visit_result']
        visit_time = request.form['visit_time']
        bd_username=session.get('username')
        record_id = str(uuid.uuid1())
        record = BDRecord(record_id=record_id, bd_username=bd_username, merchant_name=merchant_name, merchant_tel=merchant_tel, \
                          visit_purpose=visit_purpose, visit_result=visit_result, visit_time=visit_time)
        db.session.add(record)
        db.session.commit()
        flash('Add succeed.')
        return redirect(url_for('hmk.add'))    
    else:
        return render_template('hmk/add.html')

@hmk_bp.route('/view/')
@login_required
def view():
    limit = int(request.values.get('limit', default=7))    #默认获取7天的数据
    print limit
    if limit in [3, 7]:
        some_days_ago = str((datetime.datetime.now() - datetime.timedelta(days = limit)).strftime("%Y-%m-%d"))
        records = BDRecord.query.filter_by(bd_username=session.get('username')).filter(BDRecord.visit_time >= some_days_ago).order_by(desc(BDRecord.visit_time)).all()
    else:   #返回所有数据
        records = BDRecord.query.filter_by(bd_username=session.get('username')).order_by(desc(BDRecord.visit_time)).all()
    return render_template('hmk/view.html', records=records)



