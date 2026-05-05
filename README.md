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
* **[5] Exit:** Save all changes to the JSON database and terminate the program.

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

---

## Weekly Progress Report

### Week 1
* **Status:** Project Proposal and README drafted.
* **Task:** Designed the initial JSON schema for recipe storage.
* **Hours Logged:** 2 hours.

### Week 2
* **Status:** Successfully transitioned the project into a mostly functional prototype.
* **Tasks:**
    * Built the core Python application with a 3-level nested menu for cookbook management.
    * Integrated JSON file processing to save and load recipes.
    * Developed the math engine to calculate nutritional totals for meals.
* **Challenges:** Progress was slightly impacted by a heavy workload involving tests, exams, and other homework.
* **Hours Logged:** 7 hours.

### Week 3 (Current)
* **Status:** Expanded the prototype with file export capabilities and refined logic.
* **Tasks:**
    * **CSV Export:** Implemented the `export_shopping_list` function to generate CSV files, satisfying the first rubric objective.
    * **UI/UX Enhancement:** Refined the "Analysis" output to display formatted macro data rather than raw dictionaries.
    * **Unit Testing:** Finalized the initial `test_nutri.py` file to verify the accuracy of macro calculations.
    * **Data Integrity:** Updated ingredient lookups to be case-insensitive to prevent user errors.
* **Hours Logged:** 2 hours.

### Week 4 (Current)
* **Status:** Project completion and final presentation preparation.
* **Tasks:**
    * **Architecture Split:** Separated the project into a standard `main.py` execution file and a `nutri_track.py` helper module.
    * **Data Visualization:** Built and integrated the Matplotlib Spider Plot to visualize recipe macros against standard daily targets.
    * **Testing Additions:** Added additional unit tests to verify proper handling of missing database files.
    * **Code Quality:** Formatted all inline comments into standard Python docstrings for professional documentation.
* **Hours Logged:** 4 hours.

**Total Project Hours Logged:** 15 hours.

