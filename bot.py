import discord
import os
from dotenv import load_dotenv
from config import DISCORD_TOKEN
from llm_brain import generate_response

load_dotenv()

# User history storage: {user_id: [(role, text), ...]}
# We store only the last 10 messages to keep the context clean and to allow for continuation of stories
user_histories = {}

#Sends the messages to discord server
async def send_message(message, user_message, is_private):
    user_id = message.author.id
    
    # Get or create history for this user
    if user_id not in user_histories:
        user_histories[user_id] = []
    
    history = user_histories[user_id]
    
    try:
        # Generate response using the conversation history
        response = generate_response(user_message, history=history)
        
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)
            
        # Update history with the exchange
        user_histories[user_id].append(("User", user_message))
        user_histories[user_id].append(("PIO", response))
        
        # Trim history to prevent context bloat (keep last 10 turns)
        if len(user_histories[user_id]) > 20:
            user_histories[user_id] = user_histories[user_id][-20:]
            
    except Exception as e:
        print(f"Error sending message: {e}")

def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running (PIO_Bot_v2.1)') #Verification that bot is functional

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message.startswith('?'):
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(DISCORD_TOKEN)
