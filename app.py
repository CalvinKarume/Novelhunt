from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///novelhunt.db'  # SQLite database for simplicity
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255))
    synopsis = db.Column(db.Text)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables
    app.run(host='0.0.0.0', port=5000, debug=True)

# ... (previous code)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    books = Book.query.filter(Book.title.contains(query) | Book.author.contains(query)).all()
    return jsonify([book.to_dict() for book in books])

@app.route('/recommend', methods=['POST'])
def recommend():
    book_id = request.json['book_id']
    book = Book.query.get(book_id)
    if book:
        similar_books = Book.query.filter(Book.genre == book.genre).all()
        return jsonify([book.to_dict() for book in similar_books])
    else:
        return jsonify({'error': 'Book not found'}), 404

# ... (remaining code)

class Book(db.Model):
    # ... (previous code)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'genre': self.genre,
            'synopsis': self.synopsis
        }

