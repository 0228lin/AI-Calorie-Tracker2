import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from ai_calorie_tracker.core.calculations import (
    calculate_bmi,
    bmi_category,
    calculate_total_intake
)
from ai_calorie_tracker.ai_analysis.nutritional_data_fetcher import get_nutritional_data
from ai_calorie_tracker.ai_analysis.gemini_interface import get_ai_analysis

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """Renders the main input form page."""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """Processes user input and displays the analysis."""
    try:
        height_cm = float(request.form['height'])
        weight_kg = float(request.form['weight'])
        food_list_raw = request.form['food_items'].strip().split('\n')
        
        height_m = height_cm / 100
        food_items_raw = {item.strip(): True for item in food_list_raw if item.strip()}

        # Dynamically fetch nutritional data
        food_intake_data = []
        for item in food_items_raw.keys():
            nut_data = get_nutritional_data(item)
            if nut_data:
                food_intake_data.append(nut_data)

        # Aggregate nutritional data
        calories, protein, carbs, fat = calculate_total_intake(food_intake_data)
        
        # Calculate BMI
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
        
        # Get AI analysis
        ai_analysis = get_ai_analysis(user_data)

        return render_template('results.html',
                               user_data=user_data,
                               ai_analysis=ai_analysis,
                               food_items=food_intake_data)
    
    except (ValueError, KeyError) as e:
        return f"Invalid input. Please check your height and weight. Error: {e}", 400

if __name__ == '__main__':
    app.run(debug=True)
