import requests
import json

# Define the API endpoint and your API key
url = "https://api.together.xyz/v1/images/generations"
api_key = "c0f8ab71542b72af5a2516d97f8ad45e9abd75bfb7d5f7155527a3c41a0fe504"

# Prepare the payload for the request
data = {
    "model": "black-forest-labs/FLUX.1-schnell",
    "prompt": "car image",
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
    print("Base64 Image Data:")
    print(image_data)  # Print the Base64 image data
else:
    print(f"Failed to generate image: {response.status_code}")
    print("Response:", response.text)
