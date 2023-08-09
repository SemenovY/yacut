"""Create a random link for the custom_id field with a match check."""
import random
import string

from .constants import MIN_SHORT
from .models import URLMap


def get_unique_short_id():
    """Через random и string создаем ссылку, делаем проверку, возвращаем."""
    while True:
        letters = string.ascii_letters + string.digits
        short_id = ''.join(random.choice(letters) for _ in range(MIN_SHORT))
        if URLMap.query.filter_by(short=short_id).first() is None:
            return short_id
