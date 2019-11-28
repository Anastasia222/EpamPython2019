def atom(value=None):
    """ Returning the set of functions including:
    - getting a value of the variable
    - setting a new value of the variable
    - applying a set of functions to the variable and getting a new value
    - deleting the value of the variable.
    """

    def get_value():
        return value

    def set_value(new_value):
        nonlocal value
        value = new_value
        return value

    def process_value(*functions):
        nonlocal value
        for function in functions:
            value = function(value)
        return value

    def delete_value():
        nonlocal value
        value = None

    return get_value, set_value, process_value, delete_value