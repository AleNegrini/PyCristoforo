import json


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
