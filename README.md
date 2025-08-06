<h2 align="center">AI-Calorie-Tracker</h2>

<p align="center">
<img src="https://placehold.co/80x80/047857/ffffff?text=Diet" alt="AI Icon" width="80" />
</p>

<h4 align="center">An AI-powered tool to analyze your daily diet and provide personalized recommendations.</h4>

<p align="center">
<a href="https://github.com/0228lin/AI-Calorie-Tracker2/blob/main/LICENSE" target="_blank">
<img src="https://img.shields.io/github/license/0228lin/AI-Calorie-Tracker?style=flat-square" alt="licence" />
</a>
<a href="https://github.com/0228lin/AI-Calorie-Tracker2/fork" target="_blank">
<img src="https://img.shields.io/github/forks/0228lin/AI-Calorie-Tracker?style=flat-square" alt="forks"/>
</a>
<a href="https://github.com/0228lin/AI-Calorie-Tracker2/stargazers" target="_blank">
<img src="https://img.shields.io/github/stars/0228lin/AI-Calorie-Tracker?style=flat-square" alt="stars"/>
</a>
<a href="https://github.com/0228lin/AI-Calorie-Tracker2/issues" target="_blank">
<img src="https://img.shields.io/github/issues/0228lin/AI-Calorie-Tracker?style=flat-square" alt="issues"/>
</a>
<a href="https://github.com/0228lin/AI-Calorie-Tracker2/pulls" target="_blank">
<img src="https://img.shields.io/github/issues-pr/0228lin/AI-Calorie-Tracker?style=flat-square" alt="pull-requests"/>
</a>
<a href="https://twitter.com/intent/tweet?text=👋%20Check%20out%20this%20amazing%20AI%20Calorie%20Tracker%20project%20https://github.com/0228lin/AI-Calorie-Tracker"><img src="https://img.shields.io/twitter/url?label=Share%20on%20Twitter&style=social&url=https%3A%2F%2Fgithub.com%2F0228lin%2FAI-Calorie-Tracker"></a>
</p>

<p align="center">
<!-- Remember to update this with your actual Vercel deployment URL after deploying -->
<a href="https://ai-calorie-tracker2.vercel.app/" target="_blank">View Demo</a>
·
<a href="https://github.com/0228lin/AI-Calorie-Tracker2/issues/new/choose" target="_blank">Report Bug</a>
·
<a href="https://github.com/0228lin/AI-Calorie-Tracker2/issues/new/choose" target="_blank">Request Feature</a>
</p>
A powerful and intelligent calorie and nutrition tracker that leverages a large language model (LLM) to dynamically fetch food data and provide a personalized, AI-driven analysis of your diet.

-----

## 👋🏻 Introducing `AI-Calorie-Tracker`

`AI-Calorie-Tracker` is a tool that uses the power of AI to help you analyze your daily diet and manage your calorie intake. Simply input your food items and let the AI provide a detailed breakdown and personalized health recommendations.

This tool is perfect for anyone who wants to monitor their nutrition, understand their eating habits, and receive smart, data-driven advice.

## 🚀 Demo

Here is a quick demo of the app. I hope you enjoy it.

