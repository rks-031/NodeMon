const express = require('express');
const { exec } = require('child_process');
require('dotenv').config();

const app = express();
app.use(express.json());

const PORT = process.env.PORT || 3000;

// Endpoint to handle URL submission from social media posts
app.post('/extract-content', async (req, res) => {
    const { url } = req.body;

    // Extract content from the URL (this is a placeholder function)
    const content = await extractContentFromURL(url);

    // Call the Python script to generate product listing using extracted content
    exec(`python model/generate_listing.py "${content}"`, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error: ${error.message}`);
            return res.status(500).send('Error generating product listing');
        }
        if (stderr) {
            console.error(`Stderr: ${stderr}`);
            return res.status(500).send('Error generating product listing');
        }
        res.json(JSON.parse(stdout));
    });
});

// Function to extract content from social media URL (placeholder)
async function extractContentFromURL(url) {
    // Implement actual extraction logic here (text, images, videos)
    // For now, we return mock content for testing purposes.
    return "Check out my new Smart Fitness Tracker! It tracks heart rate and sleep patterns. Features: Heart rate monitoring, Sleep tracking.";
}

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});