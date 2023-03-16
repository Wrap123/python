import unittest
import city_functions


class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        full_info = city_functions.get_city_country_name('henan', 'nanyang')
        self.assertEqual(full_info, 'Henan, Nanyang')

    def test_city_country_population(self):
        full_info = city_functions.get_city_country_name('henan', 'nanyang', 5000000)
        self.assertEqual(full_info, 'Henan, Nanyang - Population 5000000')


if __name__ == '__main__':
    unittest.main()
