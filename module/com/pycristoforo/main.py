from module.com.pycristoforo.geo.shape import generate_random, setup_shape
from module.com.pycristoforo.utils.utils import print_list


def main(key: str, num: int):

    shape = setup_shape(key)
    a = generate_random(shape, num, key)

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

    print_list(a)


if __name__ == '__main__':
    main("Italy", 200)


