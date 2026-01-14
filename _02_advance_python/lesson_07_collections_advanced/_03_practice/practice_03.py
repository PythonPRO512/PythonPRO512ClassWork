from collections import Counter
import re


def count_words(text: str) -> Counter:
    text = text.lower()
    words = re.split(r'[-:;.,!? \n\t]+', text)
    # words.pop()
    return Counter(words)


if __name__ == '__main__':
    my_text = "Hello world! Hello Python. Python is great, world is big."
    result = count_words(my_text)
    print(result)
    new_text = """Ночь, улица, фонарь, аптека,
Бессмысленный и тусклый свет.
Живи ещё хоть четверть века —
Всё будет так. Исхода нет.
Умрёшь — начнёшь опять сначала
И повторится всё, как встарь:
Ночь, ледяная рябь канала,
Аптека, улица, фонарь"""
    new_result = count_words(new_text)
    print(new_result)
    # [0-9A-Za-zА-Яа-яЁё]