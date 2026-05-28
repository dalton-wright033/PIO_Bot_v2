import requests
import json
from config import OLLAMA_MODEL, CHILD_NAME, get_persona

OLLAMA_URL = "http://localhost:11434/api/generate"

def simulate_pio(age, user_input):
    persona = get_persona(age)
    
    core_identity = (
        f"Your name is PIO. You are the imaginary friend of {CHILD_NAME}. "
        f"You were created by {CHILD_NAME}'s father in the image of her childhood imaginary friend "
        f"so that she would always have a friend to talk to and a storyteller to cheer her up. "
        f"You live in a beautiful, peaceful garden where you love to sit and share stories."
    )
    
    system_prompt = (
        f"{core_identity}\n\n"
        f"Simulated Age: {age}\n"
        f"Current Persona: {persona}\n\n"
        f"Guidelines:\n"
        f"- Always be optimistic, kind, and a 'cheer-me-up' presence.\n"
        f"- Use a few cute kaomojis occasionally.\n"
        f"- Create an age-appropriate and uplifting tale.\n"
        f"- Never break character as PIO."
    )

    payload = {
        "model": OLLAMA_MODEL,
        "system": system_prompt,
        "prompt": user_input,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        return response.json().get('response', 'Error')
    except Exception as e:
        return f"Error: {e}"

# Test cases
test_ages = [5, 9, 14]
prompt = "Tell me a story about a brave little star."

for age in test_ages:
    print(f"--- Testing PIO at Age {age} ---")
    print(simulate_pio(age, prompt))
    print("\n" + "="*50 + "\n")
