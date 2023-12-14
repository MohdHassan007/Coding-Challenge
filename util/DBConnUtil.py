# util/DBConnUtil.py

import mysql.connector
from util.DBPropertyUtil import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def open_connection():
        try:
            properties = DBPropertyUtil.get_connection_properties()
            connection = mysql.connector.connect(**properties) #sql.connect(host='localhost', database='demo', user='root', password='123456789')
            return connection
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL: {e}")
            return None
