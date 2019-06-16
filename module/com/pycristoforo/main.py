from geojson import Point
import json


def main():
    with open('germany.geojson') as f:
        data = json.load(f)

    # construct point based on lat/long returned by geocoder
    point = Point(45.4519896, -122.7924463)


def get_shape(iso_name):
    """
    It is in charge of building and returning the shape object
    :param iso_name: ISO country name
    :return: it returns the object shape, according to the country name
    """

def read_json


if __name__ == '__main__':
    main()

