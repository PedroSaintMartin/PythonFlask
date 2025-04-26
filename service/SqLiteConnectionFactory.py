from sqlite3 import connect

class SqLiteConnectionFactory:
    @staticmethod
    def getConnection():
        conn = connect("./db.db")
        conn.execute("PRAGMA foreign_keys = true")

        return conn