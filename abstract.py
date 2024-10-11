import requests
import json
import os
import base64
from config import Config  # Import your configuration for the API keys

IMAGE_FOLDER = os.path.join('static', 'images')

def generate_image(prompt):
    """Generate an image using the Together API."""
    # Set up the API endpoint and your API key
    url = "https://api.together.xyz/v1/images/generations"
    api_key = Config.TOG_API_KEY  # Assuming you have the API key in your config

    # Prepare the payload for the request
    data = {
        "model": "black-forest-labs/FLUX.1-schnell",
        "prompt": prompt,
        "width": 1024,
        "height": 768,
        "steps": 4,
        "n": 1,
        "response_format": "b64_json"
    }

    # Headers including the API key for authorization
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Make the POST request to generate the image
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        result = response.json()
        image_data = result['data'][0]['b64_json']
        print("Image generated successfully!")
        return image_data  # Return the base64 image data
    else:
        print(f"Failed to generate image: {response.status_code}")
        print("Response:", response.text)
        return None

def save_image(image_data, file_name):
    """Save base64 image data to a PNG file."""
    file_path = os.path.join(IMAGE_FOLDER, file_name)

    # Decode the base64 data
    os.makedirs(IMAGE_FOLDER, exist_ok=True)
    image_data_decoded = base64.b64decode(image_data)

    # Write the decoded image to a file
    with open(file_path, 'wb') as image_file:
        image_file.write(image_data_decoded)
    print(f"Image saved to {file_path}")

def process_conc(concept):
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={Config.GEMINI_API_KEY}'
    headers = {'Content-Type': 'application/json'}

    # Create the prompt for the concept
    prompt = f"Explain the following concept to a 5-year-old autistic child in 1-2 simple sentences. Use a clear example to help the child understand: {concept}"

    # The body of the POST request
    data = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response JSON
            result = response.json()
            # Extract the content text
            content = result['candidates'][0]['content']['parts'][0]['text']
            return content
        else:
            return f"Error: Unable to fetch data from Gemini API (status code: {response.status_code})."

    except Exception as e:
        return f"Error: {str(e)}"

def process_metadata_for_concept(concept):
    # New function to get the metadata prompt based on the concept
    prompt = f"Describe an image that visually explains {concept} to a 5-year-old in one sentence, including the setting, background, and key objects, all in a focused and concise way."
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={Config.GEMINI_API_KEY}'
    headers = {'Content-Type': 'application/json'}

    # The body of the POST request
    data = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response JSON
            result = response.json()
            # Extract the content text
            content = result['candidates'][0]['content']['parts'][0]['text']
            
            # Generate the image based on the content extracted
            image_data = generate_image(content)

            # Save the image to a file
            if image_data:
                save_image(image_data, "output_image.png")

            # Return both the content and the image data
            return content, image_data

        else:
            return None, f"Error: Unable to fetch data from Gemini API (status code: {response.status_code})."

    except Exception as e:
        return None, f"Error: {str(e)}"
