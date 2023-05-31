import sqlite3

from src.database.db_connection import DbConnection


class Users:
    users = {}

    def __init__(self):
        self.users = []
        self.id = 0

    @classmethod
    def get_all(cls):
        cls.users = []

        try:
            conn = DbConnection().__open__()

            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users')

            rows = cursor.fetchall()

            for row in rows:
                user = {'id': row['id'], 'username': row['username']}
                cls.users.append(user)

        except Exception as _e:
            return {'message': 'Error connecting to database: ' + str(_e)}

        return cls.users

    @classmethod
    def get_by_name(cls, _name):
        cls.users = {}

        try:
            conn = DbConnection()

            db = conn.__open__()
            db.row_factory = sqlite3.Row

            cursor = db.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ?', (_name,))
            row = cursor.fetchone()

            cls.users = dict(row)

        except Exception as _e:
            return {'message': 'Error connecting to database: ' + str(_e)}

        return cls.users

    def post(self, _data):
        self.id += 1
        _data['id'] = self.id
        self.users.append(_data)

        return _data

    def put(self, _ID, _data):
        for i in range(len(self.users)):
            if self.users[i]['id'] == _ID:
                self.users[i] = _data
                return _data

        return None

    def delete(self, _ID):
        for i in range(len(self.users)):
            if self.users[i]['id'] == _ID:
                return self.users.pop(i)

        return None
