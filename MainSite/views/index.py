from flask import render_template, request

def index_page():
    return render_template('index.html')