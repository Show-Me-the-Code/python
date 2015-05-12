# -*- coding: UTF-8 -*-
#!/usr/bin/python
from flask import render_template,url_for,redirect
from flask.ext.login import current_user
from .forms import PostForm
from ..models import Post
from .. import db
from . import main


@main.route('/',methods=['GET','POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.body.data,
                    author=current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('.index'))
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html',form=form,posts=posts)


