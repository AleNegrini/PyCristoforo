import unittest
import csv
import pycristoforo as pyc
import shapely
import time


class TestStringMethods(unittest.TestCase):

    country_list = []
    with open('../resources/COUNTRIES.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[1] != ' ISO_A3':
                country_list.append(row[0])
    """
        def test_get_shape(self):
        for item in self.country_list:
            country = pyc.get_shape(item)
            print("Testing "+item)
            assert(isinstance(country, shapely.geometry.multipolygon.MultiPolygon) or
                   isinstance(country, shapely.geometry.polygon.Polygon))
    """

    def test_get_1_geoloc(self):
        test_cases = [1, 10, 100, 1000]
        for item in self.country_list:
            for case in test_cases:
                country = pyc.get_shape(item)
                start_time = time.time()
                points = pyc.geoloc_generation(country, case, item)
                elapsed_time = time.time() - start_time
                print(item+" took "+str(elapsed_time)+"s for generating "+str(case)+" random geocoordinate")


if __name__ == '__main__':
    unittest.main()
