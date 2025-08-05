// This file should be saved as `api/gemini.js` in your project's root directory.

import { GoogleGenerativeAI } from "@google/generative-ai";

export default async function handler(request, response) {
    // Read the API key from the Vercel environment variables
    const apiKey = process.env.GEMINI_API_KEY;

    if (!apiKey) {
        return response.status(500).json({ error: 'API key is not configured.' });
    }

    try {
        const genAI = new GoogleGenerativeAI(apiKey);
        const { prompt, generationConfig } = request.body;

        if (!prompt) {
            return response.status(400).json({ error: 'Prompt is required.' });
        }

        // Use the gemini-2.5-flash-preview-05-20 model for text generation
        const model = genAI.getGenerativeModel({ model: "gemini-2.5-flash-preview-05-20", generationConfig });

        const result = await model.generateContent(prompt);
        
        // This is the fix: return the full result object, not just a partial response.
        response.status(200).json(result);

    } catch (error) {
        console.error('Proxy error:', error);
        response.status(500).json({ error: 'An error occurred during the API call.' });
    }
}
