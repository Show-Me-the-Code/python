from flask import Flask, render_template, request, session, url_for, redirect
import config
from decorators import login_required
import pymysql
from exts import db
from models import User, Question, Comment



app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)




@app.route('/')
def index():
    context = {
        'questions': Question.query.order_by('-create_time').all()
    }
    return render_template('index.html', **context)

@app.route('/detail/<question_id>/')
def detail(question_id):
    question_model = Question.query.filter(Question.id == question_id).first()

    return render_template('detail.html', question = question_model)


@app.route('/comment/', methods=['POST'])
@login_required
def comment():
    content = request.form.get('content')
    question_id = request.form.get('question_id')

    comment = Comment(content=content)
    user_id = session.get('user_id')
    user = User.query.filter(User.id==user_id).first()
    comment.user = user
    question = Question.query.filter(Question.id==question_id).first()
    comment.question = question
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('detail', question_id=question_id))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone, User.password == password).first()
        if user:
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return '登录失败'

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if User.query.filter(User.telephone == telephone).first():
            return '当前号码已注册'
        else:
            if User.query.filter(User.username == username).first():
                return 'username已注册'
            else:
                if password1 == password2:
                    user = User(username=username, telephone=telephone, password=password2)
                    db.session.add(user)
                    db.session.commit()
                    return redirect(url_for('login'))
                else:
                    return '密码不符合'

@app.route('/logout/' )
def logout():
    session.pop('user_id')
    return redirect(url_for('login'))

@app.route('/push_article/', methods=['GET', 'POST'] )
@login_required
def push_article():
    if request.method == 'GET':
        return render_template('push.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title, content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id==user_id).first()
        question.author = user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))

@app.context_processor
def has_user():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user':user}
        else:
            return {}
    else:
        return {}


if __name__ == '__main__':
    app.run(debug=True)