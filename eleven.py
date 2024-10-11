from flask import Flask, render_template, request, jsonify, Response
import re
import json
import requests
import base64
from config import Config
from serper import get_thumbnails_for_objects, get_thumbnails_for_characters

app = Flask(__name__)

# Function to generate sound from text
def generate_sound(text, duration_seconds=3, prompt_influence=0.3):
    url = "https://api.elevenlabs.io/v1/sound-generation"
    
    headers = {
        "xi-api-key": Config.XI_API_KEY,
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, headers=headers, json={
        "text": text,
        "duration_seconds": duration_seconds,
        "prompt_influence": prompt_influence
    })
    
    if response.ok:
        return response.content, None
    return None, "Failed to generate sound."

# Render the index.html page
@app.route('/')
def home():
    character_thumbnails = {}
    object_thumbnails = {}

    return render_template('eleven.html', 
                           deepgram_api_key=Config.DEEPGRAM_API_KEY, 
                           gemini_api_key=Config.GEMINI_API_KEY,
                           xi_api_key=Config.XI_API_KEY,
                           character_thumbnails=character_thumbnails,
                           object_thumbnails=object_thumbnails)

def clean_gemini_response():
    try:
        raw_response = request.json.get('response', '')
        json_part = re.search(r"\{.*\}", raw_response, re.DOTALL)
        
        if json_part:
            clean_json_str = json_part.group(0)
            clean_json = json.loads(clean_json_str)
            
            unique_objects = set()
            unique_characters = set()
            object_types = {}
            
            for obj in clean_json.get('objects', []):
                obj_type = obj.get('type', 'unknown')
                obj_name = obj['name']
                
                if obj_type not in object_types:
                    object_types[obj_type] = []
                object_types[obj_type].append(obj_name)
                unique_objects.add(obj_name)

            for char in clean_json.get('characters', []):
                unique_characters.add(char['name'])
            
            object_thumbnails = get_thumbnails_for_objects(unique_objects)
            character_thumbnails = get_thumbnails_for_characters(unique_characters)

            # Clean the topic
            topic = clean_json.get('topic', '')
            topic = re.sub(r"[^a-zA-Z0-9\s.,]", '', topic)  # Allow letters, numbers, spaces, commas, and periods
            
            output = {
                "characters": ', '.join([char['name'] for char in clean_json.get('characters', [])]),
                "objects_by_type": object_types,
                "story": clean_json.get('story', ''),
                "topic": topic,  # Cleaned topic
                "object_thumbnails": {name: object_thumbnails.get(name, None) for name in unique_objects},
                "character_thumbnails": {name: character_thumbnails.get(name, None) for name in unique_characters}
            }
            return jsonify(output)
        
        else:
            return jsonify({"error": "No valid JSON found in response"}), 400
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/stream', methods=['POST'])
def stream_audio():
    text_to_speak = request.json.get('text', '')
    print(text_to_speak)
    if not text_to_speak:
        return jsonify({'error': 'No text provided'}), 400

    # Prepare the API request using the voice ID from the config
    tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{Config.VOICE_ID}/stream"
    headers = {
        "Accept": "application/json",
        "xi-api-key": Config.XI_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text_to_speak,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.1,
            "similarity_boost": 0.3,
            "style": 0.0,
            "use_speaker_boost": True
        }
    }

    # Stream audio
    response = requests.post(tts_url, headers=headers, json=data, stream=True)

    # Check for errors
    if response.status_code != 200:
        return jsonify({'error': 'Error fetching audio', 'details': response.json()}), response.status_code

    # Return the audio stream as a response
    return Response(response.iter_content(chunk_size=1024), content_type='audio/mpeg')

# Function to generate sound from text
def generate_sound(text, duration_seconds=3, prompt_influence=0.3):
    url = "https://api.elevenlabs.io/v1/sound-generation"
    
    headers = {
        "xi-api-key": Config.XI_API_KEY,
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, headers=headers, json={
        "text": text,
        "duration_seconds": duration_seconds,
        "prompt_influence": prompt_influence
    })
    
    if response.ok:
        return response.content, None
    return None, "Failed to generate sound."


if __name__ == '__main__':
    app.run(debug=True)
