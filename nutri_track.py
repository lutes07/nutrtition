import json
import os
import csv

def load_data(filepath):
    #Load JSON data into a dictionary, return empty if no file
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r') as f:
        return json.load(f)

def save_data(filepath, data):
    #Save current dictionary data to JSON file
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def calculate_recipe_totals(recipe_ingredients, nutrition_db):
    totals = {"calories": 0, "protein": 0, "fat": 0, "carbs": 0}
    for item, grams in recipe_ingredients.items():
        # Lowercase item to match the database
        item_lookup = item.lower()
        if item_lookup in nutrition_db:
            #Calculate based on 100g base unit
            factor = grams / 100
            for macro in totals:
                totals[macro] += nutrition_db[item][macro] * factor
    return totals

def get_user_choice(min_range, max_range):
    #This will handle the menu selection and prevent crashes if input is not an integer
    while True:
        try:
            choice = int(input(f"Selection ({min_range}-{max_range}): "))
            if min_range <= choice <= max_range:
                return choice
        except ValueError:
            pass
def export_shopping_list(cookbook, filename="shopping_list.csv"):
    # Allows user to select a recipe and export ingredients to a CSV file
    if not cookbook:
        print("Cookbook is empty. Nothing to export.")
        return

    print("\n-- Export Shopping List --")
    recipe_list = list(cookbook.keys())
    for i, name in enumerate(recipe_list, 1):
        print(f"{i}. {name}")
    
    choice = get_user_choice(1, len(recipe_list))
    recipe_name = recipe_list[choice-1]
    ingredients = cookbook[recipe_name]

    try:
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Ingredient", "Amount (Grams)"])
            for ing, amt in ingredients.items():
                writer.writerow([ing.capitalize(), amt])
        print(f"Successfully exported {recipe_name} to {filename}!")
    except Exception as e:
        print(f"Error exporting CSV: {e}")
        
def manage_cookbook(cookbook, nutrition_db):
    #Nested menu for viewing, adding, and getting rid of recipes
    while True:
        print("\n-- Manage Cookbook --\n1. View\n2. Add\n3. Delete\n4. Back")
        choice = get_user_choice(1, 4)
        if choice == 1:
            for name, ingredients in cookbook.items():
                print(f"{name}: {ingredients}")
        elif choice == 2:
            name = input("Recipe Name: ")
            items = {}
            while True:
                # Force the ingredient name to be lowercase so no errors
                ing = input("Ingredient (or 'done'): ").lower()
                if ing == 'done': break
                try:
                    amount = float(input(f"Grams of {ing}: "))
                    items[ing] = amount
                except ValueError:
                    print("Please enter a number for the grams.")
            cookbook[name] = items
        elif choice == 3:
            name = input("Delete which recipe? ")
            cookbook.pop(name, None)
        else: break

def main():
    nutrition_db = load_data('nutrition_db.json')
    cookbook = load_data('cookbook.json')
    
    while True:
        print("\n-- NutriTrack Main Menu --")
        print("1. Manage Cookbook")
        print("2. Nutritional Analysis")
        print("3. Export Shopping List (CSV)") # New option
        print("4. Exit")
        
        choice = get_user_choice(1, 4)
        
        if choice == 1:
            manage_cookbook(cookbook, nutrition_db)
        elif choice == 2:
            name = input("Enter recipe name for analysis: ")
            if name in cookbook:
                results = calculate_recipe_totals(cookbook[name], nutrition_db)
                # Improved UI output for Week 3
                print(f"\n--- Analysis for {name} ---")
                print(f"Calories: {results['calories']:.2f}")
                print(f"Protein:  {results['protein']:.2f}g")
                print(f"Carbs:    {results['carbs']:.2f}g")
                print(f"Fat:      {results['fat']:.2f}g")
            else:
                print("Recipe not found.")
        elif choice == 3:
            export_shopping_list(cookbook)
        elif choice == 4:
            save_data('cookbook.json', cookbook)
            print("Progress saved. Goodbye!")
            break

if __name__ == "__main__":
    main()
