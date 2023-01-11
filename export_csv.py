import csv
import psycopg2

username = 'diubakin'
password = 'postgres'
database = 'lab2_Netflix_Top'

OUTPUT_FILE_T = 'diubakin01_DB_{}.csv'

TABLES = [
    'countries',
    'shows',
    'top10_by_contries'
]

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()

    for table_name in TABLES:
        cur.execute('SELECT * FROM ' + table_name)
        fields = [x[0] for x in cur.description]
        with open(OUTPUT_FILE_T.format(table_name), 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x) for x in row])
