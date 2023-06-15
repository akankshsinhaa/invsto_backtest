import pymysql

# Connect to the MySQL server
cnx = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='test'
)

# Create a cursor object to execute SQL queries
cursor = cnx.cursor()


def createTable(table_name):
    create_table_query = '''
    CREATE TABLE %s (
    datetime DATETIME,
    close DECIMAL(10, 2),
    open DECIMAL(10, 2),
    high DECIMAL(10, 2),
    low DECIMAL(10, 2),
    volume INT,
    instrument VARCHAR(255)
    );
    
    ''' % (table_name)

    # Execute the query to create the table
    #cursor.execute(create_table_query)

    # Commit the changes to the database
    #cnx.commit()
    print(create_table_query)


def checkIfDatabaseExists(database_name):


    # SQL query to fetch the list of databases
    show_databases_query = 'SHOW DATABASES'

    # Execute the query
    cursor.execute(show_databases_query)

    # Fetch all the databases
    databases = cursor.fetchall()

    # Check if the database exists
    if (database_name,) in databases:
        return True
    else:
        return False


# Table name to check
def checkIfTableExists(table_name):


    # SQL query to check if the table exists
    check_table_query = f"SHOW TABLES LIKE '{table_name}'"

    # Execute the query
    cursor.execute(check_table_query)

    # Fetch the result
    result = cursor.fetchone()

    # Check if the table exists
    if result:
        return True
    else:
        return False




if(checkIfTableExists("")):
    print("Table already exists")
else:
    createTable("")
print(checkIfDatabaseExists("test"))



cursor.close()
cnx.close()
