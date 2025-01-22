from sqlite3 import Connection
import generic_utils

class IngredientStats:
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
            "ingredient_id" : self.id,
            "ingredient_name" : self.name,
            "ingredient_energy" : self.energy,
            "ingredient_protein" : self.protein,
            "ingredient_fat" : self.fat,
            "ingredient_cholesterol" : self.cholesterol,
            "ingredient_carbohidrate" : self.carbohidrate,
            "ingredient_sugar" : self.sugar,
            "ingredient_sodium" : self.sodium,
            "ingredient_price" : self.price,
        }

        return info

class Ingredient:
    """Basic ingredient class
    
    Contains the nutrients, and price per 100 gr/ml"""
    def __init__(self, ingredient_stats: IngredientStats):
        self.info = ingredient_stats
        self.info_dict = ingredient_stats.load_as_dict()

        if ingredient_stats.name.strip() == "":
            raise generic_utils.ErrorNoName(self)
        if not ingredient_stats.name.replace(" ", "").isalpha():
            raise generic_utils.ErrorInappropiateName(self)
        
    
    def __repr__(self):
        representation = f"""
+------+----------------------+------------+------------+------------+------------+------------+------------+------------+------------+
|  ID  |         NAME         |   ENERGY   |   PROTEIN  |     FAT    |    CHOL    |    CARBS   |   SUGAR    |   SODIUM   |   PRICE    |
|      |                      |    kcal    |      gr    |      gr    |     gr     |      gr    |     gr     |     gr     |    CLP     |
+------+----------------------+------------+------------+------------+------------+------------+------------+------------+------------+
| {self.info.id:^4} | {self.info.name:^20} | {self.info.energy:^10} | {self.info.protein:^10} | {self.info.fat:^10} | {self.info.cholesterol:^10} | {self.info.price:^10} | {self.info.sugar:^10} | {self.info.sodium:^10} | {self.info.cholesterol:^10} |
+------+----------------------+------------+------------+------------+------------+------------+------------+------------+------------+"""
        
        return representation
    
    def add_to(self, connection: Connection):
        with connection:
            c = connection.cursor()
            c.execute("""INSERT INTO ingredients (ingredient_id, ingredient_name, ingredient_energy, ingredient_fat, ingredient_protein, ingredient_sugar, ingredient_price)
VALUES
(:ingredient_id, :ingredient_name, :ingredient_energy, :ingredient_fat, :ingredient_protein, :ingredient_sugar, :ingredient_price)
""",
                self.info
            )