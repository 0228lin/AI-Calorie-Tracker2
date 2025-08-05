def calculate_bmi(weight_kg, height_m):
    """
    Calculates Body Mass Index (BMI).
    :param weight_kg: Weight in kilograms.
    :param height_m: Height in meters.
    :return: The calculated BMI value.
    """
    if height_m <= 0:
        return 0
    return weight_kg / (height_m ** 2)

def bmi_category(bmi):
    """
    Categorizes BMI into standard health classifications.
    :param bmi: The BMI value.
    :return: A string with the BMI category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def calculate_total_intake(food_intake_data):
    """
    Calculates total calories, protein, carbs, and fat from a list of food data.
    :param food_intake_data: A list of dictionaries, where each dict contains nutritional data for a food item.
    :return: A tuple of (total_calories, total_protein, total_carbs, total_fat).
    """
    total_calories = sum(item.get('calories', 0) for item in food_intake_data)
    total_protein = sum(item.get('protein', 0) for item in food_intake_data)
    total_carbs = sum(item.get('carbohydrates', 0) for item in food_intake_data)
    total_fat = sum(item.get('fat', 0) for item in food_intake_data)

    return total_calories, total_protein, total_carbs, total_fat
