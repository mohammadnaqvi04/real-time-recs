import psycopg2
from psycopg2 import OperationalError

def create_conn():
    conn = None
    try:
        # These are placeholders; replace them with your actual credentials
        conn = psycopg2.connect(
            database="your_database",
            user="your_username",
            password="your_password",
            host="localhost",  # or the IP address of your PostgreSQL server
            port="5432",  # or the port your PostgreSQL server is listening on
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return conn

connection = create_conn()

# Creating a cursor object using the cursor() method
cursor = connection.cursor()

# Executing an MYSQL function using the execute() method
cursor.execute("SELECT DATABASE()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)
