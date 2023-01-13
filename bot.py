import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load the discord bot token
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

command_prefix = '$'
description = 'Discord Bot made by GetMyIsland#2212.'
intents = discord.Intents.all()

# Create the bot
bot = commands.Bot(command_prefix=command_prefix,
                   activity=discord.Activity(name="birds", type=discord.ActivityType.watching),
                   status=discord.Status.idle,
                   description=description,
                   intents=intents
                   )


async def load_cog_files():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'cogs.{filename[:-3]} has loaded')


@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name)
    await load_cog_files()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # print('[{0.guild.name}] Message from {0.author}: {0.content}'.format(message))
    await bot.process_commands(message)

bot.run(DISCORD_TOKEN)
