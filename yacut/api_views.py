"""Работа с API."""
import re
from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .constants import MAX_SHORT_ID_SIZE, REG_CHECK, SHORT_LINK
from .error_handlers import InvalidApiUsage
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    """Получаем на вход короткую ссылку, проверяем и возвращаем оригинал."""
    try:
        data = URLMap.query.filter_by(short=short_id).first_or_404()
    except Exception:
        raise InvalidApiUsage(
            'Указанный id не найден',
            HTTPStatus.NOT_FOUND
        )
    return jsonify(url=data.original), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def add_url():
    """
    Получаем json, проверяем, если ошибка - выбрасываем raise.

    Если короткую ссылку не передали, формируем ее.
    Заносим в базу данных. Отправляем ответ и статус ОК.
    """
    data = request.get_json()
    if not data:
        raise InvalidApiUsage('Отсутствует тело запроса')

    if 'url' not in data:
        raise InvalidApiUsage('"url" является обязательным полем!')

    if 'custom_id' not in data or not data['custom_id']:
        short_id = get_unique_short_id()
    else:
        short_id = data['custom_id']

    if URLMap.query.filter_by(short=short_id).first() is not None:
        raise InvalidApiUsage(f'Имя "{short_id}" уже занято.')

    if (
            len(short_id) > MAX_SHORT_ID_SIZE
            or not re.match(REG_CHECK, short_id)
    ):
        raise InvalidApiUsage(
            'Указано недопустимое имя для короткой ссылки',
            HTTPStatus.BAD_REQUEST
        )

    url_map = URLMap(original=data['url'], short=short_id)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(
        url=url_map.original, short_link=f'{SHORT_LINK}{url_map.short}'
    ), HTTPStatus.CREATED
