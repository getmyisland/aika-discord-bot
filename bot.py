import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random
import requests

# Load the token
load_dotenv()
TOKEN = os.getenv('TOKEN')

command_prefix = '$'
description = '''Discord Bot made by GetMyIsland'''
intents = discord.Intents.default()
intents.members = True

# Create the bot
bot = commands.Bot(command_prefix=command_prefix, activity=discord.Game(name="with her Piggy"), status=discord.Status.offline, description=description, intents=intents)


@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print('[{0.guild.name}] Message from {0.author}: {0.content}'.format(message))
    await bot.process_commands(message)


@bot.command(description="Talk with the bot")
async def talk(ctx, *content: str):
    await ctx.send('Coming Soon!')


@bot.command(description="Displays all supported animal commands")
async def animals(ctx):
    description = '$dog' + '\t' + '= Get a random dog image \n' \
                  '$dogfact' + '\t' + '= Get a random dog fact'

    embed = discord.Embed(
        title="Animal commands",
        description=description
    )
    await ctx.send(embed=embed)


@bot.command(description="Gives out a random dog image")
async def dog(ctx):
    # Making a GET request to the endpoint
    resp = requests.get("https://some-random-api.ml/img/dog")
    # Checking if response has a healthy status code
    if 300 > resp.status_code >= 200:
        content = resp.json()
        embed = discord.Embed(
            title="Random dog picture"
        )
        embed.set_image(url=content['link'])
        await ctx.reply(embed=embed)
    else:
        await ctx.reply("Recieved a bad status code of {resp.status_code}.")


@bot.command(description="Gives out a random dog fact")
async def dogfact(ctx):
    # Making a GET request to the endpoint
    resp = requests.get("https://some-random-api.ml/facts/dog")
    # Checking if response has a healthy status code
    if 300 > resp.status_code >= 200:
        content = resp.json()
        embed = discord.Embed(
            title="Random dog fact",
            description=content['fact']
        )
        await ctx.reply(embed=embed)
    else:
        await ctx.reply("Recieved a bad status code of {resp.status_code}.")


@bot.command(description='Choose between a list of choices')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.reply(random.choice(choices))


@bot.command(description="Flip a coin")
async def coinflip(ctx):
    """Flip a coin."""
    coinside = random.randint(1, 2)

    if coinside == 1:
        await ctx.reply('Heads')
    else:
        await ctx.reply('Tails')


bot.run(TOKEN)