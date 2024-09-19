import unittest 
from unittest import TestCase
from price_discount import discount  


# more unit tests here. Each test should test one scenario
class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_four_prices(self):
        prices = [100, 96, 12, 5]
        expected_discount = 5
        self.assertEqual(expected_discount, discount(prices))

    def test_list_with_decimal_prices(self):
        prices = [10.50, 54.23, 4.01, 22.22]
        expected_discount = 4.01
        self.assertEqual(expected_discount, discount(prices))

    def test_list_with_two_prices(self):
        prices = [50, 65]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_with_empty_list(self):
        prices = []
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_strings(self):
        prices = ['cat', 'stairs', 'circle']
        self.fail('No strings allowed!')

    def test_list_zero_as_a_price(self):
        self.fail('Nothing should be free')
        # zero is a "falsy" in python
        # none is falsy in python

    def test_list_with_negative_prices(self):
        self.fail('Finish this test')

    def test_strings_that_look_like_numbers(self):
        self.fail('Finish this test')






if __name__ == '__main__':
    unittest.main()