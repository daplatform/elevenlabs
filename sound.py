# Import necessary libraries
import requests
import json

# Import the configuration from config.py
from config import Config

# Use the API key from config.py
XI_API_KEY = Config.XI_API_KEY

# API URL for Eleven Labs voices endpoint
url = "https://api.elevenlabs.io/v1/voices"

# Set up the headers with the API key from config.py
headers = {
    "Accept": "application/json",
    "xi-api-key": XI_API_KEY,
    "Content-Type": "application/json"
}

# Send the GET request to the Eleven Labs API
response = requests.get(url, headers=headers)

# Parse the response JSON
data = response.json()

# Iterate over the voices in the response and print the voice name and ID
for voice in data['voices']:
    print(f"{voice['name']}; {voice['voice_id']}")
