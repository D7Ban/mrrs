from flask import Blueprint, redirect
from flask import render_template, session
from flask import request
from ..utils.db import SQLHelper
import time
from .enter import wrapper
home = Blueprint('account', __name__, template_folder='templates')



@home.route('/lin',methods=['GET',] )
def lin():
    return render_template('lin.html')

@home.route('/', methods=['GET', "POST"])
@wrapper
def index():
    print(request)
    user = session.get('user')
    if request.method == 'GET':
        selected_date = request.args.get('date', None)

        if not selected_date:
            selected_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))

        periods = SQLHelper.fetch_all('select * from periods', [])
        rooms = SQLHelper.fetch_all('select * from conference_rooms', [])
        reservations = SQLHelper.fetch_all('select * from reservations where reservation_date = "%s"' % selected_date,
                                           [])
        reservation_list = []
        for reservation in reservations:
            reservation_list.append((reservation[1],reservation[3]))

        # print('user', user)
        # print(periods)
        # print(rooms)
        print(reservations)
    else:
        selected_date = request.form.get('date', None)
        room_id = request.form.get('room_id', None)
        period_id = request.form.get('period_id', None)
        print(selected_date, room_id, period_id)
        try:
            SQLHelper.execute("insert into reservations(conference_room_id,reservation_date,period_id)values(%s,%s,%s)",
                              (room_id, selected_date, period_id))
        except Exception as e:
            pass
        redirect_url = '/?date=%s' % selected_date
        return redirect_url

    return render_template('index.html', user=user, selected_date=selected_date, periods=periods, rooms=rooms,
                           reservations=reservations,reservation_list=reservation_list)
