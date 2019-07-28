"""
    Setup file for pycristoforo.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 3.1.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyCristoforo",
    version="2.0.0",
    author="Alessandro",
    author_email="alessandro2.negrini@gmail.com",
    description="Python library for the generation of contestualized random coordinates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AleNegrini/PyCristoforo",
    packages=setuptools.find_packages(exclude='tests'),
    package_data={'pycristoforo': ['resources/*.geojson']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
