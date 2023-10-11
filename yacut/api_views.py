"""Working with the API."""
import re
from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .constants import MAX_SHORT_ID_SIZE, REG_CHECK, SHORT_LINK
from .error_handlers import InvalidApiUsage
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/api/id/<string:short_id>/', methods=['GET'])
async def get_url(short_id):
    """We receive a short link as input, check and return the original."""
    try:
        data = await URLMap.query.filter_by(short=short_id).first_or_404()
    except Exception:
        raise InvalidApiUsage(
            'The specified id was not found.',
            HTTPStatus.NOT_FOUND
        )
    return jsonify(url=data.original), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
async def add_url():
    """
    We get json, check if there is an error - throw a raise.

    If the short link is not passed, we form it.
    We enter into the database.
    Send response and status OK.
    """
    data = await request.get_json()
    if not data:
        raise InvalidApiUsage('Missing request body')

    if 'url' not in data:
        raise InvalidApiUsage('"url" is a required field!')

    if 'custom_id' not in data or not data['custom_id']:
        short_id = get_unique_short_id()
    else:
        short_id = data['custom_id']

    if URLMap.query.filter_by(short=short_id).first() is not None:
        raise InvalidApiUsage(f'Name "{short_id}" already taken.')

    if len(short_id) > MAX_SHORT_ID_SIZE or not re.match(REG_CHECK, short_id):
        raise InvalidApiUsage(
            'An invalid name was specified for a short link',
            HTTPStatus.BAD_REQUEST
        )

    url_map = URLMap(original=data['url'], short=short_id)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(
        url=url_map.original, short_link=f'{SHORT_LINK}{url_map.short}'
    ), HTTPStatus.CREATED
