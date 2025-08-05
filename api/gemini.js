// This file should be saved as `api/gemini.js` in your project's root directory.

import { GoogleGenerativeAI } from "@google/generative-ai";

export default async function handler(request, response) {
    // Read the API key from the Vercel environment variables
    const apiKey = process.env.GEMINI_API_KEY;

    if (!apiKey) {
        return response.status(500).json({ error: 'API key is not configured.' });
    }

    try {
        // Create a new instance of the GoogleGenerativeAI with your API key
        const genAI = new GoogleGenerativeAI(apiKey);
        
        // Extract the prompt and generationConfig from the request body
        const { prompt, generationConfig } = request.body;

        if (!prompt) {
            return response.status(400).json({ error: 'Prompt is required.' });
        }

        // Use the gemini-2.5-flash-preview-05-20 model
        const model = genAI.getGenerativeModel({ model: "gemini-2.5-flash-preview-05-20" });

        // This is the fix: The model expects a structured request payload.
        // We reconstruct the payload here with the prompt and optional generationConfig.
        const payload = {
            contents: [{
                role: "user",
                parts: [{ text: prompt }]
            }],
        };
        
        if (generationConfig) {
            payload.generationConfig = generationConfig;
        }

        const result = await model.generateContent(payload);
        
        // Return the full result object back to the frontend
        response.status(200).json(result);

    } catch (error) {
        console.error('Proxy error:', error);
        response.status(500).json({ error: 'An error occurred during the API call.' });
    }
}
