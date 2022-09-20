import json
with open('books.json', 'r') as f:
    books_list = json.load(f)
for book in books_list:
        print(f"Book Title: {book['Title']}")