import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Attempt to connect to the MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Titima@123",
            auth_plugin='mysql_native_password'
        )

        if connection.is_connected():
            # Create a cursor object
            cursor = connection.cursor()

            # Create the database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            # Print success message
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        # Print error message if an exception occurs
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection if they were opened
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
