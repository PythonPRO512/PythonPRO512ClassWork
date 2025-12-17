import unittest


# from _02_advance_python.lesson_03_py_unittest._03_practice._01_app_discount.discount_funcs.discount_funcs import \
#         calculate_discount  # для запуска из файла

from discount_funcs.discount_funcs import calculate_discount # для запуска из корня


class TestCalculateDiscount(unittest.TestCase):
    def setUp(self):
        self.values = ['basic', 'silver', 'gold']

    def test_basic_discount(self):
        self.assertEqual(calculate_discount(self.values[0], 100), 95.0)

    def test_silver_discount(self):
        self.assertEqual(calculate_discount('silver', 100), 90.0)

    def test_gold_discount(self):
        self.assertEqual(calculate_discount('gold', 100), 85.0)

    def test_invalid_level(self):
        with self.assertRaises(ValueError):
            calculate_discount('platinum', 80)


if __name__ == '__main__':
    unittest.main()
