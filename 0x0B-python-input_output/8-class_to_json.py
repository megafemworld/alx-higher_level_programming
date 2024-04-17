""" #8-class_to_json.py defination """


def class_to_json(obj):
    """
    This function returns the dictionary description with
    simple data structure (list, dictionary, string, integer
    and boolean) for JSON serialization of an object
    """
    return (obj.__dict__)
