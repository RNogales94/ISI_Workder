from flask import Flask, render_template
from flask import session, redirect, url_for, request

from db import find_restaurant
from db_isi import find_by_key, search

import os
import json

app = Flask(__name__)


@app.route("/",  methods = ['GET', 'POST'])
def restaurants():
    return render_template('restaurants.html')

@app.route('/api/jobs/keywords/<value>')
def query_keywords(value):
    result = search(value)

    myjson = [{"title":row.get("title"), "summary":row.get("summary"), "url":row.get("url", ""), "company":row.get("company", ""), "location":row.get("location")} for row in result]
    return json.dumps(myjson, ensure_ascii=False).encode('utf8')

@app.route('/api/jobs/<key>/<value>')
def query_key_value(key, value):
    result = find_by_key(key, value)
    myjson = [{"title":row.get("title"), "summary":row.get("summary"), "url":row.get("url", ""), "company":row.get("company", ""), "location":row.get("location")} for row in result]
    return json.dumps(myjson, ensure_ascii=False).encode('utf8')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(host='0.0.0.0', debug=True)
