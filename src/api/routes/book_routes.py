from flask import jsonify, request

from auth_middleware import token_required
from src import app
from src.api.functions.book import Book


@app.route('/api/books', methods=['GET'])
@token_required
def api_get_books():
    return jsonify(Book.get_all())


@app.route('/api/book/<int:_id>', methods=['GET'])
@token_required
def api_get_book(_id: int):
    return jsonify(Book.get_by_id(_id))


@app.route('/api/book/new', methods=['POST'])
@token_required
def api_add_reader():
    data = request.get_json()
    new_book = Book(**data)
    return jsonify(new_book.add())