> [The Demo Link](https://ai-calorie-tracker2.vercel.app/) 
> <br>
<a href="https://ai-calorie-tracker2.vercel.app/">
  <img alt="View Demo" src="https://img.shields.io/badge/Try%20it%20now-View%20Demo-brightgreen"/>
</a>

Liked it? Please give a ⭐️ to **AI-Calorie-Tracker**.  
*Many Thanks to all the `Stargazers` who have supported this project with stars(⭐)*  

[![Stargazers repo roster for @0228lin/AI-Calorie-Tracker2](https://reporoster.com/stars/0228lin/AI-Calorie-Tracker2)](https://github.com/0228lin/AI-Calorie-Tracker2/stargazers#gh-light-mode-only)

[![Stargazers repo roster for @0228lin/AI-Calorie-Tracker2](https://reporoster.com/stars/dark/0228lin/AI-Calorie-Tracker2)](https://github.com/0228lin/AI-Calorie-Tracker2/stargazers#gh-dark-mode-only)
-----

## 🔥 Features

`AI-Calorie-Tracker` comes with a bundle of features already. You can do the followings with it:

  * 🍽️ **Analyze Food Items**: Get a detailed calorie and nutritional breakdown of your meals.  
  * 🧠 **AI-Powered Recommendations**: Receive personalized diet and health recommendations based on your input.  
  * 📊 **Track Progress**: Monitor your daily, weekly, and monthly calorie intake.  
  * 📱 **Responsive and Mobile-Friendly**: Use the tracker on any device, from your desktop to your smartphone.  

-----

## 📚 How to Use `AI-Calorie-Tracker`

1\.  `Go` to the [**live demo page**](https://ai-calorie-tracker2.vercel.app/).  
2.  `Enter` your height, weight and food items into the text input box.  
3.  `Click` on the **"Get Analysis"** button.  
4.  The AI will process your input and display the nutritional information and recommendations below the form.  
5.  You can continue to add more food items or clear the form to start a new entry.  

-----

## 🏗️ How to Set Up `AI-Calorie-Tracker` for Development?

This project is configured for deployment with **Vercel**. Here are the steps to set it up:

1.  **Clone the repository**

    ```bash
    git clone [https://github.com/0228lin/AI-Calorie-Tracker2.git](https://github.com/0228lin/AI-Calorie-Tracker2.git)
    ```

2.  **Navigate to the project directory**

    ```bash
    cd AI-Calorie-Tracker
    ```

3.  **Install Vercel Function dependencies**
    Navigate into the `api` directory and install its dependencies:

    ```bash
    cd api
    npm install
    cd .. # Go back to the root directory
    ```

4.  **Create a `.env` file for local development**
    In the **root** of your project, create a file named `.env` and add your Gemini API key:
    ```
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```
    **Remember: Do NOT commit this `.env` file to your public GitHub repository! It's already in `.gitignore`.**

5.  **Run locally (optional, requires Vercel CLI)**
    * Install Vercel CLI globally if you haven't already: `npm install -g vercel`
    * From the **root** of your project, run: `vercel dev`
    * This will start a local development server, and your API functions will be available.

## 🚀 How to Deploy to Vercel

1.  **Push your code to GitHub:** Ensure your project, with the structure and files (including `vercel.json` and the `api` folder) are pushed to a GitHub repository.

2.  **Sign up or Log in to Vercel:** Go to [Vercel.com](https://vercel.com/) and sign in. You can sign up directly with your GitHub account for easy integration.

3.  **Import Your Project:**
    * On your Vercel dashboard, click "Add New..." then "Project".
    * Choose "Import Git Repository" and select your `AI-Calorie-Tracker` repository from GitHub.

4.  **Configure Project Settings:**
    * Vercel will usually auto-detect your project settings.
    * Ensure the **Root Directory** is set to `/` (the root of your repository).
    * Under **"Framework Preset"** (in the "Build & Development Settings"), select **"Other"**.
    * For **"Output Directory,"** **set this to `.`** (a single dot). This tells Vercel that your `index.html` is directly in the root of the project.

5.  **Set Environment Variables:**
    * Before deploying, go to the "Environment Variables" section in your Vercel project settings.
    * Add a new environment variable:
        * **Name:** `GEMINI_API_KEY`
        * **Value:** Paste your actual Gemini API key here.
    * Make sure this variable is configured for the "Production" and "Preview" environments.

6.  **Deploy:** Click the "Deploy" button. Vercel will build and deploy your static site and serverless functions.

7.  **Access Your Demo:** Once the deployment is complete, Vercel will provide you with a unique URL (e.g., `https://your-project-name.vercel.app`). **This is the URL you should share with your users for the live demo.** It will be fully functional, with the API key securely handled by the Vercel serverless function.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

-----

*Disclaimer: This program is for informational purposes only and should not replace professional medical advice. Always consult a healthcare professional before making changes to your diet or exercise routine.*
