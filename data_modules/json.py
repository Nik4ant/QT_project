import ujson


def load_raw_json_from_file(filename: str) -> str:
    """
    Method return raw json from file.
    (This method exists to avoid using long
    constructs for opening -> reading -> closing a file)

    :param filename: Name of .json file
    :return: Raw json
    """
    with open(filename, mode='r', encoding="utf-8") as file:
        return file.read()


def load_json_data_from_file(filename: str) -> any:
    """
    Method load json data from file by given filename

    :param filename: Name of file
    :return: Deserialized data from file
    """
    with open(filename, mode='r', encoding="utf-8") as file:
        file_data = file.read()
        # To avoid exception from ujson
        if not file_data:
            return {
                "boards": []
            }
        result = ujson.loads(file_data)

    return result


def parse_json(json: str) -> any:
    """
    Method parse given json to python's data types

    :param json: Json to parse
    :return: Parsed data
    """
    # To avoid exception from ujson
    if not json:
        return {
            "boards": []
        }
    return ujson.loads(json)


def format_json(json: str) -> str:
    """
    Method formats given json
    :param json: Input json
    :return: Formatted json
    """
    return json.replace(' ', '').replace('\t', '').replace('\n', '')


def get_json_by_data(data: any) -> str:
    """
    Method return json representation for given data
    :param data: Given data
    :return: Json for given data
    """
    return ujson.dumps(data)


def save_json_data_to_file(filename: str, json_data: dict) -> None:
    """
    Method load json data from file by given filename

    :param filename: Name of file
    :param json_data: New data for saving
    """
    with open(filename, mode='w', encoding="utf-8") as file:
        file.seek(0)
        file.write(ujson.dumps(json_data))


def can_combine_boards_jsons(json_device: str, json_database: str) -> bool:
    """
    Method return True if we can combine 2 boards jsons and false if not

    :param json_device: Json from device
    :param json_database: Json from database
    :return: True or False
    """
    return len(json_database) == 0 and len(json_device) != 0


def combine_boards_jsons(json1: str, json2: str) -> list:
    """
    Method combine 2 json strings and deserialize them

    :param json1: First json string
    :param json2: Second json string
    :return: Combined json strings and deserialized data in one list.
             First element - json string, second element - deserialized data
    """

    # In this case parse_json will return list,
    # because json1 and json2 are boards json
    data = parse_json(json1)
    data.update(parse_json(json2))
    return [ujson.dumps(data), data]
