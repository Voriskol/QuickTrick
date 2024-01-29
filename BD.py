# Importing module
from mysql.connector import connect, Error
dict_of_brothers = dict()

try:
    with connect(
        host="localhost",
        user="root",
        password="1234",
        database="mydb",
    ) as connection:
        print(connection)
        show_db_query = "SHOW DATABASES"
        with connection.cursor() as cursor:
            cursor.execute(show_db_query)
            for db in cursor:
                print(db)
        select_users_query = "SELECT FIO FROM users"
        with connection.cursor() as cursor:
            cursor.execute(select_users_query)
            result = cursor.fetchall()
            for row in result:
              print(row)
        select_users_query = """
                                SELECT FIO, text
                                FROM users
                                INNER JOIN anecdots
                                    ON users.id = anecdots.id
                                GROUP BY users.id
                              """
        with connection.cursor() as cursor:
            cursor.execute(select_users_query)
            for i in cursor.fetchall():
              dict_of_brothers[i[0]] = i[1]
              print(i)
except Error as e:
    print(e)
