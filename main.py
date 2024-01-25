def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    word_count = get_number_of_words(text)
    print(f"{word_count} words found in the document\n")
    char_dict = get_letter_counts(text)
    print_letter_counts(char_dict)


def get_number_of_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def get_letter_counts(text):
    char_dict = {}
    text = text.lower()
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def print_letter_counts(char_dict):
    char_list = []
    for key in char_dict:
        if key.isalpha():
            char_list.append(key)
    char_list.sort()
    for char in char_list:
        print(f"The '{char}' character was found {char_dict[char]} times")

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

main()
