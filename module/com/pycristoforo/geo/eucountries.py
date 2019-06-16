from module.com.pycristoforo.utils.reader import read_json
from module.com.pycristoforo.geo.key_value_pair import KeyValuePair


class EUCountryList:

    def __init__(self, full_path):
        """
        Inizializer method that builds the country dictionary with 'key','value' pair
        :param full_path: path where the geojson is stored
        """
        self.__country_dict = {}
        countries = read_json(full_path)
        for elem in countries['features']:
            country = KeyValuePair(elem['properties']['FIPS'], elem['properties']['UN'])
            self.__country_dict[country.key] = country.value
            country = KeyValuePair(elem['properties']['ISO2'], elem['properties']['UN'])
            self.__country_dict[country.key] = country.value
            country = KeyValuePair(elem['properties']['ISO3'], elem['properties']['UN'])
            self.__country_dict[country.key] = country.value
            country = KeyValuePair(elem['properties']['NAME'], elem['properties']['UN'])
            self.__country_dict[country.key] = country.value
            country = KeyValuePair(elem['properties']['UN'], elem['geometry'])
            self.__country_dict[country.key] = country.value

    def get_by_key(self, key: str) -> int:
        try:
            return self.__country_dict[key]
        except KeyError as ex:
            print(f'No key {ex} in country dictionary')
            return None

    def get_country_dict(self):
        return self.__country_dict


if __name__ == '__main__':
    a = EUCountryList('../../../resources/eu_countries.json')
    f = a.get_uid("aa")
