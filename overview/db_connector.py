
import mysql.connector

db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Prasath@2002",
)
# print(db)
mycursor=db.cursor()
#mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute('show Databases')
result=mycursor.fetchall()
for i in result:
    print(i)

"""-------------------------------------------------------------------------------------------------"""
# import mysql.connector

# try:
#     connection=mysql.connector.connect(
#                 host="localhost",
#                 user="root",
#                 password="Prasath@2002",
#                 database="event_managements"
#     )
#     if connection.is_connected():
#         print("Connected to MySQL Database")
        
#         db_info=connection.get_server_info()
#         print(f"Server Info: {db_info}")

# except mysql.connector.errors as err:
#     print(f"Error: {err}")

# finally:
#     if connection.is_connected():
#         connection.close()
#         print("MySQL connection is closed")



"""-------------------------------------------------------------------------------------------------"""


                #THIS IS THE STRUCTURE OF MYSQL CONNECTIONS BY CHATgpt..

import mysql.connector

# Establish the connection
db = mysql.connector.connect(
    host="localhost",       # Your database host (e.g., localhost)
    user="root",            # Your username
    password="your_password", # Your password
    database="your_database" # Optional: specify a database
)

# Check if the connection was successful
if db.is_connected():
    print("Connection established successfully!")

# Create a cursor object
cursor = db.cursor()

# Example 1: Create a Database
try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS sample_db")
    print("Database created successfully!")
except mysql.connector.Error as err:
    print(f"Error: {err}")

# Example 2: Select a Database
cursor.execute("USE sample_db")

# Example 3: Create a Table
try:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100) UNIQUE,
        age INT
    )
    """)
    print("Table created successfully!")
except mysql.connector.Error as err:
    print(f"Error: {err}")

# Example 4: Insert Data
try:
    cursor.execute("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", 
                   ("John Doe", "john@example.com", 30))
    db.commit()  # Commit changes to the database
    print("Data inserted successfully!")
except mysql.connector.Error as err:
    print(f"Error: {err}")

# Example 5: Fetch Data
try:
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    for row in results:
        print(row)
except mysql.connector.Error as err:
    print(f"Error: {err}")

# Close the cursor and connection
cursor.close()
db.close()
print("Connection closed.")



"""-------------------------------------------------------------------------------------------------"""