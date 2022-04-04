from datetime import datetime

import psycopg2


def create_tables():
    """ create tables in the PostgreSQL database"""
    try:
        connection = psycopg2.connect(user="postgres", password="asl123", host="localhost", port="5433",
                                      database="automation")
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    # finally:
    #     # closing database connection.
    #     if connection:
    #         connection.close()
    #         print("PostgreSQL connection is closed")


def sqlQuery():
    connection = create_tables()
    cursor = connection.cursor()
    fetch_student = """
                        insert into fail (file_name, time_stamp, status) values (%s, %s, %s)
                    """
    # Print PostgreSQL version
    cursor.execute(fetch_student, ('abcd', datetime.now().date(), 'failed'))
    connection.commit()
    cursor.close()
if __name__ == '__main__':
    sqlQuery()
