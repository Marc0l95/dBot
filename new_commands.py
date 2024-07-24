
import random
from discord.ext import commands

class newCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='random')
    async def random_command(self, ctx):
        random_strings = ["String 1", "String 2", "String 3", "String 4"]
        response = random.choice(random_strings)
        await ctx.send(response)

def setup(bot):
    bot.add_cog(newCommands(bot))
