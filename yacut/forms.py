"""Формы проекта."""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional

from .constants import MAX_SHORT_ID_SIZE, MAX_URL_SIZE


class URLForm(FlaskForm):
    """Указываем поля формы и валидаторы."""

    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    URL(message='Введите корректный URL адрес'),
                    Length(max=MAX_URL_SIZE)]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(max=MAX_SHORT_ID_SIZE),
                    Optional()]
    )
    submit = SubmitField('Добавить')
