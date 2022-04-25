import discord
from discord.ext import commands
import requests


class AnimalCommands(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command(description="Displays all supported animal commands")
    async def animals(self, ctx):
        description = '$dog' + '\t' + '= Get a random dog image \n' \
                                      '$dogfact' + '\t' + '= Get a random dog fact'

        embed = discord.Embed(
            title="Animal commands",
            description=description
        )
        await ctx.send(embed=embed)

    @commands.command(description="Gives out a random dog image")
    async def dog(self, ctx):
        # Making a GET request to the endpoint
        resp = requests.get("https://some-random-api.ml/img/dog")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title="Random Dog picture"
            )
            embed.set_image(url=content['link'])
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Recieved a bad status code of {resp.status_code}.")

    @commands.command(description="Gives out a random dog fact")
    async def dogfact(self, ctx):
        # Making a GET request to the endpoint
        resp = requests.get("https://some-random-api.ml/facts/dog")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title="Random Dog fact",
                description=content['fact']
            )
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Recieved a bad status code of {resp.status_code}.")

    @commands.command(description="Gives out a random panda image")
    async def panda(self, ctx):
        # Making a GET request to the endpoint
        resp = requests.get("https://some-random-api.ml/img/panda")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title="Random Panda picture"
            )
            embed.set_image(url=content['link'])
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Recieved a bad status code of {resp.status_code}.")

    @commands.command(description="Gives out a random panda fact")
    async def pandafact(self, ctx):
        # Making a GET request to the endpoint
        resp = requests.get("https://some-random-api.ml/facts/panda")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title="Random Panda fact",
                description=content['fact']
            )
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Recieved a bad status code of {resp.status_code}.")


# Must have a setup function
def setup(client):
    # Add the class to the cog
    client.add_cog(AnimalCommands(client))
