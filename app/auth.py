from flask import jsonify, request, make_response
from app.models import User, Role
import jwt
import uuid
import datetime
from app import app, db
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/api/v0/login', methods=['POST'])
def login():
    data = request.get_json()
    passwrd = data['password']
    email = data['email']
    if not email or not passwrd:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    user = User.query.filter_by(email=email).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if check_password_hash(user.password, passwrd):
        token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)}, app.config['SECRET_KEY'])

        return jsonify({'token': token.decode('UTF-8')})

    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})


@app.route('/api/v0/register', methods=['POST'])
def register_user():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if not not user:
        return make_response('You signup befor', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    hashed_password = generate_password_hash(data['password'], method='sha256')
    user_role = Role.query.filter_by(name='USER').first()
    new_user = User(public_id=str(uuid.uuid4()), user_name=data['user_name'], password=hashed_password, email=data['email'], role=user_role)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'New user created!'})
