import mysql.connector
from databaseConnection import create_connection
def updateToDatabase(id, name, fname, address, gender, phone):
    # Ensure id is an integer
    id = int(id)
    
    # Create a connection
    conn = create_connection()

    if conn:
        try:
            mycursor = conn.cursor()
            # Corrected SQL query with commas and proper id placeholder
            sql_query = "UPDATE records SET name=%s, fname=%s, address=%s, gender=%s, phone=%s WHERE id=%s"
            mycursor.execute(sql_query, (name, fname, address, gender, phone, id))  # Executing the query
            conn.commit()

            # Check if the record was updated
            if mycursor.rowcount > 0:
                return "Record updated successfully!"
            else:
                return "No record found with the given ID."

        except Exception as e:
            return f"Error: {str(e)}"
           
        finally:
            # Close the connection
            if conn.is_connected():
                conn.close()
