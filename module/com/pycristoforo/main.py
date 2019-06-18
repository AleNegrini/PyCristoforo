from module.com.pycristoforo.utils.constants import Constants
from module.com.pycristoforo.geo.eucountries import EUCountryList
from shapely.geometry import Polygon, MultiPolygon
from module.com.pycristoforo.geo.shape import generate_random


def main(key: str):

    # reading
    country_ids = EUCountryList(Constants.EU_PATH)
    uid = country_ids.get_by_key(key)
    shape_dict = country_ids.get_by_key(uid)

    # create shape
    poligons = []
    if shape_dict['type'] == "MultiPolygon":
        for polygon in shape_dict['coordinates']:
            for sub_polygon in polygon:
                pol = Polygon(sub_polygon)
                poligons.append(pol)
        shape = MultiPolygon(poligons)
    else:
        if shape_dict['type'] == "Polygon":
            shape = Polygon(shape_dict['coordinates'][0])
        else:
            print("Other")

    for s in shape:
        string = str(s.envelope).  \
              replace('POLYGON', '').\
              replace('(', '[').\
              replace(',', '],[').\
              replace(' [[', '[[').\
              replace(' 4', ',4'). \
              replace(' 3', ',3'). \
            replace(' 1', ',1'). \
            replace(' 2', ',2'). \
            replace(' 5', ',5'). \
            replace(' 6', ',6'). \
            replace(' 7', ',7'). \
            replace(' 8', ',8'). \
            replace(' 9', ',9'). \
            replace('[,','[').\
            replace('))', ']]')
        print('{ "type": "Feature","geometry": {"type": "Polygon","coordinates": ['+string+']},"properties": {"prop0": "value0","prop1": {"this": "that"}}},')

    a = generate_random(shape, 500, key)
    print("")


if __name__ == '__main__':
    main("Spain")


