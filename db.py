import sqlite3

conn = sqlite3.connect("movies.sqlite")

cursor = conn.cursor()
sql_query = """ CREATE TABLE movies (


    title  text NOT NULL,
    genre  text NOT NULL,
    year  integer NOT NULL

)"""

cursor.execute(sql_query)
