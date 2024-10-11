from flask import Flask, request, jsonify, render_template, send_file, Response, url_for, send_from_directory

import time
import eleven  # Import the eleven.py module
import re
import json
import os  # Import os for file operations
import requests
import base64
from config import Config  # Import Config class from config.py
from abstract import process_conc , process_metadata_for_concept
from eleven import generate_sound  # Import the function from eleven.py
from serper import get_thumbnails_for_objects, get_thumbnails_for_characters
from aac import ask_question  # Import the ask_question function from aac.py
from avatar import generate_dialogue  # Import the generate_dialogue function

app = Flask(__name__)
app.config.from_object(Config)  # Load configuration from Config class

# Route for the home page (index.html)
@app.route('/')
def home():
    return render_template('index.html')

# Route for frame.html
@app.route('/frame')
def frame():
    return render_template('frame.html')

# Route for main.html
@app.route('/main')
def main():
    return render_template('main.html')

# Route for the 'About' page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the 'Features' page
@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/generate-dialogue', methods=['POST'])  # Updated endpoint
def generate_dialogue_response():  # Updated function name
    topic = request.json.get('topic')

    if not topic:
        return jsonify({'error': 'No topic provided'}), 400

    try:
        dialogues = generate_dialogue(topic)
        return jsonify({"dialogues": dialogues})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/water')
def water():
    return render_template('water.html')

@app.route('/rock')
def rock():
    return render_template('rock.html')

# Route for adaptive.html with API keys
@app.route('/adaptive')
def adaptive():
    return render_template('adaptive.html', 
                           deepgram_api_key=Config.DEEPGRAM_API_KEY, 
                           gemini_api_key=Config.GEMINI_API_KEY, 
                           xi_api_key=Config.XI_API_KEY)

@app.route('/process_concept', methods=['POST'])
def process_concept_request():
    data = request.json
    concept = data.get('concept')
    # Process the concept using the function in abstract.py
    result = process_conc(concept)
    
    # Return the result as a JSON response
    return jsonify({'result': result})

@app.route('/get_image/<path:filename>')
def get_image(filename):
    return send_from_directory('static/images', filename)


@app.route('/process_metadata_concept', methods=['POST'])
def process_metadata_concept_request():
    data = request.json
    concept = data.get('concept')
    
    # Call the new Gemini logic for metadata prompt
    content, image_data = process_metadata_for_concept(concept)
    
    if content is not None:
        # Generate a unique image URL to prevent caching
        unique_timestamp = int(time.time())
        return jsonify({
            'content': content,
            'image_url': f"{url_for('get_image', filename='output_image.png')}?t={unique_timestamp}"
        })
    else:
       
        return jsonify({'error': image_data}), 500  # Return the error message as the image field


# Additional routes for other use cases
@app.route('/abstract')
def abstract():
    return render_template('abstract.html')

@app.route('/social')
def social():
    return render_template('social.html')

@app.route('/intelligent_aac')
def intelligent_aac():
    return render_template('intelligent_aac.html')  # Ensure you have this template

@app.route('/ask', methods=['POST'])
def ask_question_route():
    data = request.json
    response = ask_question(data)
    return response  # Return the response from ask_question



@app.route('/mother')
def mother():
    return render_template('mother.html')


@app.route('/speech')
def speech():
    return render_template('speech.html')

@app.route('/clean_gemini_response', methods=['POST'])
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

# Route for streaming audio using the Eleven Labs API
@app.route('/stream', methods=['POST'])
def stream_audio():
    text_to_speak = request.json.get('text', '')
    voice_id = request.json.get('voiceId', Config.VOICE_ID)  # Get voiceId from request
    if not text_to_speak:
        return jsonify({'error': 'No text provided'}), 400

    # Prepare the API request using the voice ID from the request or default
    tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"  # Use the received voiceId
    headers = {
        "Accept": "application/json",
        "xi-api-key": Config.XI_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text_to_speak,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.8,
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

@app.route('/generate_sound', methods=['POST'])
def handle_generate_sound():
    text_to_speak = request.json.get('text')
    if not text_to_speak:
        return jsonify({'error': 'No text provided'}), 400

    # Call the function that generates sound
    audio_data, error_message = generate_sound(text_to_speak)

    if audio_data is None:
        return jsonify({'error': error_message}), 500
   
    # If audio_data is returned, encode it to base64 for web usage
    audio_base64 = base64.b64encode(audio_data).decode('utf-8')
    return jsonify({"audio": audio_base64})


# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
