import mysql.connector

# Create a connection
my_db_connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Aiub15-1?"
)

print(my_db_connection)

# Create a database
db_name = "python_test_db"

mycursor = my_db_connection.cursor()

sql_query = "CREATE DATABASE " + db_name

mycursor.execute(sql_query)