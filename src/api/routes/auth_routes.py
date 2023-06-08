from flask import jsonify, request

from auth_middleware import token_required
from src import app
from src.api.functions.reader import Reader


@app.route('/api/auth/login', methods=['POST'])
@token_required
def api_login_user():
    data = request.get_json()
    login = data['login']
    password = data['password']
    user = Reader(login=login, password=password)
    return jsonify(user.__login__())


@app.route('/api/auth/logout', methods=['POST'])
@token_required
def api_logout_user():
    data = request.get_json()
    login = data['login']
    password = data['password']
    user = Reader(login=login, password=password)
    return jsonify(user.__logout__())


@app.route('/api/auth/change-password', methods=['POST'])
@token_required
def api_change_password():
    data = request.get_json()
    login = data['login']
    old_password = data['currentPassword']
    new_password = data['newPassword']
    confirm_password = data['confirmPassword']
    user = Reader(login=login, password=old_password, new_password=new_password, confirm_password=confirm_password)
    return jsonify(user.change_password())
