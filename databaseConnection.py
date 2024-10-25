import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create and return a database connection."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="", 
            database="trip"  
        )
        
        if connection.is_connected():
            print("Connection to MySQL DB successful")
            return connection
        else:
            print("Connection to MySQL DB failed")
            return None
    
    except Error as e:
        print(f"Error: {e}")
        return None



