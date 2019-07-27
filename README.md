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
| 28/07/2019  | PyCristoforo 2.0.0 published on PyPi  |


Table of contents
-----------------
- [Random Point generation](#random-point-generation)
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
![Germany Envelope Points KO](pycristoforo/resources/env_germ_p2.png?raw=true "Germany Envelope Points KO")

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
![Germany Envelope Points OK](pycristoforo/resources/env_germ_p1.png?raw=true "Germany Envelope Points OK")

As said above, the algorithm is very simple, but also very inefficient.

Benchmark:
* Country: "Germany"
* NumPoints: 100k
* Time: 4min 20sec

**Version 2**

In order to make the algorithm faster and more robust (https://codereview.stackexchange.com/questions/69833/generate-sample-coordinates-inside-a-polygon), v2 changes the way random points are generated:
-  country polygon is triangulated and the area of each triangle is then calculated;
-  for each sample:
  * pick the triangle 𝑡 containing the sample, using random selection weighted by the area of each triangle.
  * pick a random point uniformly in the triangle, as follows:
    * pick a random point 𝑥,𝑦 uniformly in the unit square.
    * If 𝑥+𝑦>1, use the point 1−𝑥,1−𝑦 instead. The effect of this is to ensure that the point is chosen uniformly in the unit right triangle  with vertices (0,0),(0,1),(1,0)
    * Apply the appropriate affine transformation to transform the unit right triangle to the triangle 𝑡.

The hard constraint of this method is that it works only for **convex polygons**, and therefore some points may be generated out of the country shape (convex hull).
![Germany Convex Hull Points KO](pycristoforo/resources/germ_hull_p3.png?raw=true "Germany Convex Hull Points KO")

All points are checked if lying inside the country shape.
For each point outside the country, a new one is generated.

![Germany Convex Hull Points KO](pycristoforo/resources/germ_hull_p4.png?raw=true "Germany Convex Hull Points KO")

This method almost 20% more faster on benchmark.

Benchmark:
* Country: "Germany"
* NumPoints: 100k
* Time: 3min 30sec

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
Current version: 2.0.0

[Changelog](CHANGELOG.rst)

License
-------
This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details

What Next
------------
* v2.1.0: random points printed in an external file
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
