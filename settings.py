"""Укажем пути к базе данных и ключ для CSRF."""
import os


class Config(object):
    """Основные параметры и дефолт для енв."""

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='0000000')
