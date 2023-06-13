import sqlite3

from src.database.db_connection import DbConnection
from src.database.db_object import DatabaseObject


class Reader(DatabaseObject):
    def __init__(self, login: str, **kwargs: dict):
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
        self.new_password = kwargs.get('new_password')
        self.confirm_password = kwargs.get('confirm_password')

    def __login__(self) -> dict:
        table_name = type(self).__name__.lower()
        query = f"SELECT * FROM {table_name}, " \
                f"login_data WHERE reader.login = login_data.login AND reader.login = ? OR login_data.email = ?"

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

    def __logout__(self) -> None:
        pass

    def get_by_name(self) -> dict | tuple:
        table_name = type(self).__name__.lower()
        query = f"SELECT * FROM {table_name} WHERE login = ?"

        try:
            conn = DbConnection().__open__()

            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(query, (self.login,))

            row = cursor.fetchone()

            if row is None:
                return {"error": "User not found"}, 401

            return dict(row)

        except Exception as e:
            print(f"Error getting object from database: {str(e)}")
            return {"error": str(e)}

        finally:
            DbConnection().__close__()

    def change_password(self) -> dict | tuple:
        old_password = f"SELECT password FROM login_data WHERE login = ?"

        try:
            conn = DbConnection().__open__()

            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(old_password, (self.login,))

            row = cursor.fetchone()

            if row is None:
                return {"error": "User not found"}, 401

            if self.password == '' or self.new_password == '' or self.confirm_password == '':
                return {"error": "Please fill all fields"}

            if row['password'] != self.password:
                return {"error": "Invalid old password"}
            elif row['password'] == self.new_password:
                return {"error": "New password cannot be the same as the old one"}
            elif self.new_password != self.confirm_password:
                return {"error": "Passwords do not match"}
            elif len(self.new_password) < 8:
                return {"error": "Password must be at least 8 characters long"}
            elif len(self.new_password) > 50:
                return {"error": "Password must be at most 50 characters"}
            else:
                query = f"UPDATE login_data SET password = ? WHERE login = ?"
                cursor.execute(query, (self.new_password, self.login))
                conn.commit()

            return {"message": "Password changed successfully"}

        except Exception as e:
            print(f"Error getting object from database: {str(e)}")
            return {"error": str(e)}

        finally:
            DbConnection().__close__()
