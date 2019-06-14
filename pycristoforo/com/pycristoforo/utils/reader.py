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
