# what_to_watch/opinions_app/api_views.py
from http import HTTPStatus

# Импортируем метод jsonify
from flask import jsonify, request

from . import app, db
from .models import URLMap


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    # Получить объект по id или выбросить ошибку
    data = URLMap.query.get_or_404(short_id)
    # Конвертировать данные в JSON и вернуть объект и код ответа API
    return jsonify({'url': data.to_dict()}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def add_url():
    # Получение данные из запроса в виде словаря
    data = request.get_json()
    original = data.get('url')
    custom_url = data.get('custom_id')
    # Создание нового пустого экземпляра модели
    url_map = URLMap(
        original=original,
        short=custom_url
    )
    db.session.add(url_map)
    db.session.commit()
    return jsonify({'url': url_map.to_dict()}), HTTPStatus.CREATED








def get_unique_short_id():
    pass

# ヽ(´▽`)/

# kaonashi
# =^..^=______/
