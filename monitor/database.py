import psycopg2

from monitor.logging import logger


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
    with psycopg2.connect(db_uri) as conn:
        with conn.cursor() as cur:
            logger.info('Create table if not exists')
            cur.execute(command)


def insert_values(db_uri, values):
    """ insert values in the stats table"""
    values = [
        (value['status_code'], value['reason'], value['response_time'])
        for value in values]

    value_records = ", ".join(["%s"] * len(values))
    keys = "(status_code, reason, response_time)"
    command = "INSERT INTO stats {} VALUES {}".format(keys, value_records)

    with psycopg2.connect(db_uri) as conn:
        with conn.cursor() as cur:
            logger.info("Insert values %s to table", values)
            cur.execute(command, values)
