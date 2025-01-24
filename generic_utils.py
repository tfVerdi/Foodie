def check_valid_num(blame: any, number: int | float) -> int | float | str:
    if len(str(number)) > 10:
        raise ErrorLongNumber(blame, number)

def check_valid_name(blame: any, name: str):
    if name.strip() == "":
        raise ErrorNoName(blame, name)
    if not name.replace(" ", "").isalpha():
        raise ErrorInappropiateName(blame, name)
    if len(name) > 20:
        raise ErrorLongName
        
class FoodStats:
        def __init__(self, name: str = "", energy: float = -1, protein: float = -1, fat: float = -1, cholesterol: float = -1, carbohidrate: float = -1, sugar: float = -1, sodium: float = -1, price: int = -1):
            check_valid_name(self, name)
            self.name = name            
            check_valid_num(self, energy)
            self.energy = energy
            check_valid_num(self, protein)
            self.protein = protein
            check_valid_num(self, fat)
            self.fat = fat
            check_valid_num(self, cholesterol)
            self.cholesterol = cholesterol
            check_valid_num(self, carbohidrate)
            self.carbohidrate = carbohidrate
            check_valid_num(self, sugar)
            self.sugar = sugar
            check_valid_num(self, sodium)
            self.sodium = sodium
            check_valid_num(self, price)
            self.price = price

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

class ErrorLongNumber(Exception):
    def __init__(self, blame: any, number: int | float):
        self.message = f"""
    Tried to make an instance of {type(blame)},
    but one of the number variables had too many digits!?!? Ew!
    Try making it smaller, or if it already is, remove some decimals :P\n
    The offender object:
    \t{blame}
    The offender number:
    \t{number}
    """
        super().__init__(self.message)
