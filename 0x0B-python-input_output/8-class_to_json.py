""" #8-class_to_json.py defination """


def class_to_json(obj):
    """
    Serialize an object into a dictionary suitable for JSON serialization.

    Args:
        obj: An instance of a Class with attributes that are serializable,
             including lists, dictionaries, strings, integers, and booleans.

    Returns:
        dict: A dictionary representation of the object with simple data structures
              that can be serialized to JSON.
    """

    return (obj.__dict__)
