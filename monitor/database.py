import psycopg2


def create_table(db_uri):
    """ create tables in the PostgreSQL database"""
    command = """
        CREATE TABLE IF NOT EXISTS stats (
            stat_id SERIAL PRIMARY KEY,
            status_code VARCHAR(255) NOT NULL,
            reason VARCHAR(255) NOT NULL,
            response_time DECIMAL NOT NULL
        )
        """
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(db_uri)
        cur = conn.cursor()
        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

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


def insert_values(db_uri, values):
    """ insert values in the stats table"""
    values = [
        (value['status_code'], value['reason'], value['response_time'])
        for value in values]

    value_records = ", ".join(["%s"] * len(values))
    keys = "(status_code, reason, response_time)"
    insert_query = (
        "INSERT INTO stats {} VALUES {}".format(keys, value_records)
    )

    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(db_uri)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(insert_query, values)

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
