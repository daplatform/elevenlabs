import json
import requests
from config import Config  # Import the Config class

def fetch_images(query):
    # Construct the query
    full_query = f"{query} cartoon"
    
    # Set the URL and headers
    url = 'https://google.serper.dev/images'
    headers = {
        'X-API-KEY': Config.SERPER_API_KEY,  # Access the API key through the Config class
        'Content-Type': 'application/json'
    }
    
    # Create the data payload
    data = {
        'q': full_query
    }

    # Send the POST request
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

def get_first_thumbnail(query):
    images = fetch_images(query)
    
    # Check if images were retrieved and get the first thumbnail
    if images and 'images' in images and len(images['images']) > 0:
        first_image = images['images'][0]  # Get the first image record
        # Get the URL value next to 'thumbnailUrl'
        return first_image.get('thumbnailUrl')  # Correct key for the thumbnail URL
    else:
        print("No images found or error in response.")
        return None

def get_thumbnails_for_objects(objects):
    results = {}
    for obj in objects:
        thumbnail_url = get_first_thumbnail(obj)
        results[obj] = thumbnail_url  # Store the thumbnail URL in the results dictionary
    return results

def get_thumbnails_for_characters(characters):
    results = {}
    for char in characters:
        thumbnail_url = get_first_thumbnail(char)  # Fetch the thumbnail for each character
        results[char] = thumbnail_url  # Store the thumbnail URL in the results dictionary
    return results
