# AI-Calorie-Tracker

A powerful and intelligent calorie and nutrition tracker that leverages a large language model (LLM) to dynamically fetch food data and provide a personalized, AI-driven analysis of your diet.

## Features
- **BMI Calculation:** Calculates Body Mass Index (BMI) based on user's height and weight.
- **Dynamic Nutrition Tracking:** Uses an AI model (like Gemini or GPT) to instantly get nutritional data (calories, protein, carbs, fat) for any food item you input.
- **AI-Powered Analysis:** Acts as a personal diet assistant, providing detailed feedback on your diet and actionable recommendations for improvement.
- **Modular and Extensible:** The code is structured for easy modification and is a great foundation for further development.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/0228lin/AI-Calorie-Tracker.git
   cd AI-Calorie-Tracker

2.  Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4.  Set up your API key:
    Create a `.env` file in the root directory and add your API key:

    ```
    GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
    ```

## Usage

Run the main program from the root directory:

```bash
python -m ai_calorie_tracker.main
```

The program will guide you to enter your personal details and daily food intake, then provide a comprehensive AI-generated analysis.

## Project Structure

  - `ai_calorie_tracker/core/calculations.py`: Core logic for all calculations.
  - `ai_calorie_tracker/ai_analysis/nutritional_data_fetcher.py`: Manages the communication with the AI to get food data.
  - `ai_calorie_tracker/ai_analysis/gemini_interface.py`: Handles the AI model integration for the final analysis.
  - `ai_calorie_tracker/main.py`: The main program entry point.

## Contributing

We welcome contributions\! Please see our [CONTRIBUTING.md](https://www.google.com/search?q=CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

-----

*Disclaimer: This program is for informational purposes only and should not replace professional medical advice. Always consult a healthcare professional before making changes to your diet or exercise routine.*
