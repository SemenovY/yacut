"""Формы проекта."""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import Regexp, URL, DataRequired, Length, Optional

from .constants import MAX_SHORT_ID_SIZE, REG_CHECK, SHORT_LINK


class URLForm(FlaskForm):
    """Указываем поля формы и валидаторы."""

    original_link = URLField(
        'Длинная ссылка',
        description=SHORT_LINK,
        validators=(
            DataRequired(message='Обязательное поле'),
            URL(message='Введите корректный URL адрес'),
        ),
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        description='Ваш вариант короткой ссылки',
        validators=(
            Length(
                max=MAX_SHORT_ID_SIZE,
                message='Длина поля не должна превышать 16 символов'
            ),
            Optional(),
            Regexp(
                REG_CHECK,
                message='Ссылка может состоять только из латинских букв и цифр'
            ),
        ),
    )
    submit = SubmitField('Добавить')
