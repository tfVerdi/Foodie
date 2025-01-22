CREATE TABLE meals (
    meal_id INTEGER PRIMARY KEY,
    meal_name VARCHAR(20) NOT NULL,
    meal_energy REAL,
    meal_protein REAL,
    meal_fat REAL,
    meal_cholesterol REAL,
    meal_carbohidrate REAL,
    meal_sugar REAL,
    meal_sodium REAL,
    meal_price INTEGER
);