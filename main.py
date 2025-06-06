from stats import get_character_count
from stats import get_word_count
from stats import sort_dictionary
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    character_count = get_character_count(get_book_text(sys.argv[1]))

    sorted_list = sort_dictionary(character_count)

    print("============ BOOKBOT ============")

    print(f"Analyzing book found at {sys.argv[1]}")

    print("----------- Word Count ----------")

    print(f"Found {get_word_count(get_book_text(sys.argv[1]))} total words")

    for dict in sorted_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")

    print("============= END ===============")


main()