import os
from dotenv import load_dotenv
from ai_calorie_tracker.core.calculations import calculate_bmi, bmi_category, calculate_total_intake
from ai_calorie_tracker.ai_analysis.nutritional_data_fetcher import get_nutritional_data
from ai_calorie_tracker.ai_analysis.gemini_interface import get_ai_analysis

# Load environment variables from .env file
load_dotenv()

def get_user_input():
    """Gathers user's height, weight, and food intake."""
    try:
        height_cm = float(input("Enter your height in centimeters: "))
        weight_kg = float(input("Enter your weight in kilograms: "))
        
        food_list_raw = {}
        print("Enter the food items you consumed today. Type 'done' to finish.")
        while True:
            food_item_input = input("Food item (e.g., '1 large apple' or '100g cooked chicken breast'): ").strip().lower()
            if food_item_input == 'done':
                break
            food_list_raw[food_item_input] = True
        
        return height_cm / 100, weight_kg, food_list_raw
    except ValueError:
        print("Invalid input. Please enter numbers for height and weight.")
        return None, None, None

def main():
    """Main function to run the diet program."""
    height_m, weight_kg, food_items_raw = get_user_input()
    
    if height_m is None or weight_kg is None:
        return

    # Dynamically fetch nutritional data for each food item
    food_intake_data = []
    print("\nFetching nutritional data for your food items...")
    for item in food_items_raw.keys():
        nut_data = get_nutritional_data(item)
        if nut_data:
            food_intake_data.append(nut_data)
            print(f"- Fetched data for: {nut_data.get('food_item', item)}")
        else:
            print(f"- Could not get data for: {item}. Skipping.")

    if not food_intake_data:
        print("\nNo food data was found. Cannot perform analysis.")
        return

    # Aggregate nutritional data
    calories, protein, carbs, fat = calculate_total_intake(food_intake_data)
    
    # Calculate BMI and prepare data for AI analysis
    bmi = calculate_bmi(weight_kg, height_m)
    bmi_cat = bmi_category(bmi)
    
    user_data = {
        'height_m': height_m,
        'weight_kg': weight_kg,
        'bmi': bmi,
        'bmi_category': bmi_cat,
        'total_calories': calories,
        'total_protein': protein,
        'total_carbs': carbs,
        'total_fat': fat,
        'food_items': food_items_raw
    }

    # Print a summary to the user
    print("\n--- Your Daily Summary ---")
    print(f"Height: {height_m * 100} cm")
    print(f"Weight: {weight_kg} kg")
    print(f"BMI: {bmi:.2f} ({bmi_cat})")
    print(f"Total Calories: {calories:.2f} kcal")
    print(f"Total Protein: {protein:.2f} g")
    print(f"Total Carbohydrates: {carbs:.2f} g")
    print(f"Total Fat: {fat:.2f} g")
    print("--------------------------\n")
    
    # Get and print AI-powered analysis
    print("Fetching AI-powered analysis...")
    ai_analysis = get_ai_analysis(user_data)
    print("\n--- AI Diet Analysis and Recommendations ---")
    print(ai_analysis)
    print("------------------------------------------")

if __name__ == "__main__":
    main()
