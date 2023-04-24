from os import listdir

def show_all_books():
    list_books = listdir('./books')
    print("\n*** List Books txt in the directory ***\n")
    for index, book in enumerate(list_books):
        print(f"{index}. {book}")
    print("\n*** End of books list ***\n")


def get_book_path():
    file_name = input("Please enter the file name you like to parse (e.g.'mytext.txt'):")
    book_path = f'./books/{file_name}'
    return book_path
