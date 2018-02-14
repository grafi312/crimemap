import dbconfig
import pymysql

connection = pymysql.connect(host='localhost',
                                user=dbconfig.db_user,
                                password=dbconfig.db_password)

try:
    with connection.cursor() as cursor:
        sql = "CREATE DATABASE IF NOT EXISTS `crimemap`"
        cursor.execute(sql)

        sql = """
CREATE TABLE IF NOT EXISTS `crimemap`.`crimes`(
id INT NOT NULL AUTO_INCREMENT,
latitude FLOAT(10,6),
longitude FLOAT(10,6),
date DATETIME,
category VARCHAR(50),
description TEXT,
update_at TIMESTAMP,

PRIMARY KEY (id)
)
"""
        cursor.execute(sql)

    cursor.commit()

finally:
    connection.close()