import psycopg2

## Connect to database using psycopg2
connect = psycopg2.connect(database="fulfil", user="postgres", password="postgres", host="127.0.0.1", port="5432")