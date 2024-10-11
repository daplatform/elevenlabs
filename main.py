from flask import Flask, request, jsonify, render_template, send_file
import eleven  # Import the eleven.py module
import os
from config import Config  # Import Config class from config.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('adaptive.html', deepgram_api_key=Config.DEEPGRAM_API_KEY, 
                        gemini_api_key=Config.GEMINI_API_KEY, 
                        xi_api_key=Config.XI_API_KEY)

@app.route('/clean_gemini_response', methods=['POST'])
def clean_gemini_response_route():
    raw_response = request.json.get('response', '')
    result = eleven.clean_gemini_response(raw_response)
    return jsonify(result)

@app.route('/stream', methods=['POST'])
def stream_audio_route():
    text_to_speak = request.json.get('text', '')
    response = eleven.stream_audio(text_to_speak)
    return response

@app.route('/play-audio/<path:filename>')
def play_audio(filename):
    """Serve audio files to be played in the browser."""
    return send_file(filename, as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)
