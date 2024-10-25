from databaseConnection import create_connection

def retriveData():
    # Create a connection
    conn = create_connection()
    if conn:
        try:
            mycursor = conn.cursor()
            mycursor.execute("SELECT * FROM records")
            rows = mycursor.fetchall()
            return rows
        except Exception as e:
            return f"Error: {str(e)}"
        finally:
            # Close the connection
            conn.close()
