""" #8-class_to_json.py defination """


def class_to_json(obj):
    """ class_to_json
    This function returns the dictionary description with
    simple data structure (list, dictionary, string, integer
    and boolean) for JSON serialization of an object
    Arg:
        obj - This is an instance of a class to return its json
    """
    return (obj.__dict__)
