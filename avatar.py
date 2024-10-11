import subprocess
import json
import random  # Import the random module
from config import Config  # Import the Config class

# Use the API key from config.py
API_KEY = Config.GEMINI_API_KEY
GEMINI_API_URL = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}'

# Define personas with 3 boys and 3 girls
PERSONAS = [
        {"name": "Aria", "attributes": "climate finance, equitable funding, NCQG, SDGs, just transition, climate technology", "voice_id": "9BWtsMINqrJLrRacOk9x"},
        {"name": "Roger", "attributes": "carbon markets, Article 6, mitigation strategies, non-market mechanisms, innovation, technology-driven", "voice_id": "CwhRBWXzGAHq8TQ4Fs17"},
        {"name": "Sarah", "attributes": "financial architect, Loss and Damage Fund, gender inclusion, climate finance, Indigenous Peoples", "voice_id": "EXAVITQu4vr4xnSDxMaL"},
        {"name": "Laura", "attributes": "adaptation advocate, vulnerable communities, climate strategist, capacity-building, resilience, children and youth", "voice_id": "FGY2WhTYpPnrIDTdsKH5"},
        {"name": "Charlie", "attributes": "proactive leader, adaptation finance, land use, debt-for-climate, community empowerment, Just Transition", "voice_id": "IKne3meq5aSn9XLyUdCD"},
        {"name": "George", "attributes": "scalability expert, fossil fuel subsidies, ocean action, mitigation, global stocktake, low-carbon innovation", "voice_id": "JBFqnCBsd6RMkjVDRZzb"}
]

def generate_dialogue(topic):
    # Shuffle the personas to randomize the order
    shuffled_personas = random.sample(PERSONAS, len(PERSONAS))

    # Create the prompt for Gemini using all shuffled personas
    personas_prompt = ', '.join([f"{persona['name']} ({persona['attributes']})" for persona in shuffled_personas])
    prompt = (
        f"Generate a dialogue script using random personas, not in a cyclic order of speaking, consisting of 10 lines on the topic: ~{topic}~. "
        f"The dialogue should involve the following personas: {personas_prompt}. "
        f"Use '@' to indicate usernames, ':' to separate the username from dialogue, and '|' to signify the end of each line. "
        "The script should incorporate random names for the personas and explore a complex interplay of emotions, conflicts, and negotiation, ultimately leading to a satisfying conclusion. "
        "Names should not be presented in sequence; some personas may not speak at all during the dialogue."
    )

    prompt_data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    # Call Gemini API using curl
    curl_command = [
        'curl',
        '-H', 'Content-Type: application/json',
        '-d', json.dumps(prompt_data),
        '-X', 'POST', GEMINI_API_URL
    ]

    try:
        result = subprocess.run(curl_command, capture_output=True, text=True)
        result.check_returncode()  # Raise an error for non-zero exit codes

        response_json = json.loads(result.stdout)
        content = response_json['candidates'][0]['content']['parts'][0]['text'].strip()

        # Split the generated dialogue into lines
        dialogues = content.split('|')

        # Create a list of tuples containing the dialogue line and corresponding voice ID
        dialogue_with_voices = []
        for i, dialogue in enumerate(dialogues):
            # Randomly select a voice ID from the shuffled personas
            voice_id = shuffled_personas[random.randint(0, len(shuffled_personas) - 1)]['voice_id']
            dialogue_with_voices.append((dialogue.strip(), voice_id))

        return dialogue_with_voices

    except Exception as e:
        raise RuntimeError(f'Error generating dialogue: {str(e)}')
