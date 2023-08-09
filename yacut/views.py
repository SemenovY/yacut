"""
For the main page, we process the POST request.

Returning a working link.
"""
from http import HTTPStatus

from flask import flash, redirect, render_template

from . import app, db
from .constants import INDEX_HTML
from .forms import URLForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    """
    Получаем форму.

    Делаем проверки, при необходимости генерируем короткую ссылку.
    Сохраняем в базу.
    Возвращаем статус и уведомление.
    """
    form = URLForm()
    if not form.validate_on_submit():
        return render_template(INDEX_HTML, form=form)

    short_url = form.custom_id.data
    if URLMap.query.filter_by(short=short_url).first() is not None:
        flash(f'Имя {short_url} уже занято!')
        return render_template(INDEX_HTML, form=form)
    if short_url is None or short_url == '':
        form.custom_id.data = get_unique_short_id()

    url_map = URLMap(
        original=form.original_link.data,
        short=form.custom_id.data,
    )
    db.session.add(url_map)
    db.session.commit()

    return (
        render_template(INDEX_HTML, form=form, short=url_map),
        HTTPStatus.OK
    )


@app.route('/<string:short>')
def redirect_url(short):
    """Возвращаем если есть ссылку, а для перехода - 404."""
    urlmap = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(urlmap.original)
