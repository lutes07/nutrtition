# Project Proposal: NutriTrack Recipe Optimizer
**Student:** Lucas Lutes  
**Major:** Computer Engineering

## Project Summary
The **NutriTrack Recipe Optimizer** is a console-based application designed to help users manage a digital cookbook while analyzing the nutritional impact of their meals. The program stores recipes as data structures to calculate total caloric and macronutrient values. It utilizes local JSON data to map ingredients to their corresponding nutritional values, allowing for meal planning and health tracking without a constant internet connection. As I am personally trying to eat better and manage my meals, this program serves as a functional tool to assist in that goal.

## Core Features (Main Menu)
* **[1] Manage Cookbook:** Enter a submenu to view, add, or delete recipes from the collection (Level 3 depth).
* **[2] Nutritional Analysis:** Select a recipe to calculate total Calories, Protein, Carbs, and Fats based on ingredient quantities.
* **[3] Visualize Macros:** Generate a Matplotlib Radar Chart (Spider Plot) comparing a recipe's profile to daily Recommended Daily Intake (RDI).
* **[4] Smart Substitution:** A feature that suggests lower-calorie or healthier alternatives for specific ingredients within a selected recipe.
* **[5] Export Shopping List:** Generate a summarized CSV file of all ingredients needed for a selected list of recipes.
* **[0] Exit:** Save all changes to the JSON database and terminate the program.

## Anticipated Helper Functions
* `load_data(filepath)`: Handles reading the nested JSON structures into Python dictionaries at startup.
* `calculate_recipe_totals(ingredients, nutrition_db)`: Iterates through a recipe dictionary, cross-references the nutrition database, and returns a dictionary of total macros.
* `create_radar_chart(label_data, values)`: Uses the Matplotlib library to generate a plot showing nutrient distribution.
* `get_user_choice(min_range, max_range)`: A robust validation function to handle menu navigation and prevent crashes from invalid inputs.

## Selected Rubric Objectives (5)
1. **JSON/CSV File Processing:** The application uses JSON for the primary database and CSV for exporting shopping lists.
2. **Complex Datatypes:** Recipes and nutritional data are managed using deeply nested dictionaries and lists of dictionaries.
3. **Matplotlib Plot:** Implementation of a **Spider Plot** to visualize how a meal fits within nutritional targets.
4. **Unittest Framework:** A dedicated `test_nutri.py` file will be used to run unit tests on all math-heavy calculation functions.
5. **Nested Menutree:** The "Manage Cookbook" option will lead to submenus for viewing or editing, reaching a depth of 3 levels.

## Innovative Component
**Smart Substitution Engine:** This component will analyze the "pain points" of a recipe (such as high saturated fat or high calories). It will scan the broader nutrition database to suggest replacement ingredients with a similar profile but better health metrics. It then automatically updates a temporary "optimized" version of the recipe for the user to review.

---

## Weekly Progress Report
### Week 1 (Current)
* **Status:** Project Proposal and README drafted.
* **Task:** Designed the initial JSON schema for recipe storage.
* **Hours Logged:** 2 hours.

```python
def calculate_recipe_totals(recipe_ingredients, nutrition_db):
    totals = {"calories": 0, "protein": 0, "fat": 0, "carbs": 0}
    for item, grams in recipe_ingredients.items():
        if item in nutrition_db:
            factor = grams / 100
            for macro in totals:
                totals[macro] += nutrition_db[item][macro] * factor
    return totals
