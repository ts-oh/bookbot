book_path = "./books/frankenstein.txt"

def main():
    text = read_file(book_path)
    word_count = count_words(text)
    char_count = count_character(text)
    sorted_count = sort_dict(char_count)
    
    print()
    print(f"+++ Begin report of {book_path} +++")
    print()
    print(f"{word_count} found in the document")
    print()
    
    for key in sorted_count:
        print(f"The '{key}' character was found {sorted_count[key]} times")
    
    print()
    print(f"--- End report of {book_path} ---")
    print()
    
def read_file(book_path):
    with open(book_path) as f:
        book_file = f.read()
        return book_file

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
    # convert dictionary into a tuple
    tuple_list = list(char_count.items())
    
    # sort tuple by second element (.sort() mutates original data) reverse sorting so it is descending
    tuple_list.sort(key=lambda c: c[1], reverse=True)

    # add sorted tuple list to a dictionary only if it is alphabet character
    sorted_dict = {}
    for key, value in tuple_list:
        if(key.isalpha()):
            sorted_dict[key] = value
        else:
            continue
    
    return sorted_dict
  
main()

