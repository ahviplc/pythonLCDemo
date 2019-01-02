import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Flask
from config import basedir

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object('config')
lm = LoginManager()
# lm.setup_app(app) # 过时方法 废弃使用 现在使用：lm.init_app(app)
lm.init_app(app)
lm.login_view = 'login'

from app import views, models
