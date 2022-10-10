book_path = "./books/frankenstein.txt"

with open(book_path) as f:
    book_file = f.read()
    print(book_file)
