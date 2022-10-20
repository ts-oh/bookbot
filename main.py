book_path = "./books/frankenstein.txt"

def main():
    text = read_file(book_path)
    get_word_count = count_words(text)
    get_char_count = count_character(text)
    get_print = display_output(get_char_count)
    
    print(get_word_count) 
    
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
            char = char.lower()
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def display_output(get_char_count):
    char_dict = get_char_count
    for char in char_dict:
        if(char.isalpha()):
            char_value = char_dict[char]
            print(f"The '{char}' character was found {char_value} times")
        else:
            continue
main()
