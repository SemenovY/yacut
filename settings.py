import os


MAX_URL_SIZE = 256
MAX_SHORT_ID_SIZE = 16


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')


# kaonashi
# =^..^=______/
