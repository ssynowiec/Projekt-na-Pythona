from flask import jsonify

from auth_middleware import token_required
from src import app
from src.api.functions.book import Book


@app.route('/api/books', methods=['GET'])
@token_required
def api_get_books():
    return jsonify(Book.get_all())


@app.route('/api/book/<int:id>', methods=['GET'])
@token_required
def api_get_book(_ID: int):
    return jsonify(Book.get_by_id(_ID))
