import sys


# I have decided not to count new lines as characters
def counting_characters(filename):
    with open(filename) as fh:
        counter = 0
        for line in fh:
            line = line.rstrip()
            for ch in line:
                counter += 1
    return counter


def counting_lines(filename):
    with open(filename) as fh:
        text = fh.read()
        counter = 0
        for ch in text:
            if ch == "\n":
                counter += 1
    return counter


def counting_words(filename):
    counter = 0
    with open(filename) as fh:
        for line in fh:
            list = line.split()
            words_in_line = len(list)
            counter += int(words_in_line)
    return counter


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
