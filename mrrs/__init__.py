from flask import Flask

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/static')

from .views.home import home
from .views.enter import enter
from .views.user import user

app.register_blueprint(home)
app.register_blueprint(enter)
app.register_blueprint(user)

