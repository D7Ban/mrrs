from flask import Blueprint
from flask import render_template, redirect
from flask import request, session,url_for
from ..utils.db import SQLHelper
from .home import *
enter = Blueprint('enter', __name__, template_folder='templates')



def wrapper(func):
    def inner(*args, **kwargs):
        if not session.get("user_info"):
            return redirect('/login')
        ret = func(*args, **kwargs)
        return ret

    return inner





@enter.route('/login', methods=['GET', "POST"])
# def login():
#     if request.method == 'GET':
#         return render_template('login.html')
#     else:
#         # print(request.form)
#         session['user'] = request.form.get('user', 'Anoy')
#         # print(session)
#         return redirect('/')
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'admin' and pwd == '123':
            session['user_info'] = user
            session['user'] = request.form.get('user', 'Anoy')
            return redirect('/')
        return render_template('login.html', error='用户名或密码错误')