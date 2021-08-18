from flask import render_template, redirect
import webbrowser
from MainSite.storage import ARTICLES
from MainSite.static.articles.numbers import d
import requests


def watch_page(value, key):
    if int(key) < 5:
        with open('C:/Users/Рамиль/PycharmProjects/MLSite/MainSite/static/articles/data_handling/' + value + '.txt', 'r', encoding="utf-8") as file:
            lib = file.readlines()
        r = requests.head(lib[0]).status_code
        if r == 200:
            return render_template('library.html', ARTICLES=ARTICLES, d=d), webbrowser.open_new_tab(lib[0])
        else:
            return render_template('error.html')

    elif 5 <= int(key) < 15:
        with open('C:/Users/Рамиль/PycharmProjects/MLSite/MainSite/static/articles/supervised_learning/' + value + '.txt', 'r', encoding="utf-8") as file:
            lib = file.readlines()
        r = requests.head(lib[0]).status_code
        if r == 200:
            return render_template('library.html', ARTICLES=ARTICLES, d=d), webbrowser.open_new_tab(lib[0])
        else:
            return render_template('error.html')

    elif 15 <= int(key) < 30:
        with open('C:/Users/Рамиль/PycharmProjects/MLSite/MainSite/static/articles/unsupervised_learning/' + value + '.txt', 'r', encoding="utf-8") as file:
            lib = file.readlines()
            r = requests.head(lib[0]).status_code
        if r == 200:
            return render_template('library.html', ARTICLES=ARTICLES, d=d), webbrowser.open_new_tab(lib[0])
        else:
            return render_template('error.html')
    # return render_template('watch.html', lib=lib, value=value)

