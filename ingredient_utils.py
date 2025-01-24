from sqlite3 import Connection
import generic_utils

class Ingredient:
    """Basic ingredient class
    
    Contains the nutrients, and price per 100 gr/ml"""
    def __init__(self, stats: generic_utils.FoodStats):
        self.stats = stats
        self.info_dict = {}
        
    def load_as_dict(self) -> dict:
        info = {
            "ingredient_name" : self.stats.name,
            "ingredient_energy" : self.stats.energy,
            "ingredient_protein" : self.stats.protein,
            "ingredient_fat" : self.stats.fat,
            "ingredient_cholesterol" : self.stats.cholesterol,
            "ingredient_carbohidrate" : self.stats.carbohidrate,
            "ingredient_sugar" : self.stats.sugar,
            "ingredient_sodium" : self.stats.sodium,
            "ingredient_price" : self.stats.price,
        }

        self.info_dict = info
    
    def __repr__(self):
        representation = f"""
+----------------------+------------+------------+------------+------------+------------+------------+------------+------------+
|         NAME         |   ENERGY   |   PROTEIN  |     FAT    |    CHOL    |    CARBS   |   SUGAR    |   SODIUM   |   PRICE    |
|                      |    kcal    |      gr    |      gr    |     gr     |      gr    |     gr     |     gr     |    CLP     |
+----------------------+------------+------------+------------+------------+------------+------------+------------+------------+
| {self.stats.name:^20} | {self.stats.energy:^10} | {self.stats.protein:^10} | {self.stats.fat:^10} | {self.stats.cholesterol:^10} | {self.stats.price:^10} | {self.stats.sugar:^10} | {self.stats.sodium:^10} | {self.stats.cholesterol:^10} |
+----------------------+------------+------------+------------+------------+------------+------------+------------+------------+"""
        
        return representation
    
    def add_to(self, connection: Connection):
        with connection:
            self.load_as_dict()
            c = connection.cursor()
            c.execute("""INSERT INTO ingredients (ingredient_name, ingredient_energy, ingredient_fat, ingredient_protein, ingredient_sugar, ingredient_price)
VALUES
(:ingredient_name, :ingredient_energy, :ingredient_fat, :ingredient_protein, :ingredient_sugar, :ingredient_price)
""",
                self.info_dict
            )