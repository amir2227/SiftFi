from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from app.models import User, Role
import uuid
from app.utils import token_required


@app.route('/api/v0/admin/create_user', methods=['POST'])
@token_required
def create_user(current_user):
    if not current_user.role.name == 'ADMIN' or not current_user.role.name == 'OWNER':
        return jsonify({'message': 'Cannot perform that function!'})

    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')
    role = Role.query.filter_by(name=data['role']).first()
    new_user = User(public_id=str(uuid.uuid4()), user_name=data['user_name'], password=hashed_password, email=data['email'], role=role)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'New user created!'})


@app.route('/api/v0/admin/get_all_user', methods=['GET'])
@token_required
def get_all_users(current_user):
    print(current_user.role.name)
    if not current_user.role.name == 'OWNER' and not current_user.role.name == 'ADMIN':
        return jsonify({'message': 'Cannot perform that function!'})

    users = User.query.all()
    print(current_user.role.name)
    output = []

    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['user_name'] = user.user_name
        user_data['password'] = user.password
        user_data['role'] = user.role.name
        user_data['email'] = user.email
        output.append(user_data)

    return jsonify({'users': output})


@app.route('/api/v0/admin/promote_user')
@token_required
def promote_user(current_user):
    if not current_user.role.name == 'OWNER' and not current_user.role.name == 'ADMIN':
        return jsonify({'message': 'Cannot perform that function!'})
    email = str(request.args.get('email'))
    role_name = str(request.args.get('role_name'))
    user = User.query.filter_by(email=email).first()
    print(user)
    if not user:
        return jsonify({'message': 'No user found!'})
    role = Role.query.filter_by(name=role_name).first()
    print(role.name)

    user.role = role
    db.session.commit()

    return jsonify({'message': 'The user has been promoted!'})
