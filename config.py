import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
CHILD_NAME = os.getenv('CHILD_NAME')
CHILD_BIRTHDAY_STR = os.getenv('CHILD_BIRTHDAY')
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL')

#Allows LLM to mature with child's age and to keep within age appropriate safeguards
def calculate_age():
    birthday = datetime.strptime(CHILD_BIRTHDAY_STR, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return age

#Criteria given to LLM for age groups. Alter this for different ambiance based off your vison for PIO
def get_persona(age):
    if age <= 6:
        return "The Magical Phase: Use very simple language, emphasize imagination and animals, with clear happy morals. Keep stories rhythmic and short."
    elif age <= 11:
        return "The Curiosity Phase: Use engaging language, themes of friendship, school, and discovery. Develop more detailed plots."
    elif age <= 15:
        return "The Identity Phase: Use supportive and thoughtful language. Focus on resilience, self-discovery, and emotional optimism."
    else:
        return "The Young Adult Phase: Use sophisticated but warm language. Focus on reflective, nuanced optimism and mature storytelling."
