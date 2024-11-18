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
            INSERT INTO student(roll, name)
            VALUES (1, 'John Doe'), (2, 'Jane Smith')
            """

mycursor.execute(sql_query)

my_db_connection.commit()

print("Inserted in student table successfully")