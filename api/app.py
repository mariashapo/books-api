from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data as a dictionary
books = [
    {
        'id': 1,
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'publication_year': 1960,
        'genre': 'Southern Gothic'
    },
    {
        'id': 2,
        'title': '1984',
        'author': 'George Orwell',
        'publication_year': 1949,
        'genre': 'Dystopian Fiction'
    },
    {
        'id': 3,
        'title': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'publication_year': 1813,
        'genre': 'Romantic Novel'
    },
    {
        'id': 4,
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'publication_year': 1925,
        'genre': 'American Literature'
    },
    {
        'id': 5,
        'title': 'The Hunger Games',
        'author': 'Suzanne Collins',
        'publication_year': 2008,
        'genre': 'Young Adult Dystopian'
    }
]

@app.route('/books', methods=['GET'])
def get_books():
    genre = request.args.get('genre')
    author = request.args.get('author')
    title = request.args.get('title')

    filtered_books = []
    
    if genre or author or title:
        for book in books:
            genre_match = str.lower(genre) in str.lower(book['genre']) if genre else True
            author_match = str.lower(author) in str.lower(book['author']) if author else True
            title_match = str.lower(title) in str.lower(book['title']) if title else True

            # Add the book if it matches both genre and author criteria
            if genre_match and author_match and title_match:
                filtered_books.append(book)
    else:
        # If no filters are provided, use all books
        filtered_books = books

    return jsonify(filtered_books)

if __name__ == '__main__':
    app.run(debug=True)
