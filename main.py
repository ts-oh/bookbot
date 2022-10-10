book_path = "./books/frankenstein.txt"

def main():
    text = read_file(book_path)
    word_count = count_words(text)
    print(word_count)
    

def read_file(book_path):
    with open(book_path) as f:
        book_file = f.read()
        return book_file

def count_words(text):
    text_list = text.split()
    return len(text_list)

main()