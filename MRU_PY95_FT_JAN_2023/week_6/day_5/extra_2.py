import psycopg2
import psycopg2.extras

from secrets import HOSTNAME, USERNAME, PASSWORD, DATABASE


# Connect to the db
postgres_db_connection = psycopg2.connect(
    host=HOSTNAME,
    user=USERNAME,
    password=PASSWORD,
    dbname="extra_exercise",
)

print(postgres_db_connection.closed)

# Init the SQL cursor
cursor = postgres_db_connection.cursor()

# What a bad actor would do, this is called SQL Injection
first_name = "Victor', '234234'); DROP TABLE author; INSERT INTO person (first_name, last_name) VALUES ('Victor"  # This could have been first_name = input("Please enter your first name")
last_name = "Daniel"

query = f"INSERT INTO person (first_name, last_name) VALUES (%s, %s);"
args = (first_name, last_name)
cursor.execute(query, args)

# Get the results from the cursor
query = "SELECT * FROM person;"
cursor.execute(query)
results = cursor.fetchall()


# Print the results
print(results)


query = "SELECT * FROM author;"
cursor.execute(query)
results = cursor.fetchall()

# Print the results
print(results)

postgres_db_connection.commit()

# Disconnecting from the db
postgres_db_connection.close()
