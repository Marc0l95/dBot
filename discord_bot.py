# bot.py
import os
import discord
from discord.ext import commands
import openai

# Load environment variables
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI API
openai.api_key = OPENAI_API_KEY

# Define the command prefix for the bot
bot = commands.Bot(command_prefix='!')

# Define the command
@bot.command(name='command')
async def command(ctx, *, question: str):
    try:
        # Interact with OpenAI's GPT-4 API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=question,
            max_tokens=150
        )
        # Extract the response text
        answer = response.choices[0].text.strip()

        # Send the response to the Discord channel
        await ctx.send(answer)
    except Exception as e:
        # Handle any exceptions
        await ctx.send(f"An error occurred: {str(e)}")

# Run the bot
bot.run(DISCORD_TOKEN)
