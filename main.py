import time

def main():
    book_path = get_book_path()
    text = None
    start = time.time()

    try:
        with open(book_path) as f:
            text = f.read()
    except:
        print('File not found, please check the filename!')
        main()

    word_count = count_words(text)
    char_count = count_character(text)
    sorted_count = sort_dict(char_count)
    
    print(f"\n+++ Begin report of {book_path} +++\n")
    print(f"{word_count} words found in the text file\n")
    
    for key in sorted_count:
        print(f"The '{key}' character was found {sorted_count[key]} times")

    print(f"\n--- End report of {book_path} ---\n")
    end = time.time()
    print(f"Parsing time: {round(end - start, 3)} seconds!\n")
    parse_again()


def get_book_path():
        file_name = input("Please enter the file name you like to parse (e.g.'mytext.txt'):")
        book_path = f'./books/{file_name}'
        return book_path 


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

def count_words(text):
    text_list = text.split()
    return len(text_list)


def count_character(text):
    char_dict = {}
    text_list = text.split()
    for str in text_list:
        for char in str:
            low_char = char.lower()
            if low_char in char_dict:
                char_dict[low_char] += 1
            else:
                char_dict[low_char] = 1
    return char_dict


def sort_dict(char_count):
    tuple_list = list(char_count.items())
    tuple_list.sort(key=lambda c: c[1], reverse=True)
    sorted_dict = {}
    for key, value in tuple_list:
        if(key.isalpha()):
            sorted_dict[key] = value
        else:
            continue
    return sorted_dict


main()
