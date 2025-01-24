import sqlite3
import meal_utils
import ingredient_utils
import generic_utils

CONNECTION = sqlite3.connect("foodie.db")

if __name__ == "__main__":
    test_ingredient = ingredient_utils.Ingredient(
        generic_utils.FoodStats(
            name="Radiation",
            energy=9_999_999_999
        )
    )
        
    test_meal = meal_utils.Meal(
        generic_utils.FoodStats(
            name="TF Bonk"
        ),
        ingredients={
            test_ingredient : 350
        }
    )

    test_ingredient.add_to(CONNECTION)
    print()
    print("Ingredient added")
    print(test_ingredient)

    test_meal.add_to(CONNECTION)
    print()
    print("Meal added")
    print(test_meal)