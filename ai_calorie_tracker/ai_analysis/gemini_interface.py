import google.generativeai as genai
import os

def get_ai_analysis(user_data):
    """
    Sends user data to the Gemini API and returns a generated diet analysis.
    :param user_data: A dictionary containing user info and nutritional data.
    :return: A string with the AI's analysis and suggestions.
    """
    # Load API key from environment variable
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f"""
    Analyze the following user data and provide a detailed, actionable diet analysis.
    The analysis should include:
    1. A summary of the user's current status (BMI, weight category).
    2. Comments on the macronutrient distribution (calories, protein, carbs, fat) and whether it is balanced for their BMI.
    3. Specific, practical suggestions for improvement (e.g., "increase protein intake", "reduce fat consumption", "add more vegetables").
    4. A clear, friendly, and non-judgmental tone.

    User Data:
    - Height: {user_data['height_m']} meters
    - Weight: {user_data['weight_kg']} kg
    - BMI: {user_data['bmi']:.2f}
    - BMI Category: {user_data['bmi_category']}
    - Total Calories: {user_data['total_calories']:.2f} kcal
    - Total Protein: {user_data['total_protein']:.2f} g
    - Total Carbohydrates: {user_data['total_carbs']:.2f} g
    - Total Fat: {user_data['total_fat']:.2f} g
    - Food items consumed: {', '.join([item for item in user_data['food_items'].keys()])}
    
    Please provide the analysis in a single, well-structured paragraph or a short list.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred with the AI analysis: {e}"
