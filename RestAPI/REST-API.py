from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {"id": 1, "title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams"},
    {"id": 2, "title": "Pride and Prejudice", "author": "Jane Austen"},
]

@app.route('/books', methods=['GET'])
def get_all_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = [b for b in books if b['id'] == book_id]
    if book:
        return jsonify(book[0])
    else:
        return jsonify({"message": "Book not found"}), 404  

@app.route('/books', methods=['POST'])
def add_book():
    content = request.get_json()  
    if content and 'title' in content and 'author' in content:
        new_book = {"id": len(books) + 1, **content} 
        books.append(new_book)
        return jsonify(new_book), 201  
    else:
        return jsonify({"message": "Missing required fields"}), 400  

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    content = request.get_json()
    if content and 'title' in content and 'author' in content:
        for i, book in enumerate(books):
            if book['id'] == book_id:
                books[i] = {"id": book_id, **content}  
                return jsonify(books[i])
        return jsonify({"message": "Book not found"}), 404  
    else:
        return jsonify({"message": "Missing required fields"}), 400  

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for i, book in enumerate(books):
        if book['id'] == book_id:
            del books[i]
            return jsonify({"message": "Book deleted"})
    return jsonify({"message": "Book not found"}), 404  

if __name__ == '__main__':
    app.run(debug=True)
