from databaseConnection import create_connection  # Ensure this module correctly handles the database connection

def deleteRecord(s_no):
    """Delete a record from the database based on the serial number."""
    # Create a connection
    conn = create_connection()
    
    if conn:
        try:
            mycursor = conn.cursor()
            
            # Prepare and execute the delete statement
            mycursor.execute(f"DELETE FROM records WHERE id={s_no}")
            
            # Check if any row was deleted
            if mycursor.rowcount == 0:
                print(f"No record found with serial number: {s_no}")
            else:
                print(f"Record with serial number {s_no} deleted successfully.")
                
            # Commit the changes to the database
            conn.commit()
           
        except Exception as e:
            print(f"An error occurred: {e}")
        
        finally:
            # Close the connection
            conn.close()
