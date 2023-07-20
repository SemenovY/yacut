from . import app, db

from flask import render_template, url_for
from .forms import URLForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)

    url_map = URLMap(
        original=form.original_link.data,
        short=form.custom_id.data,
    )
    db.session.add(url_map)
    db.session.commit()
    result_url = url_for('index_view', _external=True) + url_map.short
    context = {
        'form': form,
        'result_url': result_url
    }
    # return render_template('index.html', **context)
    return render_template('index.html')
