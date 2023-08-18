"""Project Forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import Regexp, URL, DataRequired, Length, Optional

from .constants import MAX_SHORT_ID_SIZE, REG_CHECK, SHORT_LINK


class URLForm(FlaskForm):
    """Specify form fields and validators."""

    original_link = URLField(
        'Long link',
        description=SHORT_LINK,
        validators=(
            DataRequired(message='Obligatory field'),
            URL(message='Please enter a valid URL'),
        ),
    )
    custom_id = StringField(
        'Your Short Link',
        description='Your Short Link',
        validators=(
            Length(
                max=MAX_SHORT_ID_SIZE,
                message='The field length must not exceed 16 characters'
            ),
            Optional(),
            Regexp(
                REG_CHECK,
                message='The link can only consist of letters and numbers'
            ),
        ),
    )
    submit = SubmitField('Add')
