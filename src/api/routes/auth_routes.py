from flask import jsonify, request

from auth_middleware import token_required
from src import app
from src.api.functions.reader import Reader


@app.route('/api/login', methods=['POST'])
@token_required
def api_login_user():
    data = request.get_json()
    login = data['login']
    password = data['password']
    user = Reader(login=login, password=password)
    return jsonify(user.__login__())
