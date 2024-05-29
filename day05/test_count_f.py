import count_f


def test_words():
    result = count_f.counting_words("text_for_tests.txt")
    assert result == 9

def test_lines():
    result = count_f.counting_lines("text_for_tests.txt")
    assert result == 5

def test_ch():
    result = count_f.counting_characters("text_for_tests.txt")
    assert result == 45