# PyCristoforo

**Note: PyCristoforo is not yet available on PyPi**

The new python library for the generation of **contestualized random** coordinates.
PyCristoforo takes in input a country name (in version 1.0, only European Countries) and it generates random coordinates, inside that country (not including the sea/ocean sections).

Table of contents
-----------------
- [Description](#description)
- [Requirements](#requirements)
- [Install](#install)
- [Usage](#usage)
- [Running tests](#running-tests)
- [ChangeLog](#changelog)
- [License](#license)
- [What next](#what-next)
- [Authors](#authors)
- [Notes](#notes)

Description
-----------

Work in progress

Requirements
------------
* numpy v1.16.4
* Shapely v1.6.4.post2

Details [here](https://github.com/AleNegrini/PyCristoforo/blob/develop/requirements.txt)

Resources
---------
* Europen countries geoJSON ([link](https://github.com/AleNegrini/PyCristoforo/blob/develop/COUNTRIES.csv))

Install
-------
PyCristoforo is very easy to install and use
```
pip install pycristoforo
```

Usage
-------

* Now you can import it in your script:
```
import pycristoforo as pyc
```

* You can now load the geojson of the country you'd like to generate geocoordinates in:
```
country = pyc.get_shape("Italy")
```
The supported input for `get_shape` method are not only the extended country names: you can either use `FIPS`, `ISO2` or `ISO3` code.
[Here](https://github.com/AleNegrini/PyCristoforo/blob/develop/COUNTRIES.csv) you can find the supported input (country_name, FIPS, ISO2, ISO3).
Method is case insensitive:
```
country = pyc.get_shape("ITALY")
```
is the same as:
```
country = pyc.get_shape("italy")
```

`country` var contains now the shape of the country passed in input (usually a `shapely Poligon`or `MultiPoligon`):
```
MULTIPOLYGON (((12.127777 47.00166300000012, 12.13611 46.966942, 12.16027600000012 46.92805, 12.18138900000014 46.909721, 12.189722 46.90610500000014, 12.232222 46.888885, 12.301666 46.84111, 12.378611 46.72666, 12.38888700000012 46.715553, ... , 12.047777 36.753052, 12.03833200000014 36.747215, 12.027777 36.74222, 12.01583 36.738327)))
```

* Now that country shape has been loaded, it's time to get `n` random geocoordinates.
Suppose to generate 100 geocoordinates:
```
points = geoloc_generation(country, 100, "Italy")
```

`points` is a list of Points:
```
00 = {dict} {'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [13.963703154465053, 42.591335534115316]}, 'properties': {'point': 1, 'country': 'Italy'}}
01 = {dict} {'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [11.659857182901725, 43.95787059805974]}, 'properties': {'point': 2, 'country': 'Italy'}}
02 = {dict} {'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [7.992769814920238, 45.89632889069682]}, 'properties': {'point': 3, 'country': 'Italy'}}
...
99 = {dict} {'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [6.112769314920238, 45.45632889569111]}, 'properties': {'point': 100, 'country': 'Italy'}}
```

You can now iterate through the list and make good use of them.

* A utility method is the `get_envelope` one:
```
env = pyc.get_envelope(country)
```

Running tests
-------------
Work in progress

ChangeLog
---------
Current version: 1.0

[Changelog](https://github.com/AleNegrini/PyCristoforo/blob/develop/CHANGELOG.rst)

License
-------
This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details


What Next
------------
* v1.1 : us countries support
* v1.2 : American countries support
* v1.3 : Asian + Australia countries support
* v1.4 : African countries support
* v2.0 : random coordinates generation method will be enhanced

After release 2.0, I wish to add support for counties and cities.

Authors
-------
* **Alessandro Negrini** - *Initial work* - [Github profile](https://github.com/AleNegrini)

See also the list of [contributors](https://github.com/AleNegrini/PyCristoforo/blob/develop/AUTHORS.rst) who participated in this project.

Notes
-----
This project has been set up using PyScaffold 3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
