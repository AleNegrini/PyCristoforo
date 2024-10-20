import logging
from xml.dom import NotFoundErr

import geopandas as geopd

class OceansBoundaries:

    _OCEANS_FILE_PATH = "World_Seas_IHO_v1.zip"
    _SEA_NAME_COLUMN = "NAME"
    _GEOMETRY_COLUMN = "geometry"

    def __init__(self):
        self.__columns_to_keep = [
            self._SEA_NAME_COLUMN,
            self._GEOMETRY_COLUMN
        ]
        self.__shapes: geopd.GeoDataFrame = self.__load()

    def __load(self) -> geopd.GeoDataFrame:
        try:
            shapes_df = geopd.read_file(
                "resources/"+self._OCEANS_FILE_PATH,
            )
            shapes_df[self._SEA_NAME_COLUMN] = shapes_df[self._SEA_NAME_COLUMN].str.lower()
            return shapes_df
        except FileNotFoundError:
            logging.error("The World Administrative Boundaries file was not found. Contact the library administrator to fix the issue")
        except Exception as e:
            logging.error("An error occurred while reading the World Administrative Boundaries file: " + str(e))

    def get_boundaries_by_sea_name(self, name: str) -> geopd.GeoSeries:
        sea_name = name.lower()
        if sea_name in self.__shapes[self._SEA_NAME_COLUMN].values:
            return self.__shapes[self.__shapes[self._SEA_NAME_COLUMN] == sea_name][self._GEOMETRY_COLUMN]
        raise NotFoundErr("Key "+sea_name+" not found as sea name")