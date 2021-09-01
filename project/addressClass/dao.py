import sqlite3

# Dao : Data Access Object
class SqliteAddressDao:
    "sqlite에 주소록 입출력을 담당하는 클래스"
    def __init__(self, fileName):
        self.conn = sqlite3.connect(fileName)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def inputAddress(self, tableName, address):
        sql = """
            INSERT INTO {0}(name, age, addr) VALUES('{1}','{2}','{3}')
        """.format(tableName, address.name, address.age, address.addr)
        self.cursor.execute(sql)
        self.conn.commit()

    def searchAddress(self, tableName, name):
        sql = """
            SELECT * FROM {0} WHERE name='{1}'
        """.format(tableName, name)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def deleteAddress(self, tableName, name):
        sql = """
            DELETE FROM {0} WHERE name='{1}'
        """.format(tableName, name)
        self.cursor.execute(sql)
        self.conn.commit()

    def updateAddress(self, tableName, fname, address):
        sql = """
            UPDATE {0} SET name='{1}', age='{2}', addr='{3}'
             WHERE name='{4}'
        """.format(tableName, address.name, address.age, address.addr, fname)
        self.cursor.execute(sql)
        self.conn.commit()

    def searchAllAddress(self, tableName):
        sql = """
            SELECT * FROM {0}
        """.format(tableName)
        self.cursor.execute(sql)
        return self.cursor.fetchall()