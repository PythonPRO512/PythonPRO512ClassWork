"""
Задача: создайте модуль temperature_converter.py, который содержит функции:

celsius_to_fahrenheit(c) — переводит температуру из Цельсия в Фаренгейт.
fahrenheit_to_celsius(f) — переводит температуру из Фаренгейта в Цельсий.
kelvin_to_celsius(k) — переводит температуру из Кельвина в Цельсий.
Напишите программу, которая позволяет пользователю
выбрать тип конверсии и вводит температуру для преобразования.
"""


def celsius_to_fahrenheit(temp_c):
    return temp_c * 9 / 5 + 32


def fahrenheit_to_celsius(temp_f):
    return (temp_f - 32) * 5 / 9


def kelvin_to_celsius(temp_k):
    if temp_k < 0:
        return f'Это невозможно!'
    return temp_k - 273.15

