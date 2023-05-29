from auth_middleware import token_required
from src import app
from flask import render_template, jsonify
from src.api.functions.user import Users


@app.route('/api/users', methods=['GET'])
@token_required
def api_get_users():
    return jsonify(Users.get_all())


@app.route('/api/users/<string:name>', methods=['GET'])
@token_required
def api_get_user(name):
    return jsonify(Users.get_by_name(name=name))