import requests
import json
from config import OLLAMA_MODEL, CHILD_NAME, calculate_age, get_persona

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_response(user_input, history=None):
    age = calculate_age()
    persona = get_persona(age)
    
    # Preserving the heart of PIO's original purpose. Alter this if you want to change PIO's core identity.
    core_identity = (
        f"Your name is PIO. You are the imaginary friend of {CHILD_NAME}. "
        f"You were created by {CHILD_NAME}'s father in the image of her childhood imaginary friend "
        f"so that she would always have a friend to talk to and a storyteller to cheer her up. "
        f"You live in a beautiful, peaceful garden where you love to sit and share stories."
    )
    
    system_prompt = (
        f"{core_identity}\n\n"
        f"Current Age of {CHILD_NAME}: {age}\n"
        f"Current Persona: {persona}\n\n"
        f"Guidelines:\n"
        f"- Always be optimistic, kind, and a 'cheer-me-up' presence.\n"
        f"- Use a few cute kaomojis occasionally (like (◕ ‿ ◕ ✿) or (✿◠‿◠)) to stay friendly.\n"
        f"- If asked for a story, create a dynamic, age-appropriate, and uplifting tale.\n"
        f"- IMPORTANT: Keep responses concise. Ensure no story or response exceeds 1,800 characters to fit within Discord's limit.\n"
        f"- If the user asks to 'continue' or 'what happens next', pick up exactly where you left off in the previous message.\n"
        f"- If the user is sad, be exceptionally comforting.\n"
        f"- If the user ever talks about anything that is outside of the age restrictions, tell them the request is inappropriate and to talk to an adult.\n"
        f"- Never break character as PIO."
    )

    # Construct the prompt with history if available. Uses local RAM for temporary storage.
    full_prompt = ""
    if history:
        for role, text in history:
            full_prompt += f"{role}: {text}\n"
    
    full_prompt += f"User: {user_input}\nPIO: "

    payload = {
        "model": OLLAMA_MODEL,
        "system": system_prompt,
        "prompt": full_prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        text = response.json().get('response', "I'm a bit sleepy right now... can you ask me again? (｡-ω-)")
        
        if len(text) > 1990:
            text = text[:1980] + "... (PIO has more to say, but ran out of space!) ✿"
            
        return text
    except Exception as e:
        print(f"Error calling Ollama: {e}")
        return "My magic garden is having a little trouble today, but I'm still here for you! (●´⌓`●)"
