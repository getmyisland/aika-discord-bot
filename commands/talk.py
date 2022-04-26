import string

import discord
from discord.ext import commands
import random
from commands.ai.ai import get_response


class TalkCommand(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command(description="Talk with the bot", aliases=['t'])
    async def talk(self, ctx, *, message):
        texts = []
        message = [letters.lower() for letters in message if letters not in string.punctuation]
        message = ''.join(message)
        texts.append(message)

        await ctx.reply(get_response(self, texts))


# Must have a setup function
def setup(client):
    # Add the class to the cog
    client.add_cog(TalkCommand(client))
