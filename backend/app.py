from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Tietokantayhteys

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="booksfromitfield"
)

# Haetaan kirjat käyttäjän hakutietojen mukaan

@app.route('/api/search', methods=['GET'])
def search():
    # Käyttäjän syöttämän hakusanan haku
    query = request.args.get('query')
    cursor = db_connection.cursor(dictionary=True)

    # Haetaan tietokannoista tiedot hakusanan mukaan
    cursor.execute("""
        SELECT books.book, books.description, books.author, booksintosubgenres.subgenre_id
        FROM books
        JOIN booksintosubgenres ON books.id = booksintosubgenres.book_id
        WHERE books.book LIKE %s
    """, (f"%{query}%",))

    results = cursor.fetchall()
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)