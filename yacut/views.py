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
        custom_id = form.custom_id.data

        if URLMap.query.filter_by(short=custom_id).first() is not None:
            flash(f'Имя {custom_id} уже занято!')
            return render_template('index.html', form=form)

        if not custom_id:
            custom_id = get_unique_short_id()

        url_map = URLMap(
            original=form.original_link.data,
            short=form.custom_id
        )
        db.session.add(url_map)
        db.session.commit()

        return (
            render_template('index.html', form=form, short=custom_id),
            HTTPStatus.OK
        )
    return render_template('index.html', form=form)

@app.route('/<string:short>')
def redirect_view(short):
    original_link = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(original_link.original)



# kaonashi
# =^..^=______/
