import csv
import psycopg2

username = 'diubakin'
password = 'postgres'
database = 'lab2_Netflix_Top'

INPUT_CSV_FILE = 'labs\\lab3\\dataset\\all-weeks-countries.csv'


query_1 = '''
DELETE FROM countries;
'''

query_2 = '''
INSERT INTO countries (country_iso2, country_name) VALUES (%s, %s)
'''

query_3 = '''
DELETE FROM shows;
'''

query_4 = '''
INSERT INTO shows (show_id, show_title, category) VALUES (%s, %s, %s)
'''

query_5 = '''
DELETE FROM top10_by_contries;
'''

query_6 = '''
INSERT INTO top10_by_contries (country_iso2, show_id, week, weekly_rank, cumulative_weeks_in_top_10) VALUES (%s, %s, %s, %s, %s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()
    cur.execute(query_5)
    cur.execute(query_3)
    cur.execute(query_1)
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)

        countries = []
        shows = []
        ids = 0
        for idx, row in enumerate(reader):
            if row['country_iso2'] not in countries:
                countries.append(row['country_iso2'])
                values = (row['country_iso2'], row['country_name'])
                cur.execute(query_2, values)

            if row['show_title'] not in shows:
                shows.append(row['show_title'])
                ids += 1
                values = (ids, row['show_title'], row['category'])
                cur.execute(query_4, values)

            id = shows.index(row['show_title'])
            values = (row['country_iso2'], id+1, row['week'],
                      row['weekly_rank'], row['cumulative_weeks_in_top_10'])
            cur.execute(query_6, values)

        print('sucsesfull')

    conn.commit()
