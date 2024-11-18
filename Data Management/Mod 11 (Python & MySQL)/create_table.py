import mysql.connector

db_name = "python_test_db"

# Create a connection
my_db_connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Aiub15-1?",
    database = db_name
)

mycursor = my_db_connection.cursor()

sql_query = """
            CREATE TABLE student
            (
                roll VARCHAR(4),
                name VARCHAR(30)
            )
            """

mycursor.execute(sql_query)

print("Created student table successfully")