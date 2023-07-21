from http import HTTPStatus

from . import app, db

from flask import redirect, render_template, flash
from .api_views import get_unique_short_id
from .forms import URLForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        short_url = form.custom_id.data

        if URLMap.query.filter_by(short=short_url).first() is not None:
            flash(f'Имя {short_url} уже занято!')
            return render_template('index.html', form=form)

        if not short_url:
            short_url = get_unique_short_id()

        url_map = URLMap(
            original=form.original_link.data,
            short=form.custom_id.data
        )
        db.session.add(url_map)
        db.session.commit()

        return (
            render_template('index.html', form=form, short=short_url),
            HTTPStatus.OK
        )
    return render_template('index.html', form=form)


@app.route('/<string:short>')
def redirect_url(short):
    url = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(url.original)



# kaonashi
# =^..^=______/
