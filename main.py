import time
import cli_display
import parse

def parse_again():
    valid_prompt = False
    while not valid_prompt:
        prompt = input("Parse another file? 'y'[yes] or 'n'[no] :")
        if prompt == 'y':
            valid_prompt = True
            return main()
        elif prompt == 'n':
            valid_prompt = True    
            print('\nGood Bye!\n')
            return False
    return

def main():

    cli_display.show_all_books()

    book_path = cli_display.get_book_path()
    text = None
    start = time.time()

    try:
        with open(book_path) as f:
            text = f.read()
    except:
        print('File not found, please check the filename!')
        main()

    word_count = parse.count_words(text)
    char_count = parse.count_character(text)
    sorted_count = parse.sort_dict(char_count)
    
    print(f"\n+++ Begin report of {book_path} +++\n")
    print(f"{word_count} words found in the text file\n")
    
    for key in sorted_count:
        print(f"The '{key}' character was found {sorted_count[key]} times")

    print(f"\n--- End report of {book_path} ---\n")
    end = time.time()
    print(f"Parsing time: {round(end - start, 3)} seconds!\n")
    parse_again()


main()
