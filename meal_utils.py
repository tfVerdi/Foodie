from sqlite3 import Connection
import generic_utils
from ingredient_utils import Ingredient

class MealStats:
    def __init__(self, id: int = -1, name: str = "", energy: float = -1, protein: float = -1, fat: float = -1, cholesterol: float = -1, carbohidrate: float = -1, sugar: float = -1, sodium: float = -1, price: int = -1):
        self.id = generic_utils.check_null(id)
        self.name = name
        self.energy = generic_utils.check_null(energy)
        self.protein = generic_utils.check_null(protein)
        self.fat = generic_utils.check_null(fat)
        self.cholesterol = generic_utils.check_null(cholesterol)
        self.carbohidrate = generic_utils.check_null(carbohidrate)
        self.sugar = generic_utils.check_null(sugar)
        self.sodium = generic_utils.check_null(sodium)
        self.price = generic_utils.check_null(price)

    def load_as_dict(self) -> dict:
        info = {
            "meal_id" : self.id,
            "meal_name" : self.name,
            "meal_energy" : self.energy,
            "meal_protein" : self.protein,
            "meal_fat" : self.fat,
            "meal_cholesterol" : self.cholesterol,
            "meal_carbohidrate" : self.carbohidrate,
            "meal_sugar" : self.sugar,
            "meal_sodium" : self.sodium,
            "meal_price" : self.price,
        }

        return info

class Meal:
    """Basic meal class, mix of Ingredients
    
    Contains the nutrients, and price per 100 gr/ml"""
    def __init__(self, meal_stats: MealStats, ingredients: dict[Ingredient: int]):
        self.ingredients = ingredients
        self.info = meal_stats
        self.info_dict = meal_stats.load_as_dict()

        if meal_stats.name.strip() == "":
            raise generic_utils.ErrorNoName(self)
        if not meal_stats.name.replace(" ", "").isalpha():
            raise generic_utils.ErrorInappropiateName(self)
        
        
    def __repr__(self) -> str:
        ingredients_string = ""
        for ingredient, amount in self.ingredients.items():
            ingredients_string += f"\n| {ingredient.name:<20} {amount:^6} gr/ml " + " "*(98) + "|\n"
        representation = f"""
+------+----------------------+------------+------------+------------+------------+------------+------------+------------+------------+
|  ID  |         NAME         |   ENERGY   |   PROTEIN  |     FAT    |    CHOL    |    CARBS   |   SUGAR    |   SODIUM   |   PRICE    |
|      |                      |    kcal    |      gr    |      gr    |     gr     |      gr    |     gr     |     gr     |    CLP     |
+------+----------------------+------------+------------+------------+------------+------------+------------+------------+------------+
| {self.info.id:^4} | {self.info.name:^20} | {self.info.energy:^10} | {self.info.protein:^10} | {self.info.fat:^10} | {self.info.cholesterol:^10} | {self.info.price:^10} | {self.info.sugar:^10} | {self.info.sodium:^10} | {self.info.cholesterol:^10} |
+------+----------------------+------------+------------+------------+------------+------------+------------+------------+------------+
| Ingredients                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------+"""
        representation += ingredients_string
        representation += "+-------------------------------------------------------------------------------------------------------------------------------------+"
        
        return representation
    
    def add_to(self, CONNECTION: Connection):
        with CONNECTION:
            c = CONNECTION.cursor()
            c.execute(
                """INSERT INTO meals (meal_id, meal_name, meal_energy, meal_fat, meal_protein, meal_sugar, meal_price)
VALUES
(:meal_id, :meal_name, :meal_energy, :meal_fat, :meal_protein, :meal_sugar, :meal_price)
""",
                self.info_dict
            )