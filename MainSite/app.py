# -*- coding: utf-8 -*-
from flask import Flask
from MainSite.static import index_page, library_page, ml_page, article_page, watch_page

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.add_url_rule('/', view_func=index_page, methods=['GET', 'POST'])
app.add_url_rule('/library', view_func=library_page, methods=['GET', 'POST'])
app.add_url_rule('/ml', view_func=ml_page, methods=['GET', 'POST'])
app.add_url_rule('/article/<key>', view_func=article_page, methods=['GET', 'POST'])
app.add_url_rule('/watch/<value>/<key>', view_func=watch_page, methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run()
