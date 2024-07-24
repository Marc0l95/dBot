# bot.py
import os
import discord
from discord.ext import commands
import openai
from dotenv import load_dotenv
import new_commands

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API')
GUILD_ID = int(os.getenv('GUILD_ID'))
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

openai.api_key = OPENAI_API_KEY

bot = cpo = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if not message.content.startswith('!'):
        return

    # Ensure the bot responds only in the specified server and channel
    if message.guild.id != GUILD_ID or message.channel.id != CHANNEL_ID:
        return

    if message.content.startswith('!random'):
        await bot.process_commands(message)
        return
    
    # Extract the command and query
    query = message.content[1:].strip()

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages = [
        {"role": "system", "content": "You are a knowledgeable gamer. Give on point explanations that are short but to the point. Be condescending and a little bit of a memer.:"},
        {"role": "user", "content": query}
    ]
    )

    await message.channel.send(response.choices[0].message['content'])

new_commands.setup(bot)

# Run the bot
bot.run(DISCORD_TOKEN)
