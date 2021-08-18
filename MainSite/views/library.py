from flask import render_template, request
from MainSite.storage import ARTICLES
from MainSite.static.articles.numbers import d


def library_page():
    return render_template('library.html', ARTICLES=ARTICLES, d=d)
