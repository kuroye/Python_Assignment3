from datetime import datetime, timedelta
from flask import Flask
from flask.helpers import make_response
from flask import request
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
import jwt
from functools import wraps
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:er2003618@localhost/PythonFlask'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user_table'

    id = db.Column('id', db.Integer, primary_key=True)

    login = db.Column('login', db.Unicode)

    password = db.Column('password', db.Unicode)

    token = db.Column('token', db.Unicode)

    def __init__(self, id, login, password, token):

        self.id = id

        self.login = login

        self.password = password

        self.token = token


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message': 'Token is missing'}), 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
        except Exception as e:
            logging.exception(e)
            return jsonify({'message': 'Hello, Could not verify the token'}), 403

        return f(*args, **kwargs)

    return decorated


@app.route('/protected')
@token_required
def protected():
    return '<h1>Hello, token which is provided is correct</h1>'


@app.route('/login')
def login():

    auth = request.authorization

    user = User.query.get(1)

    if auth.username == user.login and auth.password == user.password:
        token = jwt.encode({'user': auth.username, 'exp': datetime.utcnow() + timedelta(minutes=10)},
                               app.config['SECRET_KEY'])
        user.token = token
        db.session.commit()
        
        return '<h1>token:</h1>'+user.token+'<h3>Try this link below</h3>'+'http://127.0.01:5000/protected?token='+user.token

    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required'})


if __name__ == '__main__':
    app.run(debug=True)
