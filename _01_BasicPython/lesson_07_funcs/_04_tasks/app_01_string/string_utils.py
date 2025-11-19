"""
Уровень 2: Средний

Задача: создайте модуль string_utils.py, который содержит функции для работы со строками:

reverse_string(text) — возвращает перевёрнутую строку.
count_vowels(text) — возвращает количество гласных букв в строке.
is_palindrome(text) — проверяет, является ли строка палиндромом (читается одинаково в обоих направлениях).
Напишите основную программу, которая импортирует этот модуль и предоставляет
 пользователю выбор функции для работы со строкой.
"""


def reverse_string(text):
    return text[::-1]


def count_vowels(text):
    vowels_counter = 0
    vowels = "aeiouAEIOUуеыаоэяиюУЕЫАОЭЯИЮ"
    for char in text:
        if char in vowels:
            vowels_counter += 1
    return vowels_counter


def is_palindrome(text):
    text = text.replace(' ', '').lower()
    return text == text[::-1]
