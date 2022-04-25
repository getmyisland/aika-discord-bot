import discord
from discord.ext import commands
import random
import requests


class MiscCommands(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command(description='Choose between a list of choices')
    async def choose(self, ctx, *choices: str):
        # Chooses between multiple choices
        await ctx.reply(random.choice(choices))

    @commands.command(description="Flip a coin")
    async def coinflip(self, ctx):
        # Flip a coin
        coin_side = random.randint(1, 2)

        if coin_side == 1:
            await ctx.reply('Heads')
        else:
            await ctx.reply('Tails')

    @commands.command()
    async def base64(self, ctx, *encode: str):
        resp = requests.get(f"https://some-random-api.ml/base64?encode={encode}")
        if 300 > resp.status_code >= 200:
            content = resp.json()
            await ctx.reply(content['base64'])
        else:
            await ctx.reply("Recieved a bad status code of " + str(resp.status_code))

    @commands.command()
    async def binary(self, ctx, *encode: str):
        resp = requests.get(f"https://some-random-api.ml/binary?encode={encode}")
        if 300 > resp.status_code >= 200:
            content = resp.json()
            await ctx.reply(content['binary'])
        else:
            await ctx.reply("Recieved a bad status code of " + str(resp.status_code))


# Must have a setup function
def setup(client):
    # Add the class to the cog
    client.add_cog(MiscCommands(client))
