# aac.py
from flask import jsonify, request
import subprocess
import json

API_KEY = 'AIzaSyC0VHyo19QVjBG7GhnMKZUWR_KRUVnIGKU'
GEMINI_API_URL = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}'

def ask_question(data):
    question = data.get('question')
    if not question:
        return jsonify({'error': 'No question provided'}), 400

    # Create the prompt for Gemini
    prompt_data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"You are a non-verbal child who provides short answers (3-4 words) to questions. Here is a question: '{question}'. "
                                "Please remove any special characters except for commas and full stops. Provide all possible response options—positive, negative, and neutral—without indicating their sentiment. Do not include any bold text or formatting, and keep the responses to a maximum of 4 options."
                    }
                ]
            }
        ]
    }

    # Use subprocess to execute the curl command and get the response from Gemini
    curl_command = [
        'curl',
        '-H', 'Content-Type: application/json',
        '-d', json.dumps(prompt_data),
        '-X', 'POST', GEMINI_API_URL
    ]

    try:
        # Execute the curl command
        result = subprocess.run(curl_command, capture_output=True, text=True)

        # Check if the response was successful
        if result.returncode != 0:
            return jsonify({'error': 'Error calling Gemini API'}), 500

        response_json = json.loads(result.stdout)

        # Extract the content from the response
        content = response_json['candidates'][0]['content']['parts'][0]['text']
        responses = content.split('\n')  # Split responses into a list

        return jsonify({
            'responses': responses[:4]  # Limit to 4 responses
        })

    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid response from Gemini API'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500
