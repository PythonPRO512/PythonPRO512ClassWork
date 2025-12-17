# from _02_advance_python.lesson_03_py_unittest._03_practice._02_app_count_puncts.count_puncts.count_puncts import \
#     count_punct_marks

from count_puncts.count_puncts import \
    count_punct_marks


def test_empty_string():
    assert count_punct_marks('') == 0


def test_no_punctuation():
    assert count_punct_marks('Hello world') == 0


def test_single_punctuation(string_for_test):
    assert count_punct_marks(string_for_test) == 1


def test_multiple_punctuation():
    assert count_punct_marks('Hello, World! How are you?') == 3


def test_edge_case():
    assert count_punct_marks('!!!') == 3


def test_all_punctuation():
    assert count_punct_marks(",.:;'!?") == 7
