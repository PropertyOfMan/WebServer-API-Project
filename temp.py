from flask import Flask
from data import db_session
from data.database import Phrases
from random import randint


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    while 1:
        db_session.global_init("db/my_db.sqlite")
        session = db_session.create_session()


        theme = Phrases()
        n = input()
        if n != '0':
            theme.phrase = n
            input()
            theme.author = input()
            session.add(theme)
            session.commit()

            print('OK')
        else:
            break


if __name__ == '__main__':
    main()

