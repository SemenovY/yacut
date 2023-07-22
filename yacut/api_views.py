import re
from http import HTTPStatus
from flask import jsonify, request
from .utils import get_unique_short_id
from . import app, db
from .models import URLMap
from .error_handlers import InvalidAPIUsage
from .constants import MAX_SHORT_ID_SIZE, REG_CHECK



@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    data = URLMap.query.filter_by(short=short_id).first()
    if data is None:
        raise InvalidAPIUsage('Указанный id не найден',
                              HTTPStatus.NOT_FOUND)
    return jsonify({'url': data.to_dict()}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if ('custom_id' not in data or data['custom_id'] == ''
            or data['custom_id'] is None):
        short_id = get_unique_short_id()
    else:
        short_id = data['custom_id']

    if URLMap.query.filter_by(short=short_id).first() is not None:
        raise InvalidAPIUsage(f'Имя "{short_id}" уже занято.')
    if len(short_id) > MAX_SHORT_ID_SIZE or not re.match(REG_CHECK, short_id):
        raise InvalidAPIUsage(
            'Указано недопустимое имя для короткой ссылки',
            HTTPStatus.BAD_REQUEST
        )

    url_map = URLMap(original=data['url'], short=short_id)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(
        short_link='http://localhost/' + url_map.short, url=url_map.original
    ), HTTPStatus.CREATED









# ヽ(´▽`)/

# kaonashi
# =^..^=______/
