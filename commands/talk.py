import discord
from discord.ext import commands
import random


class TalkCommand(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command(description="Talk with the bot")
    async def talk(self, ctx, *content: str):
        await ctx.send('Coming Soon!')


# Must have a setup function
def setup(client):
    # Add the class to the cog
    client.add_cog(TalkCommand(client))
