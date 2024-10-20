import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Titima@123",
    database="alx_book_store",
    auth_plugin='mysql_native_password'
)


# Check if the connection was successful
if connection.is_connected():
    # Create a cursor
    cursor = connection.cursor()

    # Execute the SQL command to create the database
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    # Print success message
    print("Database 'alx_book_store' created successfully!")

    # Close the cursor and connection
    cursor.close()
    connection.close()
else:
    print("Failed to connect to the database.")