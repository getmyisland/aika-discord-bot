import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load the token
load_dotenv()
TOKEN = os.getenv('TOKEN')

command_prefix = '$'
description = '''Discord Bot made by GetMyIsland#2212'''
intents = discord.Intents.default()
intents.members = True

# Create the bot
bot = commands.Bot(command_prefix=command_prefix, activity=discord.Game(name="with her Piggy"), status=discord.Status.online, description=description, intents=intents)
cog_files = ['commands.animals', 'commands.misc', 'commands.talk']

for cog_file in cog_files:
    bot.load_extension(cog_file)
    print("%s has loaded." % cog_file)


@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print('[{0.guild.name}] Message from {0.author}: {0.content}'.format(message))
    await bot.process_commands(message)


bot.run(TOKEN)
