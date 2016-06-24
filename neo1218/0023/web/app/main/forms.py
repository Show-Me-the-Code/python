# -*- coding: UTF-8 -*-
# !/usr/bin/python
from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField,SubmitField
from wtforms.validators import Required

class PostForm(Form):
    body = TextAreaField("说点什么吧!",validators=[Required()])
    submit = SubmitField('提交')


