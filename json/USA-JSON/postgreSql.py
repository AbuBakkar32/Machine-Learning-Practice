import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE student (
            student_id SERIAL PRIMARY KEY,
            student_name VARCHAR(255) NOT NULL
        )
        """,
        """ CREATE TABLE grade (
                grade_id SERIAL PRIMARY KEY,
                grade_name VARCHAR(255) NOT NULL
                )
        """,
        """
        CREATE TABLE student_grade (
                grade_id INTEGER PRIMARY KEY,
                file_extension VARCHAR(5) NOT NULL,
                drawing_data BYTEA NOT NULL,
                FOREIGN KEY (grade_id)
                REFERENCES grade (grade_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE student_detail (
                student_id INTEGER NOT NULL,
                grade_id INTEGER NOT NULL,
                PRIMARY KEY (student_id , grade_id),
                FOREIGN KEY (student_id)
                    REFERENCES student (student_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (grade_id)
                    REFERENCES grade (grade_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
