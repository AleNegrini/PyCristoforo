import logging
from xml.dom import NotFoundErr

import geopandas as geopd

class WorldCountriesBoundaries:

    _WORLD_COUNTRIES_BOUNDARIES_FILE_PATH = "world-administrative-boundaries.zip"
    _COUNTRY_NAME_COLUMN = "name"
    _ISO3_COLUMN = "iso3"
    _GEOMETRY_COLUMN = "geometry"

    def __init__(self):
        self.__columns_to_keep = [
            self._COUNTRY_NAME_COLUMN,
            self._ISO3_COLUMN,
            self._GEOMETRY_COLUMN
        ]
        self.__shapes: geopd.GeoDataFrame = self.__load()

    def __load(self) -> geopd.GeoDataFrame:
        try:
            shapes_df = geopd.read_file(
                "resources/"+self._WORLD_COUNTRIES_BOUNDARIES_FILE_PATH,
                columns=self.__columns_to_keep
            )
            shapes_df[self._COUNTRY_NAME_COLUMN] = shapes_df[self._COUNTRY_NAME_COLUMN].str.lower()
            shapes_df[self._ISO3_COLUMN] = shapes_df[self._ISO3_COLUMN].str.lower()
            return shapes_df
        except FileNotFoundError:
            logging.error("The World Administrative Boundaries file was not found. Contact the library administrator to fix the issue")
        except Exception as e:
            logging.error("An error occurred while reading the World Administrative Boundaries file: " + str(e))

    def get_boundaries_by_country_name(self, country_name: str) -> geopd.GeoSeries:
        country_name = country_name.lower()
        if country_name in self.__shapes[self._COUNTRY_NAME_COLUMN].values:
            return self.__shapes[self.__shapes[self._COUNTRY_NAME_COLUMN] == country_name][self._GEOMETRY_COLUMN]
        raise NotFoundErr("Key "+country_name+" not found as country name")

    def get_boundaries_by_iso_code(self, iso3_code: str) -> geopd.GeoSeries:
        iso3_code = iso3_code.lower()
        if iso3_code in self.__shapes[self._ISO3_COLUMN].values:
            return self.__shapes[self.__shapes[self._ISO3_COLUMN] == iso3_code][self._GEOMETRY_COLUMN]
        raise NotFoundErr("Key " + iso3_code + " not found as iso code")