# PIO_Bot_v2

## Pio's Purpose

I once heard that if you want to create, create things for people that you love.

PIO Bot_v2 is a much needed improvement to the previous chat bot that I made for my daughter. Pio is the name of my daughter's childhood imaginary friend. I wanted to preserve this childhood innocence in the form of a digital friend that she could call on for stories that will brighten her day.

Pio is now a locally run chat bot that is served through Discord (or any other messaging app you trust) that is powered by artificial intelligence using Ollama. Pio is designed with age appropriate safeguards intended to provide a safe and entertaining environment for a child of any age. 

As my daughter has grown, her taste in stories has grown and matured as well. With this in mind, I designed the new Pio to know how old she is and to tell appropriate stories based off her age. There is an example environmental file (example.env) provided to give you an idea of what information to give to the local AI. 

### Disclaimer

This bot is inteded for LOCAL USE ONLY, and precautions have been taken to ensure personal information is not shared outside of the local machine and the messaging interface used (i.e. Discord). If using this for your own child (or self), please be sure to keep your information secure. 

Again, it is intended to run on your personal computer/server. No data is given to me or any other entity to my knowledge. Please give personal information with discretion.

---

## Improvements from original PIO

- Removal of previously hardcoded stories from version 1
- Integration with Ollama LLM for more dynaic story telling 
- Short term memory of conversation added so the story can continue even if it reaches Discord's 2000 character limit

## Setting up Ollama locally

- Use this video to learn how to set up Ollama locally: https://youtu.be/UtSSMs6ObqY?si=RlXsm0IgpK5QPpZY

- I used gemma4:31b-cloud for mine. I tried using Gemma2, which is an older version of Gemma, and is still fantastic for this use case, but I found it not as verbose as the Gemma4 model. Depending on the hardware you're using or the amount of context you want given (which can also be adjusted with manual configuration), choose the model to your liking.

- If you decide to use a cloud-based model, you will need to log in/make an account with ollama. This can be done by simply typing ```ollama login``` which will open a browser login portal.

- A LLM of your choice will need to be downloaded after Ollama installation using ```ollama run [LLM_Model]```.

- Add this LLM model name to your .env file using the OLLAMA_MODEL variable

## How to use PIO_Bot_v2

- Please be sure to install the following dependencies into your python environment before attempting to launch PIO using the command ```pip install [dependency_nam]```. Otherwise you may get errors:
    - discord.py
    - requests
    - dotenv
- Use template from the example.env file to fill in user (child or self) info for Ollama to generate appropriate stories**
- ** See Disclaimer section above for more information on data privacy.
- If using Discord as medium for text generation, you will need to follow the steps on Discord to create a channel for the bot to access and how to create the bot
    - How to make a discord bot: https://discordpy.readthedocs.io/en/latest/discord.html
- After creating your bot, run ```python3 main_PIO.py``` in the terminal (linux/MacOS) or Command Line (Windows)
    - Please make sure you have Python 3 downloaded to ensure code exectiton
- You should see a line in the terminal that reads: [Your_bot_name] is now running. This means that it is operational and ready for use.
- Navigate to your Discord channel with the bot and say hello!

## Other notes

- We have tested and improved upon Pio's safety in conversations with children. We still recommend parental supervison for two reasons
    1. LLMs are still in an infantile stage of development and should be used with caution.
    2. So parents can also have fun reading along to Pio's stories with their children and have some quality time together!
- I have some custom prompts that tell Pio's purpose that serve as a note to my daughter. Pio will state it's purpose when asked who it is. If you wish to remove this, alter the core_identity variable in the generate_response() function in the llm_brain.py file. Leaving or removing this prompt will not affect the PIO's function.

- I hope this inspires others to make projects for the people they love the most! :D
