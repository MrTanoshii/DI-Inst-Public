# import psycopg2
# import psycopg2.extras

# from secrets import HOSTNAME, USERNAME, PASSWORD, DATABASE


# # Connect to the db
# postgres_db_connection = psycopg2.connect(
#     host=HOSTNAME,
#     user=USERNAME,
#     password=PASSWORD,
#     dbname=DATABASE,
# )

# print(postgres_db_connection.closed)

# # Init the SQL cursor
# cursor = postgres_db_connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
# # cursor = postgres_db_connection.cursor()
# print(type(cursor))

# query = "SELECT * FROM actors;"
# cursor.execute(query)

# # Get the results from the cursor
# results = cursor.fetchall()

# # fetchone() # Return single result
# # fetchmany(5) # Return 5 results

# postgres_db_connection.commit()

# # Disconnecting from the db
# postgres_db_connection.close()

# # Print the results
# print(results)
# print(type(results))
# print(type(results[0]))

# print("-- Results from Postgres")
# for row in results:
#     print(row)


# SQLite3
import sqlite3

# Connect to the db
sqlite_db_connection = sqlite3.connect("alexissebastienjacobyushi.db")

# Init the SQL cursor
cursor = sqlite_db_connection.cursor()

# Create a table
query = "CREATE TABLE IF NOT EXISTS pets ( \
    id INTEGER PRIMARY KEY AUTOINCREMENT, \
    name VARCHAR(255) \
);"
cursor.execute(query)

# Insert a row
# query = "INSERT INTO pets (name) VALUES \
#     ('Lucky'), \
#     ('Cookie'), \
#     ('Candy'), \
#     ('Rocky'), \
#     ('Schtroumpf'), \
#     ('Canelle'), \
#     ('Treasure') \
# ;"
# cursor.execute(query)

# Select the rows
query = "SELECT * FROM pets;"
sqlite_db_connection.commit()
cursor.execute(query)

# Get the results from the cursor
# results = ""
results = cursor.fetchall()
# while results is not "None":
# results = cursor.fetchone()

# Print the results
print(results)

# Close connection
sqlite_db_connection.close()
