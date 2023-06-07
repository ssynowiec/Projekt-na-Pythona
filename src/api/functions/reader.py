import sqlite3

from src.database.db_connection import DbConnection
from src.database.db_object import DatabaseObject


class Reader(DatabaseObject):
    def __init__(self, login: str, **kwargs):
        self.card_number = kwargs.get('card_number')
        self.name = kwargs.get('name')
        self.surname = kwargs.get('surname')
        self.PESEL = kwargs.get('PESEL')
        self.birthday = kwargs.get('birthday')
        self.phone_number = kwargs.get('phone_number')
        self.address_street = kwargs.get('address_street')
        self.postal_code = kwargs.get('postal_code')
        self.city = kwargs.get('city')
        self.citizenship = kwargs.get('citizenship')
        self.login = login
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')

    def __login__(self):
        table_name = type(self).__name__.lower()
        query = f"SELECT * FROM {table_name}, login_data WHERE reader.login = login_data.login AND reader.login = ? OR login_data.email = ?"

        try:
            conn = DbConnection().__open__()

            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(query, (self.login, self.login))

            row = cursor.fetchone()

            if row is None:
                return {"error": "Invalid login or email"}

            if row['password'] != self.password:
                return {"error": "Invalid password"}

            return dict(row)

        except Exception as e:
            print(f"Error getting object from database: {str(e)}")
            return {"error": str(e)}

        finally:
            DbConnection().__close__()

    def __logout__(self):
        pass

    def get_by_name(self):
        table_name = type(self).__name__.lower()
        query = f"SELECT * FROM {table_name} WHERE login = ?"

        try:
            conn = DbConnection().__open__()

            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(query, (self.login,))

            row = cursor.fetchone()

            if row is None:
                return {"message": "User not found"}, 401

            return dict(row)

        except Exception as e:
            print(f"Error getting object from database: {str(e)}")
            return {"error": str(e)}

        finally:
            DbConnection().__close__()
