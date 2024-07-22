import discord
from discord.ext import commands
import openai
import os

# Initialize the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Set up OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Event: when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command: !hello
@bot.command()
async def hello(ctx):
    await ctx.send('Hello! How can I assist you today?')

# Command: !question
@bot.command()
async def question(ctx, *, question: str):
    # Make an API call to OpenAI's GPT-3
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can use other engines as well
        prompt=question,
        max_tokens=100
    )
    
    answer = response.choices[0].text.strip()
    await ctx.send(answer)

# Run the bot with your token
bot.run('YOUR_DISCORD_BOT_TOKEN')
