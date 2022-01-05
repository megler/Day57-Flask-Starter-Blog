# starterBlog.py
#
# Python Bootcamp Day 57 - Flask Starter Blog
# Usage:
#      A very simple starter blog using Flask and JSON data. Day 57 Python Bootcamp.
#
# Marceia Egler January 5, 2022

import json
from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route("/")
def home():
    data_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"
    r = requests.get(data_endpoint)
    all_posts = r.json()

    return render_template("index.html", blog_posts=all_posts)


@app.route("/post/<id>")
def blog(id):
    data_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"
    r = requests.get(data_endpoint)
    all_posts = r.json()
    id = int(id)
    title = all_posts[id]["title"]
    body = all_posts[id]["body"]
    subtitle = all_posts[id]["subtitle"]
    return render_template(
        "post.html", title=title, body=body, subtitle=subtitle
    )


if __name__ == "__main__":
    app.run(debug=True)
