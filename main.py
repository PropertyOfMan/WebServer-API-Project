from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, redirect, render_template, request, json
import os
from flask import Flask
from data import db_session
from data.database import Phrases
from random import randint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    return render_template('base2.html', theme='Кто ищет — тот всегда найдет', author='Автор неизвестен')


@app.route('/random')
def random():
    for i in session.query(Phrases).filter(Phrases.id == randint(1, len(session.query(Phrases).all()))):
        needed = i
    return render_template('base2.html', theme=needed.phrase, author=needed.author)


if __name__ == '__main__':
    db_session.global_init("db/my_db.sqlite")
    session = db_session.create_session()
    app.run(host='localhost', port=80, debug=True)