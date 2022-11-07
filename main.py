import time

def main():
    book_path = get_book_path()
    text = None
    start = time.time()

    try:
        with open(book_path) as f:
            text = f.read()
    except:
        print('not found')
        main()

    word_count = count_words(text)
    char_count = count_character(text)
    sorted_count = sort_dict(char_count)
    
    print()
    print(f"+++ Begin report of {book_path} +++")
    print()
    print(f"{word_count} words found in the text file")
    print()
    
    for key in sorted_count:
        print(f"The '{key}' character was found {sorted_count[key]} times")

    print()
    print(f"--- End report of {book_path} ---")
    print()
    end = time.time()
    print(f"Parsing time: {round(end - start, 3)} seconds!")
    
    parse_again()
 

def get_book_path():
        file_name = input("Please enter the file name you like to parse (e.g.'mytext.txt'):")
        book_path = f'./books/{file_name}'
        return book_path 


def parse_again():
    prompt = input("Parse another file? 'y'[yes] or 'n'[no] :")
    if prompt == 'y':
        return main()
    elif prompt == 'n':
        print()
        print('Good Bye!')
        return print()
    else:
        parse_again()


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
