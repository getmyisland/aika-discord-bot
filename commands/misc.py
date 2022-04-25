import discord
from discord.ext import commands
import random


class MiscCommands(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command(description='Choose between a list of choices')
    async def choose(self, ctx, *choices: str):
        """Chooses between multiple choices."""
        await ctx.reply(random.choice(choices))

    @commands.command(description="Flip a coin")
    async def coinflip(self, ctx):
        """Flip a coin."""
        coin_side = random.randint(1, 2)

        if coin_side == 1:
            await ctx.reply('Heads')
        else:
            await ctx.reply('Tails')


# Must have a setup function
def setup(client):
    # Add the class to the cog
    client.add_cog(MiscCommands(client))
