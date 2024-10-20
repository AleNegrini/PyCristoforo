import json
from typing import List

from geopandas import GeoDataFrame, GeoSeries
from shapely import Point

from world_countries_boundaries.oceans_boundaries import OceansBoundaries
from world_countries_boundaries.world_countries_boundaries import WorldCountriesBoundaries

def get_shape(country: str = None,
                iso_code: str = None) -> GeoSeries:
    if iso_code:
        return OceansBoundaries().get_boundaries_by_sea_name(iso_code)
    if country:
        return OceansBoundaries().get_boundaries_by_sea_name(country)
    raise Exception("Either country or iso code should be passed as argument")

def generate_points(country: str = None,
                    iso_code: str = None,
                    samples: int = 10
                    ) -> List[Point]:
    if iso_code:
        return list(OceansBoundaries().get_boundaries_by_sea_name(iso_code).sample_points(samples).explode())
    if country:
        return list(OceansBoundaries().get_boundaries_by_sea_name(country).sample_points(samples).explode())
    raise Exception("Either country or iso code should be passed as argument")

def get_envelope(shape: GeoSeries):
    """
    It returns the envelope built on top the shape passed as input
    :param shape: Polygon or Multipolygon
    :return: shape envelope
    """
    return shape.envelope

if __name__ == "__main__":
    # print(get_envelope(get_shape('italy')))
    print(generate_points(country="South Pacific Ocean", samples=100))
