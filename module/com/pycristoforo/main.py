from module.com.pycristoforo.utils.constants import Constants
from module.com.pycristoforo.geo.eucountries import EUCountryList
from shapely.geometry import Point, Polygon, MultiPolygon
from numpy.random import uniform

def main(key: str):

    # reading
    country_ids = EUCountryList(Constants.EU_PATH)
    uid = country_ids.get_by_key(key)
    shape_dict = country_ids.get_by_key(uid)

    # create shape
    if shape_dict['type'] == "MultiPolygon":
        shape = MultiPolygon(shape_dict['coordinates'][0])
    else:
        if shape_dict['type'] == "Polygon":
            shape = Polygon(shape_dict['coordinates'][0])
        else:
            print("Other")

    #print(shape_dict)
    generate_random(shape, 100)

def generate_random(shape, points: int):
    min_lng = shape.bounds[0]
    min_lat = shape.bounds[1]
    max_lng = shape.bounds[2]
    max_lat = shape.bounds[3]
    i = 0
    while i != points:
        val1 = uniform(min_lng, max_lng)
        val2 = uniform(min_lat, max_lat)
        random_point = Point(val1, val2)
        if random_point.within(shape):
            print(
                '{"type": "Feature","geometry": {"type": "Point","coordinates": ['+str(val1)+','+str(val2)+']},"properties": {"prop0": "value0","prop1": { "this": "that" }}},'
            )
            i = i+1
    print("")

if __name__ == '__main__':
    main("BK")


