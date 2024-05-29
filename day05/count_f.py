def counting_characters(filename):
    with open(filename) as fh:
        counter = 0
        for line in fh:
            line = line.rstrip()
            for ch in line:
                counter += 1
    return counter


def counting_lines(filename):
    counter = 0
    with open(filename) as fh:
        for line in fh:
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