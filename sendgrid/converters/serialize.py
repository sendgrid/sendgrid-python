from enum import Enum

from enum import Enum


def to_serializable(obj):
    if isinstance(obj, list):
        return [
            to_serializable(item) for item in obj if item is not None
        ]  # Remove None from lists
    elif isinstance(obj, dict):
        return {
            key: to_serializable(value)
            for key, value in obj.items()
            if value is not None
        }  # Remove None from dicts
    elif hasattr(obj, "to_dict"):
        return obj.to_dict()
    elif isinstance(obj, Enum):
        return obj.value
    else:
        return obj


def from_serializable(data, cls=None):
    """
    Converts a dictionary or list into a class instance or a list of instances.
    If `cls` is provided, it will instantiate the class using the dictionary values.
    """
    if isinstance(data, list):
        return [
            from_serializable(item, cls) for item in data
        ]  # Recursively handle lists
    elif isinstance(data, dict):
        if cls:
            # If a class is provided, instantiate it using the dictionary
            return cls(**{key: from_serializable(value) for key, value in data.items()})
        else:
            return {
                key: from_serializable(value) for key, value in data.items()
            }  # Recursively handle dicts
    else:
        return data  # Return primitive types as is
