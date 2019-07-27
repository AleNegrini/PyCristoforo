# PyCristoforo

**v2.0.0**

The new python library for the generation of **contestualized random** coordinates.
PyCristoforo takes in input a country name and it generates random coordinates, inside that country (not including the sea/ocean sections).

**Python version supported: 3.6, 3.7**

Latest updates
-----------------

| Date          |   Description |
| ------------- | ------------- |
| 30/06/2019  | PyCristoforo 1.0.0 published on PyPi  |
| 08/07/2019  | PyCristoforo 1.0.0.post4 published on PyPi  |
| 09/07/2019  | PyCristoforo 1.1.0 published on PyPi  |
| 27/07/2019  | PyCristoforo 2.0.0 published on PyPi  |


Table of contents
-----------------
- [Description](#description)
- [Requirements](#requirements)
- [Install](#install)
- [Usage](#usage)
- [Build](#build)
- [Running tests](#running-tests)
- [ChangeLog](#changelog)
- [License](#license)
- [What next](#what-next)
- [Authors](#authors)
- [Notes](#notes)

Random Point generation
-----------
In this section you can find some details about random coordinates generation method.

**Version 1**
PyCristoforo v1 implements a very simple algorithm for random point generation:
- starting from the country Polygon shape, it first gets the rectangle around it and then the min/ max latitudes and longitude.
```
# getting min, max lat/lng
min_lng = get_min_lng(shape)
min_lat = get_min_lat(shape)
max_lng = get_max_lng(shape)
max_lat = get_max_lat(shape)
```
![Germany Envelope](pycristoforo/resources/env_germ.png?raw=true "Germany Envelope")


- inside it, the random coordinates are generated in a uniform way
```
# generate random float between [min_lng, max_lng)
val1 = numpy_random.uniform(min_lng, max_lng)
# generate random float between [min_lat, max_lat)
val2 = numpy_random.uniform(min_lat, max_lat)
```

- finally, only the points inside the country shape are kept, the ones outside are discarded.
New points are then generated until reaching the user expected number.
```
# random point generation
while counter != points:
  if random_point.within(shape):
    ...
    list_of_points.append(ran_point)
    counter += 1
```

As said, the algorithm is very simple, but also very inefficient.

Benchmark:
* Country: "Italy"
* NumPoints: 10k
* Time:

**Version 2**


Requirements
------------
* numpy v1.16.4
* Shapely v1.6.4.post2

Details [here](requirements.txt)

Resources
---------
* World countries geoJSON ([link](https://datahub.io/core/geo-countries#resource-countries))

Install
-------
PyCristoforo is very easy to install and use (please be sure to have installed dependencies (section 'Requirements')
```
pip3 install pycristoforo
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
The supported input for `get_shape` method are not only the extended country names: you can either use `ISO_A3` code.
[Here](COUNTRIES.csv) you can find the supported input (country_name, ISO_A3).
Method is case insensitive:
```
country = pyc.get_shape("ITALY")
```
behaves the same as:
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
points = pyc.geoloc_generation(country, 100, "Italy")
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

* Print what you just generated:
```
geoloc_print(points, ',')
```

* A utility method is the `get_envelope` one:
```
env = pyc.get_envelope(country)
```

Build
------
```
python3 setup.py sdist bdist_wheel
```

Running tests
-------------
Work in progress

ChangeLog
---------
Current version: 1.1.0

[Changelog](CHANGELOG.rst)

License
-------
This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details

What Next
------------
* v3.0.0: regions support
* v3.1.0: counties support
* v3.2.0: cities support

Authors
-------
* **Alessandro Negrini** - *Initial work* - [Github profile](https://github.com/AleNegrini)

See also the list of [contributors](AUTHORS.rst) who participated in this project.

Notes
-----
This project has been set up using PyScaffold 3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
