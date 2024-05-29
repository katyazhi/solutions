import sys
from count_f import counting_characters, counting_lines, counting_words

def main():
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} FILENAME")

    filename = sys.argv[1]

    characters_counter = counting_characters(filename)
    lines_counter = counting_lines(filename)
    words_counter = counting_words(filename)

    print(
        f"Number of characters including spaces in your file is {characters_counter}.\nNumber of lines in your file is {lines_counter}.\nNumber of words in your file is {words_counter}."
    )


main()
