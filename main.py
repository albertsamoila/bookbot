from stats import get_number_of_words, get_number_of_characters, get_sorted_list_of_characters
import sys

def get_book_text(filepath: str):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def nice_print(filepath: str, wordcount: int, sorted_list: list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for dictionary in sorted_list:
        if dictionary["name"].isalpha():
            print(f"{dictionary["name"]}: {dictionary["num"]}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_of_words = get_number_of_words(book_text)
    characters = get_number_of_characters(book_text)
    sorted_list = get_sorted_list_of_characters(characters)
    nice_print(filepath, num_of_words, sorted_list)

main()
