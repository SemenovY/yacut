from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(1, 256)]
    )
    custom_id = URLField(
        'Короткая ссылка',
        validators=[Length(1, 16), Optional()]
    )
    submit = SubmitField('Добавить')

# ヽ(´▽`)/

# kaonashi
# =^..^=______/
