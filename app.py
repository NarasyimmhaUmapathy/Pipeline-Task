from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def db_connection():

    conn = None
    try:
        conn = sqlite3.connect("movies.sqlite")
    except sqlite3.Error as e:
        print(e)

    return conn

  
@app.route("/movies",methods=["GET","POST"])

def movies():
    conn = db_connection()
    cursor = conn.cursor() #to use sql queries
    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM movies")
        books = [
            dict(title=row[1],genre = [2], year = [3])
            for row in cursor.fetchall()
        ]
        if movies is not None:
            return jsonify(books) 

    if request.method == "POST":
        new_title = request.form["title"]
        new_genre = request.form["genre"]
        year = request.form["year"]
        sql = """INSERT INTO movies (title, genre, year )
                 VALUES (?,?,?)""" #parametrized query
        
        cursor = conn.execute(sql, (new_title,new_genre,year))
        conn.commit()   
        return "Movie {} added successfully".format(new_title)



app.run(port=5000) 