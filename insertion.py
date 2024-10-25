import mysql.connector
from databaseConnection import create_connection

def insertToDatabase(name, fname, address, gender, phone):
    # Create a connection
    conn = create_connection()

    if conn:
        try:
            mycursor = conn.cursor()
            sql_query = "INSERT INTO records  (name, fname, address, gender, phone) VALUES (%s, %s, %s, %s, %s)"
            mycursor.execute(sql_query, (name, fname, address, gender, phone))  # Executing the query
            conn.commit()
            if mycursor.rowcount > 0:
                return "Record inserted successfully!"
            else:
                return "Error occurred!"
               
        except Exception as e:
            return f"Error: {str(e)}"
           
        finally:
            # Close the connection
            if conn.is_connected():
                conn.close()
