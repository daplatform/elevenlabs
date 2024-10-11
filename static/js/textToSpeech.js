async function textToSpeech(text, action = 'stream', voiceId = '') {
    // Set a default voiceId if none is provided
    if (!voiceId) {
        voiceId = '9BWtsMINqrJLrRacOk9x'; // Default voiceId
    } 
    text = text.replace(/['"]/g, '').replace(/[^a-zA-Z0-9\s.,]/g, ''); 
   
    if (action === 'stream') {
        const apiUrl = '/stream'; // API endpoint for streaming audio
        const requestBody = {
            text: text,
            voiceId: voiceId // Include voiceId in the request
        };

        try {
            const response = await fetch(apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(requestBody),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(`Error: ${errorData.error || 'Failed to generate audio'} (status: ${response.status})`);
            }

            const audio = new Audio(URL.createObjectURL(await response.blob()));
            await audio.play();
        } catch (error) {
            console.error('Error:', error);
        }
    } else if (action === 'generate') {
        const apiUrl = '/generate_sound'; // Updated API endpoint for sound generation
        const requestBody = {
            text: text
        };

        try {
            const response = await fetch(apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(requestBody)
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(`Error: ${errorData.error || 'Failed to generate sound'} (status: ${response.status})`);
            }

            const data = await response.json();
            const audioBase64 = data.audio; // Get the Base64 audio data
            const audio = new Audio(`data:audio/mpeg;base64,${audioBase64}`); // Create audio object from Base64 data
            await audio.play();
        } catch (error) {
            console.error('Error:', error);
        }
    }  else {
        console.error('Invalid action specified. Use "stream" or "generate".');
    }
}
