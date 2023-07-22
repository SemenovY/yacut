from http import HTTPStatus

from . import app, db

from flask import redirect, render_template, flash
from .utils import get_unique_short_id
from .forms import URLForm
from .models import URLMap
from .constants import INDEX_HTML


@app.route('/', methods=['GET', 'POST'])
def index_view():
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
    urlmap = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(urlmap.original)



# kaonashi
# =^..^=______/
