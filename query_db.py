import psycopg2
from env_vars import dbname,user,host,password

def get_data(value):
    try:
        # Establish a connection to the database
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            host=host,
            password=password
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Execute the SQL query
        query = "SELECT * FROM nutritionalinfo WHERE fooditem = '"+ str(value) +"'"
        cursor.execute(query)

        # Fetch all the rows
        rows = cursor.fetchall()

        for row in rows:
            return row

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # Close the database connection
        if connection:
            cursor.close()
            connection.close()

