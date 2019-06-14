import json
import os
import unittest
from module.com.pycristoforo.utils.reader import read_json


class TestReader(unittest.TestCase):

    def test_path_join(self):
        self.assertEqual(os.path.join(os.path.dirname(__file__), 'resources/sample.json'),
                         '/Users/alessandro.negrini/Personal/code/pycristoforo/tests/resources/sample.json')

    def test_json_object_read(self):
        test_path = os.path.join(os.path.dirname(__file__), 'resources/sample.json')
        test_data = read_json(test_path)
        self.assertEqual(test_data['features'][0]['geometry']['type'], 'Point')
        self.assertEqual(test_data['features'][1]['geometry']['type'], 'LineString')
        self.assertEqual(test_data['features'][2]['geometry']['type'], 'Polygon')


if __name__ == '__main__':
    unittest.main()

    #testdata = open(TESTDATA_FILENAME).read()


    #print("sd")
