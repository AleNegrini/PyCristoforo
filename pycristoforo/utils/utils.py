import json
import pycristoforo.utils.constants as constants_py


def read_json(path: str) -> dict:
    """
    This method reads the file specified in
    :param path: resource path
    :return: json object
    """
    with open(path) as f:
        data = json.load(f)
    return data


def print_list(my_list: list):
    """
    This methods print the content of the list, with each element separated by a comma ','
    :param my_list: list of features to print
    :return: none
    """
    i = 0
    for item in my_list:
        if i == len(my_list)-1:
            print(json.dumps(item))
        else:
            print(json.dumps(item)+',')
        i += 1


def generate_comma_sep_country_list(full_path: str, acronym_path: str):
    """
    This is not a method useful for library. It can be run on spot when there is the need to re-generate the COUNTRIES.csv file
    :param full_path: geojson path with shapes
    :param acronym_path: target path
    :return: None
    """
    countries = read_json(full_path)
    with open(acronym_path, 'w') as writeFile:
        writeFile.write("Extended Name, ISO_A3\n")
        for elem in countries['features']:
            writeFile.write(elem['properties']['ADMIN']+","+elem['properties']['ISO_A3']+"\n")
    writeFile.close()


if __name__ == "__main__":
    generate_comma_sep_country_list(constants_py.Constants.EU_PATH, constants_py.Constants.ACRONYM_PATH)
