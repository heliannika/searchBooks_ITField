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
    # Käyttäjän syöttämän hakusana
    query = request.args.get('query')

    # Palauttaa tyhjän listan, jos hakusanaa ei ole
    if not query:
        return jsonify([])
    
    cursor = db_connection.cursor(dictionary=True)

    # Tarkistetaan onko käyttäjän hakusana subgenre
    cursor.execute("SELECT id FROM subgenres WHERE subgenre LIKE %s", (f"%{query}%",))
    subgenre_results = cursor.fetchall()

    if subgenre_results:
        # Jos subgenre löytyy, haetaan kaikki kirjat, jotka liittyy siihen
        subgenre_id = subgenre_results[0]['id']
        cursor.execute("""
            SELECT books.book, books.description, books.author, subgenres.subgenre
            FROM books
            JOIN booksintosubgenres ON booksintosubgenres.book_id = books.id
            JOIN subgenres ON booksintosubgenres.subgenre_id = subgenres.id
            WHERE subgenres.id = %s
        """, (subgenre_id,))
        results = cursor.fetchall()
    else:
        # Jos hakusanalla ei löydy kokonaista subgenree, niin etsitään hakusanaan sopivat kirjat
        cursor.execute("SELECT book, description, author FROM books WHERE book LIKE %s", (f"%{query}%",))
        results = cursor.fetchall()
        # Viimeisimpänä etsitään kirjailijan mukaan, jos aiemmat ehdot ei täyty
        if not results:
            cursor.execute("SELECT book, description, author FROM books WHERE author LIKE %s", (f"%{query}%",))
            results = cursor.fetchall()

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)