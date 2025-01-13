import mysql.connector

# Establish connection
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )

    if connection.is_connected():
        print("Connected to MySQL Database")
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")
finally:
    if connection.is_connected():
        connection.close()
        print("Connection closed.")
