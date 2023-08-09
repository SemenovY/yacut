"""
Модели проекта.

Так же в классе реализована конвертация данных.
"""
from datetime import datetime

from . import db
from .constants import MAX_SHORT_ID_SIZE


class URLMap(db.Model):
    """Model fields and two data converters are described."""

    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, nullable=False)
    short = db.Column(db.String(MAX_SHORT_ID_SIZE), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        """
        Сериализатор.

        Конвертируем сложный объект класса URLMap в словарь,
        который состоит из простых типов данных Python.
        """
        return dict(
            id=self.id,
            original=self.original,
            short=self.short,
            timestamp=self.timestamp,
        )

    def from_dict(self, data):
        """
        Десериализатор.

        Будем добавлять в пустой объект класса URLMap значения полей,
        которые получены в POST-запросе.
        """
        for field in ['original', 'short']:
            if field in data:
                setattr(self, field, data[field])
