import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycristoforo",
    version="0.1",
    author="Alessandro Negrini",
    author_email="alessandro2.negrini@gmail.com",
    description="Random contestualized latitude and longitude generator by country",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AleNegrini/pycristoforo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
