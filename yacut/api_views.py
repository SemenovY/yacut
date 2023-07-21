# what_to_watch/opinions_app/api_views.py
from http import HTTPStatus

# Импортируем метод jsonify
from flask import jsonify, request

from . import app, db
from .models import URLMap
from .error_handlers import InvalidAPIUsage


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    data = URLMap.query.get(short_id)
    if data is None:
        raise InvalidAPIUsage('В базе данных нет мнений', HTTPStatus.NO_CONTENT)
    return jsonify({'url': data.to_dict()}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()
    if 'original' not in data:
        raise InvalidAPIUsage('Отсутствует тело запроса')

    if URLMap.query.filter_by(short=data['custom_id']).first() is not None:
        raise InvalidAPIUsage('Такая ссылка уже есть в базе данных')

    original = data.get('url')
    custom_url = data.get('custom_id')
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
