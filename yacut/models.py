"""
Project Models.

The class also implements data conversion.
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
        Serializer.

        Converting a Complex URLMap Class Object to a Dictionary
        Consisting of Simple Python Data Types.
        """
        return dict(
            id=self.id,
            original=self.original,
            short=self.short,
            timestamp=self.timestamp,
        )

    def from_dict(self, data):
        """
        Deserializer.

        We will add to the empty object of the URLMap class the values of
        the fields that are received in the POST request.
        """
        for field in ['original', 'short']:
            if field in data:
                setattr(self, field, data[field])

    def test_serializer(self, data):
        pass
