from sqlite3 import Connection
import generic_utils
from ingredient_utils import Ingredient

class Meal:
    """Basic meal class, mix of Ingredients
    
    Contains the nutrients, and price per 100 gr/ml"""
    def __init__(self, stats: generic_utils.FoodStats, ingredients: dict[Ingredient: int]):
        self.ingredients = ingredients
        self.stats = stats
        self.info_dict = {}
        
    def load_as_dict(self) -> dict:
        info = {
            "meal_name" : self.stats.name,
            "meal_energy" : self.stats.energy,
            "meal_protein" : self.stats.protein,
            "meal_fat" : self.stats.fat,
            "meal_cholesterol" : self.stats.cholesterol,
            "meal_carbohidrate" : self.stats.carbohidrate,
            "meal_sugar" : self.stats.sugar,
            "meal_sodium" : self.stats.sodium,
            "meal_price" : self.stats.price,
        }

        self.info_dict = info
        
    def __repr__(self) -> str:
        ingredients_string = ""
        for ingredient, amount in self.ingredients.items():
            ingredients_string += f"\n| {ingredient.stats.name:<20} {amount:^6} gr/ml " + " "*(91) + "|\n"
        representation = f"""
+----------------------+------------+------------+------------+------------+------------+------------+------------+------------+
|         NAME         |   ENERGY   |   PROTEIN  |     FAT    |    CHOL    |    CARBS   |   SUGAR    |   SODIUM   |   PRICE    |
|                      |    kcal    |      gr    |      gr    |     gr     |      gr    |     gr     |     gr     |    CLP     |
+----------------------+------------+------------+------------+------------+------------+------------+------------+------------+
| {self.stats.name:^20} | {self.stats.energy:^10} | {self.stats.protein:^10} | {self.stats.fat:^10} | {self.stats.cholesterol:^10} | {self.stats.price:^10} | {self.stats.sugar:^10} | {self.stats.sodium:^10} | {self.stats.cholesterol:^10} |
+----------------------+------------+------------+------------+------------+------------+------------+------------+------------+
| Ingredients                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------+"""
        representation += ingredients_string
        representation += "+------------------------------------------------------------------------------------------------------------------------------+"
        
        return representation
    
    def add_to(self, CONNECTION: Connection):
        self.load_as_dict()
        with CONNECTION:
            c = CONNECTION.cursor()
            c.execute(
                """INSERT INTO meals (meal_name, meal_energy, meal_fat, meal_protein, meal_sugar, meal_price)
VALUES
(:meal_name, :meal_energy, :meal_fat, :meal_protein, :meal_sugar, :meal_price)
""",
                self.info_dict
            )