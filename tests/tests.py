import os
import unittest
from module.com.pycristoforo.utils.reader import read_json
from module.com.pycristoforo.geo.eucountries import EUCountryList


class Tests(unittest.TestCase):

    dix = EUCountryList(os.path.join(os.path.dirname(__file__), 'resources/eu_countries.json'))

    def test_path_join(self):
        self.assertEqual(os.path.join(os.path.dirname(__file__), 'resources/sample.json'),
                         '/Users/alessandro.negrini/Personal/code/pycristoforo/tests/resources/sample.json')

    def test_json_object_read(self):
        test_path = os.path.join(os.path.dirname(__file__), 'resources/sample.json')
        test_data = read_json(test_path)
        self.assertEqual(test_data['features'][0]['geometry']['type'], 'Point')
        self.assertEqual(test_data['features'][1]['geometry']['type'], 'LineString')
        self.assertEqual(test_data['features'][2]['geometry']['type'], 'Polygon')

    def test_init(self):
        self.assertIsInstance(self.dix.get_country_dict(), dict)

    def test_get_id(self):
        self.assertEqual(self.dix.get_id("AJ"), 31)
        self.assertEqual(self.dix.get_id("AZ"), 31)
        self.assertEqual(self.dix.get_id("AZE"), 31)
        self.assertEqual(self.dix.get_id("Azerbaijan"), 31)
        self.assertRaisesRegex(KeyError, self.dix.get_id("AAAAAA"))


if __name__ == '__main__':
    unittest.main()
