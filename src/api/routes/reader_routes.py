from flask import jsonify, request

from auth_middleware import token_required
from src import app
from src.api.functions.reader import Reader


@app.route('/api/readers', methods=['GET'])
@token_required
def api_get_users():
    return jsonify(Reader.get_all())


@app.route('/api/reader/<string:_login>', methods=['GET'])
@token_required
def api_get_user(_login):
    user = Reader(login=_login)
    return jsonify(user.get_by_name())


# TODO: Not working
@app.route('/api/reader/new', methods=['POST'])
@token_required
def api_add_book():
    data = request.get_json()
    new_reader = Reader(**data)
    return jsonify(new_reader.add())
