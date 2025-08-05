import unittest
from ai_calorie_tracker.core.calculations import (
    calculate_bmi,
    bmi_category,
    calculate_total_intake
)

class TestCalculations(unittest.TestCase):
    """
    Unit tests for the calculations module.
    """

    def test_calculate_bmi(self):
        """
        Test the calculate_bmi function with various inputs.
        """
        # Normal case
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.86, places=2)
        # Underweight case
        self.assertAlmostEqual(calculate_bmi(50, 1.75), 16.33, places=2)
        # Overweight case
        self.assertAlmostEqual(calculate_bmi(90, 1.75), 29.39, places=2)
        # Edge case: zero height
        self.assertEqual(calculate_bmi(70, 0), 0)
        # Edge case: negative height
        self.assertEqual(calculate_bmi(70, -1.75), 0)

    def test_bmi_category(self):
        """
        Test the bmi_category function with various BMI values.
        """
        # Underweight
        self.assertEqual(bmi_category(18.4), "Underweight")
        # Normal weight (boundary)
        self.assertEqual(bmi_category(18.5), "Normal weight")
        self.assertEqual(bmi_category(24.9), "Normal weight")
        # Overweight (boundary)
        self.assertEqual(bmi_category(25.0), "Overweight")
        self.assertEqual(bmi_category(29.9), "Overweight")
        # Obese (boundary)
        self.assertEqual(bmi_category(30.0), "Obese")
        self.assertEqual(bmi_category(35.5), "Obese")
        # Edge cases
        self.assertEqual(bmi_category(0), "Underweight")
        self.assertEqual(bmi_category(-10), "Underweight")

    def test_calculate_total_intake(self):
        """
        Test the calculate_total_intake function with a list of food data.
        """
        food_intake = [
            {
                "food_item": "1 large apple",
                "calories": 116,
                "protein": 0.6,
                "carbohydrates": 31,
                "fat": 0.4
            },
            {
                "food_item": "100g cooked chicken breast",
                "calories": 165,
                "protein": 31,
                "carbohydrates": 0,
                "fat": 3.6
            },
            {
                "food_item": "1 serving of brown rice",
                "calories": 216,
                "protein": 5.0,
                "carbohydrates": 45,
                "fat": 1.8
            }
        ]

        expected_calories = 116 + 165 + 216
        expected_protein = 0.6 + 31 + 5.0
        expected_carbs = 31 + 0 + 45
        expected_fat = 0.4 + 3.6 + 1.8

        total_calories, total_protein, total_carbs, total_fat = calculate_total_intake(food_intake)

        self.assertAlmostEqual(total_calories, expected_calories, places=2)
        self.assertAlmostEqual(total_protein, expected_protein, places=2)
        self.assertAlmostEqual(total_carbs, expected_carbs, places=2)
        self.assertAlmostEqual(total_fat, expected_fat, places=2)
        
    def test_calculate_total_intake_empty_list(self):
        """
        Test the function with an empty list.
        """
        total_calories, total_protein, total_carbs, total_fat = calculate_total_intake([])
        self.assertEqual(total_calories, 0)
        self.assertEqual(total_protein, 0)
        self.assertEqual(total_carbs, 0)
        self.assertEqual(total_fat, 0)

if __name__ == '__main__':
    unittest.main()
