import pymysql

import dbconfig

class DBHelper:
    def connect(self, database=dbconfig.db_database):
        return pymysql.connect(host=dbconfig.db_host,
                               user=dbconfig.db_user,
                               password=dbconfig.db_password,
                               db=database)

    def get_all(self):
        connection = self.connect()

        try:
            query = "SELECT description FROM {};".format(dbconfig.db_database)

            with connection.cursor() as cursor:
                cursor.execute(query)

            return cursor.fetchall()
        finally:
            connection.close()

    def add(self, data):
        connection = self.connect()

        try:
            query = "INSERT INTO {}(description) VALUES ('{}');".format(dbconfig.db_database, data)

            with connection.cursor as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()

    def clear_all(self):
        connection = self.connect()

        try:
            query = "DELETE FROM {}".format(dbconfig.db_database)

            with connection.cursor as cursor:
                cursor.execute(query)
                cursor.commit()
        finally:
            connection.close()