import google.generativeai as genai
import os
import json

def get_nutritional_data(food_item):
    """
    Uses the Gemini API to get nutritional data for a given food item.
    :param food_item: The name of the food and serving size (e.g., "1 large apple").
    :return: A dictionary with nutritional data, or None if not found.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f"""
    Provide the nutritional data for "{food_item}".
    Respond with a JSON object containing the following keys: "food_item", "calories", "protein", "carbohydrates", and "fat". 
    The values should be numerical (calories in kcal, macros in grams).
    Example for "100g cooked chicken breast":
    {{
        "food_item": "100g cooked chicken breast",
        "calories": 165,
        "protein": 31,
        "carbohydrates": 0,
        "fat": 3.6
    }}
    If you cannot find the data, return a JSON with a single key "error" and a description.
    """
    
    try:
        response = model.generate_content(prompt)
        response_text = response.text.strip().replace("`", "").replace("json", "").strip()
        data = json.loads(response_text)
        return data if 'error' not in data else None
    except Exception as e:
        print(f"Error fetching data for {food_item}: {e}")
        return None
