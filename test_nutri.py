import unittest
from nutri_track import calculate_recipe_totals

class TestNutri(unittest.TestCase):
    def test_calculation(self):
        db = {"apple": {"calories": 52, "protein": 0.3, "fat": 0.2, "carbs": 14}}
        recipe = {"apple": 200}
        result = calculate_recipe_totals(recipe, db)
        self.assertEqual(result["calories"], 104)

if __name__ == '__main__':
    unittest.main()
