import pycristoforo.utils.utils as utils_py
import pycristoforo.geo.key_value_pair as keyvaluepair_py


class CountryList:

    def __init__(self, full_path):
        """
        Constructor method that builds the country dictionary with 'key','value' pair
        :param full_path: path where the geojson is stored
        """
        self.__country_dict = {}
        uid: int = 0
        countries = utils_py.read_json(full_path)
        for elem in countries['features']:
            uid += 1
            country = keyvaluepair_py.KeyValuePair(elem['properties']['ADMIN'].lower(), str(uid))
            self.__country_dict[country.key] = country.value
            country = keyvaluepair_py.KeyValuePair(elem['properties']['ISO_A3'].lower(), str(uid))
            self.__country_dict[country.key] = country.value
            country = keyvaluepair_py.KeyValuePair(str(uid), elem['geometry'])
            self.__country_dict[country.key] = country.value

    def get_by_key(self, key: str) -> int:
        """
        It returns the element with a given key of the private dictionary
        :param key: dict key
        :return: dict element
        """
        try:
            return self.__country_dict[key.lower()]
        except KeyError as ex:
            print(f'No key {ex} in country dictionary')
            return None

    def get_country_dict(self):
        """
        Getter method for private attribute "country_dict"
        :return: dictionary of countries
        """
        return self.__country_dict
