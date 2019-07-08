class KeyValuePair:

    key = ''
    value = 0

    def __init__(self, key: str, value: int):
        """
        Constructor method
        :param key: dictionary key
        :param value: dictionary value
        """
        self.key = key.lower()
        self.value = value
