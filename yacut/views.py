from . import app, db

from flask import render_template
from .forms import URLMapForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    # Если ошибок не возникло, то
    if form.validate_on_submit():
        url = URLMap(
            original=form.original_link.data,
            short=form.custom_id.data,
        )
        db.session.add(url)
        db.session.commit()
        # # Затем перейти на страницу добавленного мнения
        # return redirect(url_for('opinion_view', id=opinion.id))

    # Иначе просто отрисовать страницу с формой
    return render_template('index.html', form=form)


def get_unique_short_id():
    pass
