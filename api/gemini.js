// This import is crucial for your serverless function to work.
import { GoogleGenerativeAI } from "@google/generative-ai";

export default async function handler(request, response) {
    console.log('Received request for Gemini API.');

    if (request.method !== 'POST') {
        return response.status(405).json({ message: 'Method Not Allowed' });
    }

    try {
        const { prompt, generationConfig } = request.body;

        const apiKey = process.env.GEMINI_API_KEY;
        if (!apiKey) {
            console.error('API Key is missing from environment variables.');
            return response.status(500).json({ error: 'API Key not configured.' });
        }
        
        const genAI = new GoogleGenerativeAI(apiKey);
        const model = genAI.getGenerativeModel({ model: "gemini-2.5-flash-preview-05-20" });

        const payload = {
            contents: [{ parts: [{ text: prompt }] }],
            generationConfig: generationConfig,
        };
        
        console.log('Sending payload to Gemini:', JSON.stringify(payload, null, 2));

        const result = await model.generateContent(payload);
        const geminiResponse = await result.response;
        const text = geminiResponse.text();

        console.log('Received successful response from Gemini.');
        
        response.status(200).json({
            candidates: [{
                content: {
                    parts: [{ text: text }]
                }
            }]
        });

    } catch (error) {
        console.error('API call failed in serverless function:', error);
        response.status(500).json({ error: 'An error occurred while communicating with the Gemini API.' });
    }
}
