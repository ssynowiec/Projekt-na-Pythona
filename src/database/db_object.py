import sqlite3

from src.database.db_connection import DbConnection


class DatabaseObject:
    def add(self) -> dict:
        table_name = self.__class__.__name__.lower()
        attributes = vars(self)
        keys = list(attributes.keys())
        table_columns = ', '.join(keys)
        table_placeholders = ', '.join(['?'] * len(keys))
        values = list(attributes.values())
        table_values = tuple(values)
        query = f"INSERT INTO {table_name} ({table_columns}) VALUES ({table_placeholders})"

        try:
            conn = DbConnection().__open__()

            cursor = conn.cursor()
            cursor.execute(query, table_values)

            conn.commit()
            return {"message": f"Successfully added {table_name} to database"}

        except Exception as e:
            print(f"Error adding {table_name} to database: {str(e)}")
            return {"message": f"Error adding {table_name} to database", "error": str(e)}

        finally:
            DbConnection().__close__()

    @classmethod
    def get_all(cls) -> list | bool:
        table_name = cls.__name__.lower()
        query = f"SELECT * FROM {table_name}"

        try:
            conn = DbConnection().__open__()

            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(query)

            rows = cursor.fetchall()

            return [dict(row) for row in rows]

        except Exception as e:
            print(f"Error getting objects from database: {str(e)}")
            return False

        finally:
            DbConnection().__close__()

    @classmethod
    def get_by_id(cls, _id: int) -> dict | bool:
        table_name = cls.__name__.lower()
        query = f"SELECT * FROM {table_name} WHERE id = ?"

        try:
            conn = DbConnection().__open__()

            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(query, (_id,))

            row = cursor.fetchone()

            return dict(row)

        except Exception as e:
            print(f"Error getting object from database: {str(e)}")
            return False

        finally:
            DbConnection().__close__()
