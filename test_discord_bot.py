# test_bot.py
import unittest
from unittest.mock import patch, AsyncMock
import discord
from discord.ext import commands
import openai
from bot import bot

class TestDiscordBot(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.bot = bot
        self.ctx = AsyncMock()
        self.ctx.send = AsyncMock()
        self.ctx.message = AsyncMock()
        self.ctx.author = AsyncMock()
        self.ctx.guild = AsyncMock()

    @patch('openai.Completion.create')
    async def test_command_response(self, mock_openai_create):
        # Mock the OpenAI API response
        mock_openai_create.return_value.choices[0].text = "This is a test response."

        # Simulate a command call
        await self.bot.get_command('command').callback(self.bot, self.ctx, question="What is AI?")
        
        # Check if the bot sends the correct response
        self.ctx.send.assert_called_once_with("This is a test response.")
    
    @patch('openai.Completion.create')
    async def test_command_error_handling(self, mock_openai_create):
        # Mock the OpenAI API to raise an exception
        mock_openai_create.side_effect = Exception("API Error")
        
        # Simulate a command call
        await self.bot.get_command('command').callback(self.bot, self.ctx, question="What is AI?")
        
        # Check if the bot sends the error message
        self.ctx.send.assert_called_once_with("An error occurred: API Error")

if __name__ == '__main__':
    unittest.main()
