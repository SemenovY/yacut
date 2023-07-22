from http import HTTPStatus
from flask import jsonify, request
from . import app, db
from .models import URLMap
from .error_handlers import InvalidAPIUsage


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    data = URLMap.query.get(short_id)
    if data is None:
        raise InvalidAPIUsage('Адрес не найден', HTTPStatus.NO_CONTENT)
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









# ヽ(´▽`)/

# kaonashi
# =^..^=______/
