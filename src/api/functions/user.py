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
                user = {}
                user['id'] = row['id']
                user['username'] = row['username']
                cls.users.append(user)
        except Exception as e:
            return {'message': 'Error connecting to database: ' + str(e)}

        return cls.users

    @classmethod
    def get_by_name(cls, name):
        cls.users = {}
        try:
            conn = DbConnection()
            db = conn.__open__()
            db.row_factory = sqlite3.Row
            cursor = db.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ?', (name,))
            row = cursor.fetchone()
            cls.users = dict(row)
        except Exception as e:
            return {'message': 'Error connecting to database: ' + str(e)}
        return cls.users

    def post(self, data):
        self.id += 1
        data['id'] = self.id
        self.users.append(data)
        return data

    def put(self, id, data):
        for i in range(len(self.users)):
            if self.users[i]['id'] == id:
                self.users[i] = data
                return data
        return None

    def delete(self, id):
        for i in range(len(self.users)):
            if self.users[i]['id'] == id:
                return self.users.pop(i)
        return None
