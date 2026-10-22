import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-fallback-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'instance', 'syncplay.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STEAM_API_KEY = os.environ.get('STEAM_API_KEY')
