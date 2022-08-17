import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'l1ll111ll111lll111l1l1l'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False