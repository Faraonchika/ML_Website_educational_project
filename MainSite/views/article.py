from flask import render_template, request
from MainSite.storage import ARTICLES


def article_page(key):
    article = [x for x in ARTICLES if x['Key'] == key]
    return render_template('article.html', article=article[0])
