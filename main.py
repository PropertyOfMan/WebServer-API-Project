from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, redirect, render_template, request, json
import os
from flask import Flask
from data import db_session
from data.database import Phrases
from random import randint
import _sqlite3


dictionary = {1: ('В золотом окне востока лик свой солнце показало.', 'Ромео и Джульетта'), 2: ('— Через столько лет? — Всегда.', 'Северус Снегг (Северус Снейп)'), 3: ('Ни одного правителя не поддерживают все до единого.', 'Игра престолов'), 4: ('Он коснулся пальцами ее волос, она ощутила, что к ней прикоснулась любовь.', 'Сцены из жизни за стеной'), 5: ('Воины-победители сперва побеждают и только потом вступают в битву; те же, что терпят поражение, сперва вступают в битву и только затем пытаются победить.', 'Сунь-Цзы')}



app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    return render_template('base2.html', theme='Кто ищет — тот всегда найдет', author='Автор неизвестен')


@app.route('/random')
def random():
    x = randint(1, len(dictionary))
    print(x)
    theme, author = dictionary.get(x)
    return render_template('base2.html', theme=theme, author=author)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True)
