from app import app
from flask import render_template, request, jsonify
from models import Message
from datetime import datetime


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/message", methods=["POST"])
def save_msg():
    form = request.form
    author = form.get("author")
    content = form.get("content")
    msg = Message(author=author, content=content, time=datetime.now())
    msg.save()
    return jsonify(status='success')


@app.route("/messages")
def list_msg():
    page = request.args.get("page")
    paginator =Message.objects.order_by('-time').paginate(page=int(page), per_page=5)
    pager = {
        'page': paginator.page,
        'pages': paginator.pages,
        'messages': [m.to_json() for m in paginator.items]
    }
    return jsonify(status="success", pager=pager)


