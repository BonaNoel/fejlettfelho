import os
from flask import Flask, jsonify, request
from openai import OpenAI


app = Flask(__name__)
os.environ["OPENAI_API_KEY"] = ""

# Példa adatok
books = [
    {'id': 1, 'title': '1984', 'author': 'George Orwell'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
    {'id': 3, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'}
]

# Összes könyv lekérése
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Egy könyv lekérése ID alapján
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is not None:
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404

@app.route('/books', methods=['POST'])
def getByPost():
    data = request.json
    question = data.get('question')
    language = data.get('language')
    model_name = data.get('model_name')
    print(question)
    print(language)
    print(model_name)
    
    return jsonify(books)

@app.route('/ai', methods=['POST'])
def getAiByPost():
    data = request.json
    question = data.get('question')
    language = data.get('language')
    model_name = data.get('model_name')
    system_prompt = "Allways answer in " + language
    client = OpenAI()

    completion = client.chat.completions.create(
    model=model_name,
    messages=[{
        "role": "user",
        "content": question
    }, {
        "role": "system",
        "content": system_prompt
    }]
)

    print(completion.choices[0].message.content)
    
    return completion.choices[0].message.content


if __name__ == '__main__':
    app.run(debug=True)