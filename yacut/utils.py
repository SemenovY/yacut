import random
import string
from .constants import MIN_SHORT


def get_unique_short_id():
    letters = string.ascii_letters + string.digits
    short_id = ''.join(random.choice(letters) for _ in range(MIN_SHORT))

    return short_id

# Автоматически сгенерированная короткая ссылка должна добавляться в базу
# данных, но только если в ней уже нет такого же идентификатора.
# В противном случае нужно генерировать идентификатор заново.
# from . import db
# from .models import URLMap
# from .constants import SHORT_URL_MAX_LENGTH
#
# def get_unique_short_id():
#     while True:
#         short_id = ''.join(random.choices(
#             string.ascii_letters + string.digits, k=SHORT_URL_MAX_LENGTH))
#         if not db.session.query(db.exists().where(URLMap.short == short_id)).scalar():
#             return short_id

# ヽ(´▽`)/

# kaonashi
# =^..^=______/
#
