"""
For the main page, we process the POST request.

Returning a working link.
"""
from http import HTTPStatus

from flask import flash, redirect, render_template
from setuptools._entry_points import render

from . import app, db
from .constants import INDEX_HTML
from .forms import URLForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    """
    Get form.

    We make checks, if necessary, generate a short link. We save to
    the database. Return status and notification.
    """
    form = URLForm()
    if not form.validate_on_submit():
        return render_template(INDEX_HTML, form=form)

    short_url = form.custom_id.data
    if URLMap.query.filter_by(short=short_url).first() is not None:
        flash(f'Name {short_url} already taken!')
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
    """We return if there is a link, and for the transition - 404."""
    urlmap = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(urlmap.original)


@app.route('/', methods=['GET'])
def test_or_404(request):
    """Test"""
    if request.method == 'GET':
        return redirect(request.method)
    return render(request)
