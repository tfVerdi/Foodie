class ErrorNoName(Exception):
    def __init__(self, object):
        self.message = f"""
    Tried to make an instance of {type(object)}, but it had no name!?!? Guacala!\n
    The offender:
    \t{object}
    """
        super().__init__(self.message)

class ErrorInappropiateName(Exception):
    def __init__(self, object):
        self.message = f"""
    Tried to make an instance of {type(object)}, but it had an illegal character!?!? Yuck!
    You can only use letters and spaces to name things :(\n
    The offender:
    \t{object.__repr__()}
    """
        super().__init__(self.message)

class ErrorLongName(Exception):
    def __init__(self, object):
        self.message = f"""
    Tried to make an instance of {type(object)}, but it a very long name!?!? Yikes!
    Try naming it in less than 20 characters ;)\n
    The offender:
    \t{object}
    """
        super().__init__(self.message)

def check_null(number: int | float) -> int | float | str:
    result = "NULL" if number < 0 else number
    return result