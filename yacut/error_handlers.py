"""Кастомные ошибки для браузера и для API."""
from flask import jsonify, render_template

from . import app, db


class Invalid_api_usage(Exception):
    """Для апи, ошибка 400."""

    status_code = 400

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return dict(message=self.message)


@app.errorhandler(Invalid_api_usage)
def invalid_api_usage(error):
    """Словарь и статус код."""
    return jsonify(error.to_dict()), error.status_code


@app.errorhandler(404)
def page_not_found(error):
    """Ошибка 404."""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """Ошибка 500."""
    db.session.rollback()
    return render_template('500.html'), 500
