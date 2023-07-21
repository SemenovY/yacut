from datetime import datetime

from settings import MAX_SHORT_ID_SIZE
from . import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, nullable=False)
    short = db.Column(db.String(MAX_SHORT_ID_SIZE), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    # Вот он — новый метод:
    def to_dict(self):
        return dict(
            id = self.id,
            original = self.original,
            short = self.short,
            timestamp = self.timestamp,
        )

    def from_dict(self, data):
        # Для каждого поля модели, которое можно заполнить...
        for field in ['original', 'short']:
            # ...выполняется проверка: есть ли ключ с таким же именем в словаре
            if field in data:
                # Если есть — добавляем значение из словаря
                # в соответствующее поле объекта модели:
                setattr(self, field, data[field])



# kaonashi
# =^..^=______/
