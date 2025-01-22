import sqlite3
import meal_utils
import ingredient_utils

CONNECTION = sqlite3.connect("foodie.db")

if __name__ == "__main__":
    test_meal = meal_utils.Meal(
        meal_utils.MealStats(
            id=-1,
            name="TF2 Bonk",
            energy=10_000_000,
            fat=1,
            protein=0,
            sugar=100_000,
            price=1
        ),
        ingredients={
            ingredient_utils.Ingredient(
                ingredient_utils.IngredientStats(
                    name="Radiation",
                    energy=9_999_999_999
                )
            ) : 350
        }
    )

    print(test_meal)
    test_meal.add_to(CONNECTION)
    print()
    print("Meal added")