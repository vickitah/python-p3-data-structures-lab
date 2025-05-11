spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # Returns a list of names of the spicy foods
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    # Returns a list of foods with heat_level > 5
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    # Prints each spicy food in the specified format with 🌶 emojis
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # Returns the first food that matches the given cuisine
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    # Prints only the spiciest foods (heat_level > 5) in the specified format
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    # Returns the average heat level of all spicy foods
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    # Adds a new spicy food to the list and returns the updated list
    return spicy_foods + [spicy_food]
